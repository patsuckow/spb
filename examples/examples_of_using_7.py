"""
Download one file or all files from a folder Google Drive using
google-api-client.

First you need to create a service account and get a key. How to do this can
be read on the official website https://developers.google.com/
https://console.cloud.google.com/iam-admin/iam
https://developers.google.com/drive/api/v3/about-sdk
https://developers.google.com/drive/api/v3/reference/files
https://github.com/googleapis/google-api-python-client
"""
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
import io
import pprint
from spb import SimpleProgressBar as spb


SERVICE_ACCOUNT_FILE = 'client_secret_really_long_ID_.json'
CHUNK_SIZE = 1024*1024

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/drive']
)
service = build('drive', 'v3', credentials=credentials)

# Get a list of files in the folder to which we have (or were given)
# access through https://console.cloud.google.com/iam-admin/iam
pp = pprint.PrettyPrinter(indent=4)
results = service.files().list(
    pageSize=1000, fields="files(id, name, mimeType)"
).execute()
# pp.pprint(results)


# 1. Download one file you need:
file_id = '1d3V33JRUS0i0cRHLqnmQ1tfT8peXt-9f'
request = service.files().get_media(fileId=file_id)
filename = 'thinkcomplexity2.pdf'
fh = io.FileIO(filename, 'wb')
downloader = MediaIoBaseDownload(fh, request, chunksize=CHUNK_SIZE)

pb = spb(speed='show', load='show',
         end_msg=f' "{filename}" download complete.\n')

done = False
while done is False:
    status, done = downloader.next_chunk()
    if status:
        pb.iteration = int(status.progress() * 100)
        pb.loaded_bytes += CHUNK_SIZE  # for ⭳[weight] & [speed]
        pb.progress_bar()


# 2. Download all files from a folder.
# All that is needed is to cycle through the selection result stored in
# 'results' and select the file id and their names, while excluding the folder
# itself from the selection.
for i in results['files']:
    if i['mimeType'] != 'application/vnd.google-apps.folder':
        file_id = i['id']
        request = service.files().get_media(fileId=file_id)
        filename = i['name']
        fh = io.FileIO(filename, 'wb')
        downloader = MediaIoBaseDownload(fh, request, chunksize=CHUNK_SIZE)
        pb = spb(speed='show', load='show',
                 end_msg=f' "{filename}" download complete.\n')
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            if status:
                pb.iteration = int(status.progress() * 100)
                pb.loaded_bytes += CHUNK_SIZE
                pb.progress_bar()

# Notice:
# It is not possible to upload the file to Google Drive and show the upload
# indicator, since the googleapiclient.http.MediaFileUpload class of Google
# Drive API v.3 does not support returning status.progress().
# https://developers.google.com/drive/api/v3/manage-uploads
# https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.http.MediaFileUpload-class.html

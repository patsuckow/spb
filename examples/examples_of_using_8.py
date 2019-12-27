"""
Download from Google drive using requests module and not using google-api-client.

If you need to count the number of bytes downloaded, and the download speed,
not knowing the content-length, then you need to remove the progress bar and
remove the percentage.
"""
import requests
from spb import SimpleProgressBar as spb

# We have a link to a public file:
# https://drive.google.com/file/d/1d3V33JRUS0i0cRHLqnmQ1tfT8peXt-9f/view?usp=sharing
# From the link we take the file id:
file_id = '1d3V33JRUS0i0cRHLqnmQ1tfT8peXt-9f'

DOWNLOAD_URL = 'https://docs.google.com/uc?export=download'


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None


try:
    session = requests.Session()
    response = session.get(DOWNLOAD_URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)
    if token:
        response = session.get(
            DOWNLOAD_URL,
            params={'id': file_id, 'confirm': token},
            stream=True
        )
    file_name = response.headers.get('Content-Disposition').split("\'")[-1]

    if response.status_code == requests.codes.ok:
        # If content-length unknown, then REQUIRE setup next parameters:
        pb = spb(
            progress_bar='hide',
            progress_str='',
            percent='hide',
            variant_timer='increasing',
            speed='show',
            load='show'
        )
        with open(file_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=32768):
                if chunk:
                    pb.loaded_bytes += 32768
                    f.write(chunk)
                    next(pb)
            else:
                print('\n')
    else:
        raise ConnectionError
except (ConnectionError, KeyboardInterrupt):
    print('\n\x1b[?25h Work aborted.')

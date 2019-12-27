"""
How uses a load file indicator and progress bar indicator (the type of
indicator will depend on the settings that you set)
"""

# Example № 1 (Download single file using requests module):
import requests
from spb import SimpleProgressBar as spb


url = 'http://greenteapress.com/complexity2/thinkcomplexity2.pdf'
file_name = url.split("/")[-1]  # so as not to import the os module

try:
    req = requests.get(url, stream=True)
    if req.status_code == requests.codes.ok:
        # Find out length (in bytes) of the transmitted content
        content_length = int(str(req.headers.get('content-length')))
        # Translation of bytes into kilobytes, while 1 kilobyte is added to
        # approximately take into account the digits after the decimal point,
        # that is, an incomplete kilobyte.
        kB = int((content_length / 1024) + 1)
        pb = spb(stop=kB, speed='show', load='show')
        with open(file_name, "wb") as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pb.loaded_bytes += len(chunk)  # for ⭳[weight] & [speed]
                    next(pb)
    else:
        raise ConnectionError
except (ConnectionError, KeyboardInterrupt):
    print('\n\x1b[?25h Work aborted.')


# Example using № 2 (Download files from url list one by one using requests
# module):
import requests
from spb import SimpleProgressBar as spb

urls = [
    "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
    "https://www.irs.gov/pub/irs-pdf/f4506t.pdf",
    "https://www.irs.gov/pub/irs-utl/transaction_codes_pocket_guide.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
    "https://pythonworld.ru/uploads/pythonworldru.pdf",
    "http://img105.job1001.com/upload/adminnew/2015-02-03/1422940854-U8D8OE4.pdf",
    "http://greenteapress.com/complexity2/thinkcomplexity2.pdf",
    "http://inventwithpython.com/makinggames.pdf"
]

for url in urls:
    file_name = url.split("/")[-1]
    try:
        req = requests.get(url, stream=True)
        if req.status_code == requests.codes.ok:
            content_length = int(str(req.headers.get('content-length')))
            kB = int((content_length / 1024) + 1)
            pb = spb(stop=kB, speed='show', load='show')
            with open(file_name, "wb") as f:
                for chunk in req.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        pb.loaded_bytes += len(chunk)
                        next(pb)
        else:
            raise ConnectionError
    except (ConnectionError, KeyboardInterrupt):
        print('\n\x1b[?25h Work aborted.')


# Example using № 3 (Download files from url list one by one using urllib3):
# pip install urllib3
import urllib3
from spb import SimpleProgressBar as spb


urls = [
    "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
    "https://www.irs.gov/pub/irs-pdf/f4506t.pdf",
    "https://www.irs.gov/pub/irs-utl/transaction_codes_pocket_guide.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
    "https://pythonworld.ru/uploads/pythonworldru.pdf",
    "http://img105.job1001.com/upload/adminnew/2015-02-03/1422940854-U8D8OE4.pdf",
    "http://greenteapress.com/complexity2/thinkcomplexity2.pdf",
    "http://inventwithpython.com/makinggames.pdf"
]

pool = urllib3.PoolManager()

for url in urls:
    file_name = url.split("/")[-1]
    try:
        req = pool.request('GET', url, preload_content=False)
        if req.status == 200:
            content_length = int(req.headers['Content-Length'])
            kB = int((content_length / 1024) + 1)
            pb = spb(stop=kB, speed='show', load='show')
            with open(file_name, 'wb') as f:
                for chunk in req.stream(1024):
                    if chunk:
                        f.write(chunk)
                        pb.loaded_bytes += len(chunk)
                        next(pb)
        else:
            raise ConnectionError
    except (ConnectionError, KeyboardInterrupt):
        print('\n\x1b[?25h Work aborted.')


# Example using № 4 (Download multiple files (Parallel/bulk download) using
# requests module):
import requests
from multiprocessing.pool import ThreadPool
from spb import SimpleProgressBar as spb


urls = [
    "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
    "https://www.irs.gov/pub/irs-pdf/f4506t.pdf",
    "https://www.irs.gov/pub/irs-utl/transaction_codes_pocket_guide.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
    "https://pythonworld.ru/uploads/pythonworldru.pdf",
    "http://img105.job1001.com/upload/adminnew/2015-02-03/1422940854-U8D8OE4.pdf",
    "http://greenteapress.com/complexity2/thinkcomplexity2.pdf",
    "http://inventwithpython.com/makinggames.pdf"
]


def url_response(urls):
    for url in urls:
        try:
            file_name = url.split("/")[-1]
            req = requests.get(url, stream=True)
            if req.status_code == requests.codes.ok:
                content_length = int(str(req.headers.get('content-length')))
                kB = int((content_length / 1024) + 1)
                pb = spb(stop=kB, speed='show', load='show')
                with open(file_name, "wb") as f:
                    for chunk in req.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            pb.loaded_bytes += len(chunk)
                            next(pb)
            else:
                raise ConnectionError
        except (ConnectionError, KeyboardInterrupt):
            print('\n\x1b[?25h Work aborted.')


ThreadPool(len(urls)).imap_unordered(url_response, urls)
url_response(urls)

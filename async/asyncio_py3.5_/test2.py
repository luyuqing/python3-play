import requests
import time
import concurrent.futures
import threading


thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print("Done reading {}, length of content is {}".format(url, len(response.content)))


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org/",
        "https://requests.readthedocs.io/en/master/user/advanced/"
    ] * 50
    start = time.time()
    download_all_sites(sites)
    duration = time.time() - start
    print("Duration is {} seconds".format(duration))

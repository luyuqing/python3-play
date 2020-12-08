import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print('Proc {} reads {}, length of content is {}'.format(name, url, len(response.content)))


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == '__main__':
    sites = [
        "https://www.jython.org/",
        "https://requests.readthedocs.io/en/master/user/advanced/"
    ] * 50
    start = time.time()
    download_all_sites(sites)
    duration = time.time() - start
    print("Duration is {} seconds".format(duration))
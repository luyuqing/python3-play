# synchronous I/O bound

import requests
import time


# # regular requests, not using session object
# def download_site(url):
#     response = requests.get(url)
#     print("Done reading {}, length of content is {}".format(url, len(response.content)))


# def download_all_sites(sites):
#     for url in sites:
#         download_site(url)


# using session object is much faster
def download_site(url, session):
    with session.get(url) as response:
        print("Done reading {}, length of content is {}".format(url, len(response.content)))


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org/",
        "https://requests.readthedocs.io/en/master/user/advanced/"
    ] * 50
    start = time.time()
    download_all_sites(sites)
    duration = time.time() - start
    print("Duration is {} seconds".format(duration))

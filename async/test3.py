import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Done reading {}, length of content is {}".format(url, len(response.content)))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    sites = [
        "https://www.jython.org/",
        "https://requests.readthedocs.io/en/master/user/advanced/"
    ] * 50
    start = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start
    print("Duration is {} seconds".format(duration))

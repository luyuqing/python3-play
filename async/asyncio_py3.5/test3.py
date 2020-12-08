# https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/

import asyncio


# @asyncio.coroutine
# def countdown(letter, n):
#     while n > 0:
#         print("Letter: {}, n: {}".format(letter, n))
#         yield from asyncio.sleep(1)
#         n -= 1


# loop = asyncio.get_event_loop()
# tasks = [
#     asyncio.ensure_future(countdown("A", 2)),
#     asyncio.ensure_future(countdown("B", 3))
# ]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# This code works the same as above if uncommented
async def countdown(letter, n):
    while n > 0:
        print("Letter: {}, n: {}".format(letter, n))
        await asyncio.sleep(1)
        n -= 1


loop = asyncio.get_event_loop()
task1 = loop.create_task(countdown("A", 2))
task2 = loop.create_task(countdown("B", 3))
loop.run_until_complete(asyncio.wait([task1, task2]))
loop.close()

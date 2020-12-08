import asyncio


async def inner():
    return 1


async def outer():
    print(await inner())


loop = asyncio.get_event_loop()
task = loop.create_task(outer())
loop.run_until_complete(asyncio.wait([task]))
loop.close()


# async def inner2():
#     return 2


# async def outer2():
#     print(await inner2())


# loop = asyncio.get_event_loop()
# task1 = loop.create_task(outer())
# task2 = loop.create_task(outer2())
# loop.run_until_complete(asyncio.wait([task1, task2]))
# loop.close()

import asyncio


async def find_divisibles(inrange, div_by):
    print("Finding... in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)

        # suspend intentionally
        if i % 500000 == 0:
            await asyncio.sleep(0.0001)

    print("Done... in range {} divisible by {}".format(inrange, div_by))
    return located


# comment out line 29 and uncomment 24, 30, 31 if want to return results
async def main():
    divs1 = loop.create_task(find_divisibles(50800000, 34113))
    divs2 = loop.create_task(find_divisibles(100052, 3210))
    divs3 = loop.create_task(find_divisibles(500, 3))
    await asyncio.wait([divs1, divs2, divs3])
    # return divs1, divs2, divs3


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # d1, d2, d3 = loop.run_until_complete(main())
    # print(d2.result())
    loop.close()

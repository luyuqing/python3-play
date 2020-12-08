# synchronous


def find_divisibles(inrange, div_by):
    print("Finding... in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)

    print("Done... in range {} divisible by {}".format(inrange, div_by))
    return located


def main():
    divs1 = find_divisibles(50800000, 34113)
    divs2 = find_divisibles(100052, 3210)
    divs3 = find_divisibles(500, 3)


if __name__ == '__main__':
    main()

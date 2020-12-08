import os
from multiprocessing import Process, current_process


def square(num):
    """
    Example output:
    1 squares to result: 1.
    The process is <Process(Process-1, started)>.
    The process_id is 26133.
    Current process_name is Process-1.
    2 squares to result: 4.
    The process is <Process(Process-2, started)>.
    The process_id is 26134.
    Current process_name is Process-2.
    4 squares to result: 16.
    The process is <Process(Process-4, started)>.
    The process_id is 26136.
    Current process_name is Process-4.
    3 squares to result: 9.
    The process is <Process(Process-3, started)>.
    The process_id is 26135.
    Current process_name is Process-3.

    """

    res = num * num
    print("{} squares to result: {}.".format(num, res))
    process_id = os.getpid()
    print("The process is {}.".format(process))
    print("The process_id is {}.".format(process_id))
    process_name = current_process().name
    print("Current process_name is {}.".format(process_name))


if __name__ == '__main__':
    nums = [1, 2, 3, 4]

    for n in nums:
        process = Process(target=square, args=(n,))
        process.start()
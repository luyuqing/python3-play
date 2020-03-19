import os
import time
from multiprocessing import Process, current_process


"""
.join() just means "wait for this [thread/process] to complete".
The name join is used because the multiprocessing module's API is meant to look as similar to the threading module's API,
and the threading module uses join for its Thread object.
Using the term join to mean "wait for a thread to complete" is common across many programming languages,
so Python just adopted it as well.

These threads run in parallel:

d.start()
t.start()
d.join()
t.join()

and these run sequentially:

d.start()
d.join()
t.start()
t.join()

"""


def square(numbers):
    for number in numbers:
        time.sleep(0.5)
        result = number * number
        print("The number {} squares to {}.".format(number, result))


if __name__ == '__main__':

    processes = []
    numbers = range(100)

    # This will only run process at a time
    # for i in range(50):
    #     process = Process(target=square, args=(numbers,))
    #     processes.append(process)
    #     process.start()
    #     process.join()

    # This will run all processes paralell
    for i in range(50):
        process = Process(target=square, args=(numbers,))
        processes.append(process)
        process.start()
    # process implicitely do this without using .join()
    for process in processes:
        process.join()
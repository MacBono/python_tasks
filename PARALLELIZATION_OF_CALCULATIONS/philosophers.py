#!/usr/bin/python3
import threading
import time
from classes import Philosopher,ChopStick,Servant


def main():
    n = 5
    servant = Servant(n - 1)
    chops = [ChopStick(i) for i in range(n)]
    phils = [Philosopher(i, chops[i], chops[(i + 1) % n], servant) for i in range(n)]

    for i in range(n):
        phils[i].start()


if __name__ == "__main__":
    main()

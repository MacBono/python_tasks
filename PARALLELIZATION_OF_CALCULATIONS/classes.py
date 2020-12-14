#!/usr/bin/python3
import threading 
import time
import random
import sys

class Servant(object):

    def __init__(self, val):
        self.lock = threading.Condition(threading.Lock())
        self.value = val

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1


class ChopStick(object):

    def __init__(self, id):
        self.id = id
        self.user = -1
        self.lock = threading.Condition(threading.Lock())
        self.working = False

    def grab(self, user):
        with self.lock:
            while self.working:
                self.lock.wait()
            self.user = user
            self.working = True
            sys.stdout.write("Philosopher[%s] grabbed chopstick[%s]\n" % (user, self.id))
            self.lock.notifyAll()

    def drop(self, user):
        with self.lock:
            while not self.working:
                self.lock.wait()
            self.user = -1
            self.working = False
            sys.stdout.write("Philosopher[%s] dropped chopstick[%s]\n" % (user, self.id))
            self.lock.notifyAll()


class Philosopher(threading.Thread):

    def __init__(self, number, left, right, servant):
        threading.Thread.__init__(self)
        self.number = number
        self.left = left
        self.right = right
        self.servant = servant

    def run(self):
        for i in range(3):
            self.servant.down()
            time.sleep(0.1)
            self.left.grab(self.number)
            time.sleep(0.1)
            self.right.grab(self.number)
            time.sleep(0.1)
            self.right.drop(self.number)
            self.left.drop(self.number)
            self.servant.up()
        sys.stdout.write("Philosopher[%s] finished thinking and eating\n" % self.number)


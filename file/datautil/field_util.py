import uuid
import random

def get_uuid():
    return uuid.uuid1()

class int_increaser():
    base = 0
    def _get_increase_int(self):
        self.base += 1
        return self.base

_increaser = int_increaser()


def get_increase_int():
    return _increaser._get_increase_int();

def get_random_int(a=0, b=100):
    return random.randint(a,b)


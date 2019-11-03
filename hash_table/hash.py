import math

def prime_hash(key, size):
    return key % size


def hash_const(key, size, A=(math.sqrt(5) - 1) / 2):
    return int(size * math.modf(key * A)[0])

def func(A=(math.sqrt(5) - 1) / 2):
    def inner(key, size):
        return int(size * math.modf(key * A)[0])
    return inner

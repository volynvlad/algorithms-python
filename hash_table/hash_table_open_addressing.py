from collections import deque
import numpy as np

import bucket
from bucket import Bucket
import hash
from hash import prime_hash, double_hash

class OpenAddressingHashTable:
    def __init__(self, size=71, hash_function=None):
        self.count = 0
        self.size = size
        self.hash_function = hash_function or prime_hash
        self.table = [None] * self.size

    def set(self, key, value):
        if self.size == self.count:
            self._reinit()
        self._set(key, value)

    def _set(self, key, value):
        index = self.find_place(key)
        self.table[index] = Bucket(key, value)
        self.count += 1

    def get(self, key):
        index = self.find_place(key)
        if index is None:
            return None
        return self.table[index]

    def _reinit(self):
        self.size *= 2
        old_table = self.table
        self.table = [None] * self.size
        self.size = 0
        for bucket in old_table:
            self._set(bucket.key, bucket.value)

    def _hash(self, key, i=0):
        return double_hash(key, self.size, self.hash_function, prime_hash, i)

    def find_place(self, key):
        for i in range(self.size):
            index = self._hash(key, i)
            if self.table[index] is None or self.table[index].key == key:
                return index
        return None

    
from collections import deque
import numpy as np

import bucket
from bucket import Bucket
import hash
from hash import prime_hash

class ChainsHashTable:

    def __init__(self, size=71, hash_function=None):
        self.count = 0
        self.size = size
        self.hash_function = hash_function or prime_hash
        self.table = [None] * self.size

    def set(self, key, value):
        index = self.hash_function(key, self.size)
        table = self.table[index]

        if table is None:
            self.table[index] = deque()
            self.table[index].append(Bucket(key, value))
            self.count += 1
        else:
            search_bucket = None
            for bucket in table:
                if bucket.key == key:
                    search_bucket = bucket

            if search_bucket is not None:
                search_bucket.value = value
            else:
                table.append(Bucket(key, value))



    def get(self, key):

        index = self.hash_function(key, self.size)
        table = self.table[index]

        for bucket in table:
            if bucket.key == key:
                return bucket
        return None

    def load_factor(self):
        return float(self.count) / self.size


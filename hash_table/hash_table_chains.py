"""
На множестве ключей U |u|=10^k, k={4,5,6,7,........}
1) подобрать такое число m - простое, A -константа т что
при n экспериментах на случайных U
а) h(k) = k % m
b) h(k) = [m{kA}] - высчитать среднюю длину цепочек и медианную длину цепочек
а также реализовать хеширование и разрешение коллизии:
цепочки, открытая адрессация, двойное хеширование
сравнить с константой кнута (к5-1)/2
"""

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
        self.table = [deque() for _ in range(self.size)]

    def set(self, key, value):
        index = self.hash_function(key, self.size)
        table = self.table[index]
        
        search_bucket = None
        for bucket in table:
            if bucket.key == key:
                search_bucket = bucket
        
        if search_bucket is not None:
            search_bucket.value = value
        else:
            table.append(Bucket(key, value))
            self.count += 1

    def get(self, key):

        index = self.hash_function(key, self.size)
        table = self.table[index]
        
        for bucket in table:
            if bucket.key == key:
                return bucket
        
        return None


    def load_factor(self):
        return float(self.count) / self.size


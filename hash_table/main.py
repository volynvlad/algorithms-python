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


import math
import random

import bucket
from bucket import Bucket
import hash_table_chains
from hash_table_chains import ChainsHashTable
import hash_table_open_addressing
from hash_table_open_addressing import OpenAddressingHashTable
import hash


size = 10 ** 5
random_range = 5 * size


def get_metrics(hash_function):
    table = ChainsHashTable(size, hash_function)
    for _ in range(size):
        random_key = random.randint(1, random_range)
        table.set(random_key, random.randint(0, random_range))
    return {"average chain length": get_average_chain_length(table), "medium chain length": get_medium_chain_length(table)}


def get_average_chain_length(table):
    table = table.table
    elements = 0
    count = 0
    for bucket in table:
        elements += len(bucket)
        if len(bucket) > 0:
            count += 1
    return elements / count


def get_medium_chain_length(table):
    tables = table.table
    tables.sort(key=lambda bucket: len(bucket))
    return len(tables[len(tables) // 2])

if __name__ == "__main__":

    hashes = [
        {"description": "key % size", "function": hash.prime_hash},
        # root of x^2 - a * x - 1 = 0
        {"description": "[size * {key * (sqrt(5) - 1 ) / 2}]", "function": hash.func()},
        {"description": "[size * {key * (sqrt(8) - 2 ) / 2}]", "function": hash.func(A=(math.sqrt(8) - 2) / 2)},
        {"description": "[size * {key * (sqrt(13) - 3 ) / 2}]", "function": hash.func(A=(math.sqrt(13) - 3) / 2)},
        {"description": "[size * {key * (sqrt(20) - 4 ) / 2}]", "function": hash.func(A=(math.sqrt(20) - 4) / 2)},
        {"description": "[size * {key * (sqrt(29) - 5 ) / 2}]", "function": hash.func(A=(math.sqrt(29) - 5) / 2)},
        {"description": "[size * {key * (sqrt(40) - 6 ) / 2}]", "function": hash.func(A=(math.sqrt(40) - 6) / 2)},
        {"description": "[size * {key * (sqrt(53) - 7 ) / 2}]", "function": hash.func(A=(math.sqrt(53) - 7) / 2)},
        # root of x^2 - a * x + 1 = 0
        {"description": "[size * {key * (3 - sqrt(5) ) / 2}]", "function": hash.func(A=(3 - math.sqrt(5)) / 2) },
        {"description": "[size * {key * (4 - sqrt(12) ) / 2}]", "function": hash.func(A=(4 - math.sqrt(12)) / 2) },
        {"description": "[size * {key * (5 - sqrt(21) ) / 2}]", "function": hash.func(A=(5 - math.sqrt(21)) / 2) },
        {"description": "[size * {key * (6 - sqrt(32) ) / 2}]", "function": hash.func(A=(6 - math.sqrt(32)) / 2) },
        {"description": "[size * {key * (7 - sqrt(45) ) / 2}]", "function": hash.func(A=(7 - math.sqrt(45)) / 2) },
        {"description": "[size * {key * (8 - sqrt(60) ) / 2}]", "function": hash.func(A=(8 - math.sqrt(60)) / 2) },
        {"description": "[size * {key * (9 - sqrt(77) ) / 2}]", "function": hash.func(A=(9 - math.sqrt(77)) / 2) },
    ]

    for hash in hashes:
        print(hash["description"].ljust(36, ), end=" ")
        print(get_metrics(hash["function"]))

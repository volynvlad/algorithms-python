from collections import deque
import math
import random

import bucket
from bucket import Bucket
import hash_table_chains
from hash_table_chains import ChainsHashTable
import hash


size = 10 ** 4
random_range = 5 * 10 ** 4


def get_metrics(hash_fn):
    table = ChainsHashTable(size, hash_fn)
    for i in range(size):
        random_key = random.randint(1, random_range)
        table.set(random_key, random.randint(0, random_range))
    return {'average-chain-length': get_average_chain_length(table), 'medium-chain-length': get_medium_chain_length(table)}


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
        {"description": "[size * {key * (sqrt(5) - 1 ) / 2}]", "function": hash.func()},
        {"description": "[size * {key * (sqrt(3) - 1 ) / 2}]", "function": hash.func(A=(math.sqrt(3) - 1) / 2) },
        {"description": "[size * {key * (7 - sqrt(45) ) / 2}]", "function": hash.func(A=(7 - math.sqrt(45)) / 2) },
        {"description": "[size * {key * (7 - sqrt(48) ) / 2}]", "function": hash.func(A=(7 - math.sqrt(48)) / 2) }
    ]

    for hash in hashes:
        print(hash["description"])
        print(get_metrics(hash["function"]))

import bucket
from bucket import Bucket
from collections import deque
import hash_table_chains
from hash_table_chains import ChainsHashTable
from hash import hash_const

if __name__ == "__main__":
    
    table = ChainsHashTable(hash_function=hash_const)

    table.set(3, 1)
    table.set(5, 2)
    table.set(table.size*2 + 3, 3)
    table.set(table.size + 3, 4)

    """print(table.get(3)[0].value == 5)
    print(table.get(5)[0].value == 6)
    print(table.get(table.size*2 + 3)[1].value == 7)
    print(table.get(table.size + 3)[2][2].value == 8)"""

    print(table.get(3))
    print(table.get(5))
    print(table.get(table.size*2 + 3))
    print(table.get(table.size + 3))

    print(type(table.get(table.size + 3).value))

    print("-------------------")

    for count, x in enumerate(table.table):
        if len(x) != 0:
            print("index - {} | {}".format(count, x[0]))
            print("{}".format(x[0].value))

    

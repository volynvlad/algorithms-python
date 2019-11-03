import hash_table
from hash_table import ChainsHashTable
from hash import hash_const, func
import math

def test_add():
    table = ChainsHashTable(size=29)    

    table.set(3, 5)
    table.set(5, 6)
    table.set(table.size*2 + 3, 7)
    table.set(table.size + 3, 8)
    
    assert table.table[table.hash_function(3, table.size)][0].value == 5
    assert table.table[table.hash_function(5, table.size)][0].value == 6
    assert table.table[table.hash_function(3, table.size)][1].value == 7
    assert table.table[table.hash_function(3, table.size)][2].value == 8

def test_get():
    table = ChainsHashTable()

    print(table.__getattribute__('hash_function'))

    table.set(3, 5)
    table.set(5, 6)
    table.set(table.size*2 + 3, 7)
    table.set(table.size + 3, 8)

    assert table.get(3).value == 5
    assert table.get(5).value == 6
    assert table.get(table.size*2 + 3).value == 7
    assert table.get(table.size + 3).value == 8

    table = ChainsHashTable(hash_function=func())

    print(table.__getattribute__('hash_function'))

    table.set(3, 5)
    table.set(5, 6)
    table.set(table.size*2 + 3, 7)
    table.set(table.size + 3, 8)

    assert table.get(3).value == 5
    assert table.get(5).value == 6 
    assert table.get(table.size*2 + 3).value == 7
    assert table.get(table.size + 3).value == 8

    A = (7 - math.sqrt(45)) / 2
    table = ChainsHashTable(hash_function=func(A=A))

    print(table.__getattribute__('hash_function'))

    table.set(3, 5)
    table.set(5, 6)
    table.set(table.size*2 + 3, 7)
    table.set(table.size + 3, 8)

    assert table.get(3).value == 5
    assert table.get(5).value == 6
    assert table.get(table.size*2 + 3).value == 7
    assert table.get(table.size + 3).value == 8

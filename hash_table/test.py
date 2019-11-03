import hash_table_chains
import hash_table_open_addressing
from hash_table_chains import ChainsHashTable
from hash_table_open_addressing import OpenAddressingHashTable
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

    table = OpenAddressingHashTable(size=29)   

    table.set(3, 5)
    table.set(5, 6)
    table.set(9, 7)
    table.set(11, 8)

    print(table.table[table.hash_function(table.size*2 + 3, table.size)])
    
    assert table.table[table.hash_function(3, table.size)].value == 5
    assert table.table[table.hash_function(5, table.size)].value == 6
    assert table.table[table.hash_function(9, table.size)].value == 7
    assert table.table[table.hash_function(11, table.size)].value == 8

def test_get():
    table = ChainsHashTable()

    table.set(3, 5)
    table.set(5, 6)
    table.set(table.size*2 + 3, 7)
    table.set(table.size + 3, 8)

    assert table.get(3).value == 5
    assert table.get(5).value == 6
    assert table.get(table.size*2 + 3).value == 7
    assert table.get(table.size + 3).value == 8

    table = ChainsHashTable(hash_function=func())

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

    table.set(3, 5)
    table.set(5, 6)
    table.set(table.size*2 + 3, 7)
    table.set(table.size + 3, 8)

    assert table.get(3).value == 5
    assert table.get(5).value == 6
    assert table.get(table.size*2 + 3).value == 7
    assert table.get(table.size + 3).value == 8


    table = OpenAddressingHashTable()

    table.set(3, 5)
    table.set(5, 6)
    table.set(table.size*2 + 3, 7)
    table.set(table.size + 3, 8)

    assert table.get(3).value == 5
    assert table.get(5).value == 6
    assert table.get(table.size*2 + 3).value == 7
    assert table.get(table.size + 3).value == 8

    table = ChainsHashTable(hash_function=func())

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

    table.set(3, 5)
    table.set(5, 6)
    table.set(table.size*2 + 3, 7)
    table.set(table.size + 3, 8)

    assert table.get(3).value == 5
    assert table.get(5).value == 6
    assert table.get(table.size*2 + 3).value == 7
    assert table.get(table.size + 3).value == 8

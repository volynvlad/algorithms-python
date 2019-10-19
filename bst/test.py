from bst import num_bst_nodes
from bst import BinarySearchTree
import pytest


def test_insert():
    tree = BinarySearchTree()
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    assert tree.root.value == 2
    assert tree.root.left.value == 1
    assert tree.root.right.value == 3


def test_search():
    tree = BinarySearchTree()
    search_values = [1, 3, 5, 9, 10, 20, 22]
    tree.insert_values(search_values)

    for search_value in search_values:
        assert tree.search(search_value).value == search_value


def test_k_min():
    tree = BinarySearchTree()
    values = [15, 13, 17, 12, 14, 16, 18, 11]
    tree.insert_values(values)
    values = sorted(values)

    for i in range(len(values)):
        assert tree.k_min(i + 1) == values[i]


def test_bypass():
    tree1 = BinarySearchTree()

    assert [] == tree1.bypass(False)
    tree1.insert(2)
    assert [2] == tree1.bypass(False)
    tree1.insert(1)
    assert [1, 2] == tree1.bypass(False)
    tree1.insert(3)
    assert [1, 2, 3] == tree1.bypass(False)

    tree2 = BinarySearchTree()
    assert [] == tree2.bypass()
    tree2.insert(2)
    assert [2] == tree2.bypass()
    tree2.insert(1)
    assert [2, 1] == tree2.bypass()
    tree2.insert(3)
    assert [3, 2, 1] == tree2.bypass()


def test_parent():
    tree = BinarySearchTree()
    values = [15, 13, 17, 12, 14, 16, 18, 11]
    tree.insert_values(values)
    print(tree.__str__())
    assert tree.__parent__(15) is None
    assert 15 == tree.__parent__(13).value
    assert 13 == tree.__parent__(12).value
    assert 12 == tree.__parent__(11).value
    assert 17 == tree.__parent__(18).value


def test_num():
    tree = BinarySearchTree()
    values = [15, 13, 17, 12, 14, 16, 18, 11]
    tree.insert_values(values)
    print(tree.__str__())
    assert num_bst_nodes(tree.root) == values.__len__()


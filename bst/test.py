from bst.bst import BinarySearchTree
from bst.bst import count_bst_nodes


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
    assert tree.get_parent(15) is None
    assert 15 == tree.get_parent(13).value
    assert 13 == tree.get_parent(12).value
    assert 12 == tree.get_parent(11).value
    assert 17 == tree.get_parent(18).value


def test_num():
    tree = BinarySearchTree()
    values = [15, 13, 17, 12, 14, 16, 18, 11]
    tree.insert_values(values)
    assert count_bst_nodes(tree.root) == values.__len__()


def test_is_balanced():
    tree = BinarySearchTree()
    values = [15, 13, 17, 12, 14, 16, 18, 11]
    tree.insert_values(values)
    assert tree.is_balanced()


def test_balance():
    tree = BinarySearchTree()
    tree.insert_values(range(11, 19))
    tree.balance()
    assert tree.is_balanced()

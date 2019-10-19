from bst import BinarySearchTree

tree = BinarySearchTree()
values = [15, 13, 17, 12, 14, 16, 18, 11]

tree.insert_values(values)
print(str(tree))
print(tree.bypass())
print(tree.bypass(False))
tree.left_rotation(15)
print(str(tree))
tree.right_rotation(17)
print(str(tree))
print('-' * 30)
tree = BinarySearchTree()
tree.insert_values([8, 7, 9, 10])
print(tree)
tree.place_in_root(9, tree.root)
print(tree)
tree.place_in_root(7, tree.root.left)
print(tree)

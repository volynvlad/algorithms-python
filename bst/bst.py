import functools


# disallows calling a function with the same arguments
def memoize(f):
    cache = {}

    @functools.wraps(f)
    def inner(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    inner.__cache__ = cache
    return inner


@memoize
def num_bst_nodes(node):
    if node is None:
        return 0
    return num_bst_nodes(node.left) + num_bst_nodes(node.right) + 1


class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.bf = 0

        def __str__(self):
            return "[value={}, left={}, right={}]\n".format(self.value, None if not self.left else self.left.value,
                                                            None if not self.right else self.right.value)

        def has_direct_child(self, node):
            return self.left == node or self.right == node

        def has_no_child(self):
            return self.left is None and self.right is None

    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root is None:
            return "Empty tree"
        result = ""
        nodes = [self.root]
        while len(nodes) > 0:
            current_node = nodes.pop(0)
            if current_node is not None:
                result += str(current_node)
                nodes.extend([current_node.left, current_node.right])
        return result

    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
            return

        def insert_helper(node):
            if value == node.value:
                pass
            elif value < node.value:
                if node.left is None:
                    #  print(node.value)
                    node.left = self.Node(value)
                else:
                    #  print(node.value)
                    insert_helper(node.left)
            else:
                if node.right is None:
                    node.right = self.Node(value)
                else:
                    insert_helper(node.right)
        insert_helper(self.root)

    def insert_values(self, values):
        for value in values:
            self.insert(value)

    def search(self, value):

        def search_helper(node):
            if node is None or node.value == value:
                return node
            elif node.value > value:
                return search_helper(node.left)
            else:
                return search_helper(node.right)

        return search_helper(self.root)

    def k_min(self, k_index):
        current = self.root
        count = k_index

        while current is not None:
            size_of_left_subtree = num_bst_nodes(current.left)
            if size_of_left_subtree + 1 == count:
                return current.value
            elif size_of_left_subtree < count:
                current = current.right
                count -= size_of_left_subtree + 1
            else:
                current = current.left

    def bypass(self, post_order=True):
        if self.root is None:
            return []

        def bypass_helper(node):
            result = []
            if node is None:
                return result
            if post_order:
                result += bypass_helper(node.right)
                result.append(node.value)
                result += bypass_helper(node.left)
            else:
                result += bypass_helper(node.left)
                result.append(node.value)
                result += bypass_helper(node.right)

            return result
        return bypass_helper(self.root)

    def height(self):

        def height_helper(node):
            if node is None:
                return 0
            return 1 + max(height_helper(node.left), height_helper(node.right))

        return height_helper(self.root)

    def get_parent(self, value):  # return parent, node
        parent, node = None, self.root

        while True:
            if node is None and node.value == value:
                return None

            if node.value == value:
                return parent
            parent, node = (node, node.left) if value < node.value else (node, node.right)

    def left_rotation(self, node_value):
        parent_node = self.get_parent(node_value)
        node = self.search(node_value)
        print("parent_node: ", parent_node)
        print("node: ", node)

        if node is None or node.left is None:
            return None

        tmp_node = node.left
        node.left = parent_node
        parent_node.right = tmp_node

        if parent_node == self.root:
            self.root = node

        return node

    def right_rotation(self, node_value):
        parent_node = self.get_parent(node_value)
        node = self.search(node_value)

        if node is None or node.right is None:
            return None

        tmp_node = node.right
        node.right = parent_node
        parent_node.left = tmp_node

        if parent_node == self.root:
            self.root = node

        return node

    def place_in_root(self, node_value, root: Node):
        if root is None or root.has_no_child():
            return
        parent = self.get_parent(node_value)
        node = self.search(node_value)
        while node is not None and not node.has_direct_child(root):
            rotate = self.right_rotation if node.value < parent.value else self.left_rotation
            node = rotate(parent.value)
            parent = self.get_parent(node.value)
            node = self.search(node.value)
        return node

    def balance(self):
        pass


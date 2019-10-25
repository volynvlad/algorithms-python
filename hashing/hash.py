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

import numpy as np

class Hash:

    class ChainList:

        """
        Class ChainList implements a singly-linked list 
        to Store Node((key, object reference))
        """

        class Node:
            """
            Class Node represents a node in a singly-linked list 
            that will store a (key, object) tuple and a next pointer
            """
            def __init__(self, value):
                self.value = value
                self.next = None

            def __str__(self):
                return "Node[value: {}, next: {}]".format(self.value, self.next)
        
        def __init__(self):
            self.head = None
            self.length = 0
        
        def set(self, pair) -> bool:
            """
            set returns True if a New node was added
                        False if an old node's value changed
            """
            if not self.head:
                self.head = self.Node(pair)
                self.head.next = None
                self.length += 1
                return True
            else:
                curr = self.head
                while curr is not None:
                    if curr.value[0] == pair[0]:
                        curr.value = (curr.value[0], pair[1])
                        return False
                    curr = curr.next
                old_head = self.head
                self.head = self.Node(pair)
                self.head.next = old_head
                self.length += 1
                return True

        def get(self, key) -> self.Node:
            """
            get returns the Node by key
            None if there is no Node with this key
            """
            curr = self.head
            while curr is not None:
                if curr.value[0] == key:
                    return curr.value[1]
                curr = curr.next
            return None
        
        def remove(self, key) -> self.Node:
            """
            remove the Node by key and 
            return this Node
            return None if there is no Node with this key
            """
            curr = self.head
            while curr is not None:
                if curr.value[0] == key:
                    # check to see if this really works
                    to_return = curr.value[1]
                    curr.value = curr.next.value
                    curr.next = curr.next.next
                    self.length -= 1
                    return to_return
                curr = curr.next
            return None
        
        def contains(self, key) -> bool:
            """
            Returns true if the list contains the key, false otherwise
            """
            curr = self.head
            while curr is not None:
                if curr.value[0] == key:
                    return True
                curr = curr.next
            return False

    def __init__(self, size):
        self.table = [self.ChainList() for _ in range(0, size)]
        self.size = size
        self.count = 0
    
    def set(self, key, value, s_fun=True) -> bool:
        """
        set returns True if there is a node with this key or 
        """
        s_list = self.simple_func(key) if s_fun else self.func(key)
        if self.table[s_list].contains(key):
            self.table[s_list].set((key, value))
            return True
        else:
            if self.count == self.size:
                return False
            else:
                self.table[s_list].set((key, value))
                self.count += 1
                return True
        
    def get(self, key, s_fun=True):
        s_list = self.simple_func(key) if s_fun else self.func(key)
        return self.table[s_list].get(key)
    
    def delete(self, key, s_fun=True):
        s_list = self.simple_func(key) if s_fun else self.func(key)
        return self.table[s_list].remove(key)

    def load(self):
        return float(self.count) / self.size

    def simple_func(self, key):
        return key % self.size

    def func(self, key, A=(7 - np.sqrt(48)) / 2):
        return int(key * A) * self.size

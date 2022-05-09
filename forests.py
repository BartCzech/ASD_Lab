import math

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Node(data)

    def search(self, value):
        if self.data == value:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else: 
                return False
        elif value > self.data:
            if self.right:
                return self.right.search(value)
            else: 
                return False

    def maximum(self):
        if not self.right:
            return self.data
        else:
            return self.right.maximum()

    def minimum(self):
        if not self.left:
            return self.data
        else:
            return self.left.minimum()

class Tree:
    def __init__(self, element):
        self.root = Node(element)

    def insert(self, num):
        self.root.add_child(num)

    def default_print(self, node = None, prefix = '', dashes = '', right = False, indent = '   '):
        if node == None:
            node = self.root
            if not node.left and not node.right:
                return
        if right == True:
            print(indent + prefix + str(node.data), end = '' if node.left else "\n") #add count-prefix on the start
            indent += indent + ' '
        elif right == False:
            print(prefix + str(node.data), end = '' if node.left else "\n")

        prefix += '-'

        if node.left:
            self.default_print(node.left, prefix, dashes, False, indent)
        if node.right:
            self.default_print(node.right, prefix, dashes, True, indent)

        return

    def pretty_print(self, node = None, prefix = '', is_left = True):
        if node == None:
            node = self.root
            if not node.left and not node.right:
                return
        if node.right != None:
            new_prefix = '|   ' if is_left == True else '    '
            self.pretty_print(node.right, prefix + new_prefix, False)

        if is_left == True:
            print(prefix + '└── ' + str(node.data))
        else:
            print(prefix + '┌── ' + str(node.data))

        if node.left != None:
            new_prefix = '    ' if is_left == True else '│   '
            self.pretty_print(node.left,  prefix + new_prefix, True)
        return

    def search_for(self, value):
        print(self.root.search(value))

    def maximum(self):
        print(self.root.maximum())

    def minimum(self):
        print(self.root.minimum())

class Forest:
    def __init__(self, size):
        self.trees_array = size*[0.5]
        for i in range(0, size):
            self.trees_array[i] = Tree(0.5 + i)

    def default_trees_print(self):
        for i in range(0, len(self.trees_array)):
            self.trees_array[i].default_print()

    def pretty_trees(self):
        for i in range(1, len(self.trees_array) + 1):
            self.trees_array[len(self.trees_array) - i].pretty_print()
    
    def insert_base(self, elements):
        for i in range(0, len(elements)):
            index = math.floor(elements[i])
            self.trees_array[index].insert(elements[i])

    def insert(self, value):
        index = math.floor(value)
        self.trees_array[index].insert(value)        

    def maximum(self, index):
        return self.trees_array[index].maximum()

    def minimum(self, index):
        return self.trees_array[index].minimum()

    def search(self, value):
        index = math.floor(value)
        self.trees_array[index].search_for(value)

sherwood = Forest(10)

numbers = [1.3, 1.6, 3.7, 4.0, 4.99, 7.3, 7.8, 7.7, 7.9, 7.6, 9.3]
sherwood.insert_base(numbers)
sherwood.pretty_trees()
sherwood.default_trees_print()
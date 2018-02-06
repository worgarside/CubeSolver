from cube.cube_class import SOLVED_POS

DEFAULT_HEAD = 0, SOLVED_POS , '-', False

class Node:
    def __init__(self, id, data, parent_move, leaf = False):
        self.parent = None
        self.child = None
        self.id = id
        self.data = data
        self.parent_move = parent_move
        self.leaf = leaf

    def __str__(self):
        return str(self.id) + ', ' + self.data

class LinkedList:
    def __init__(self):
        self.head = Node(*DEFAULT_HEAD)

    def push(self, id, data, parent_move, leaf = False):
        node = Node(id, data, parent_move, leaf)
        if self.head == None:
            self.head = node
        else:
            node.parent = self.head
            node.parent.child = node
            self.head = node

    def __str__(self):
        output = ""
        curr_node = self.head
        if curr_node != None:
            while curr_node.parent != None:
                output += str(curr_node.id) + ', ' + curr_node.data + ', ' + str(curr_node.parent_move) + ', ' + str(curr_node.leaf) + "\n"
                curr_node = curr_node.parent
            output += str(curr_node.id) + ', ' + curr_node.data + ', ' + str(curr_node.parent_move) + ', ' + str(curr_node.leaf)
        return output
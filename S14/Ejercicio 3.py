class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left    
        self.right = right  


class BinaryTree:

    def __init__(self, root_value=None):
        if root_value is None:
            self.root = None
        else:
            self.root = Node(root_value)


    def insert_left(self, parent: Node, value):
        if parent.left is None:
            parent.left = Node(value)
        else:
            new_node = Node(value, left=parent.left)
            parent.left = new_node

    def insert_right(self, parent: Node, value):
        if parent.right is None:
            parent.right = Node(value)
        else:
            new_node = Node(value, right=parent.right)
            parent.right = new_node

    def _print_recursive(self, node):
        if node is None:
            return

        self._print_recursive(node.left)
        print(node.value)
        self._print_recursive(node.right)


    def print_tree(self):
        if self.root is None:
            print("Árbol vacío")
        else:
            self._print_recursive(self.root)


first_binary = BinaryTree("AA")


first_binary.insert_right (first_binary.root,20)
first_binary.insert_left (first_binary.root,20)
first_binary.insert_right(first_binary.root.left,40)
first_binary.insert_left (first_binary.root.right,50)
first_binary.insert_right(first_binary.root.right, 200)
first_binary.insert_left(first_binary.root.left, 250)

first_binary.print_tree()

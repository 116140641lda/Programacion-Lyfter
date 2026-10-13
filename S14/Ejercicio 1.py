class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next



class Stack:
    head: Node

    def __init__(self, first_value=None):

        if first_value is None:
            self.last = None
        else:
            self.last = Node(first_value)

    def print_structure(self):

        current_node = self.last
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
            

    def push (self,data):

            new_node = Node(data)
            new_node.next = self.last
            self.last = new_node

    
    def pop (self,remove_node):
        
        if self.last is not None:
            remove_node = self.last
            self.last = remove_node.next
            remove_node.next = None
            
            return remove_node.data
        else:
            print("No hay mas datos en la pila")
        

first_stack = Stack()
second_stack = Stack()

first_stack.push(50)
first_stack.push(30)
first_stack.push(50)

second_stack.push(100)
second_stack.push(200)
second_stack.push(300)

first_stack.print_structure()
second_stack.print_structure()

print( "Pop 1:",first_stack.pop(""))
print("Pop 1:", first_stack.pop(""))
print("Pop 1:", first_stack.pop(""))
print("Pop 1:", first_stack.pop(""))


print("Pop 2:", second_stack.pop(""))
print("Pop 2:", second_stack.pop(""))


first_stack.print_structure()
second_stack.print_structure()






                
                    



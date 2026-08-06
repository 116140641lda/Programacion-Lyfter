class Node:
    data: str

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev



class DoubleEndedQueue:

    def __init__(self):

        self.last = None
        self.head = None

    def print_structure(self):

        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
            

    def push_right (self,data):

            new_node = Node(data)
            if self.last is None: 
                self.head = self.last = new_node
            else:
                self.last.next = new_node
                new_node.prev = self.last
                self.last = new_node

    def push_left (self,data):

        new_node = Node(data)
        if self.head is None: 
            self.head = self.last = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_right (self):
        
        data = self.last.data
        if self.last.prev is None:
            self.head = self.last = None
        else:
            self.last = self.last.prev
            self.last.next = None

        return data



    def pop_left (self):
        
        data = self.head.data
        if self.head.next is None:
            self.head = self.last = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return data


first_double_ended_queue = DoubleEndedQueue()
second_double_ended_queue = DoubleEndedQueue()


first_double_ended_queue.push_right("SH")
first_double_ended_queue.push_left("SK")

first_double_ended_queue.print_structure()

first_double_ended_queue.pop_right()

second_double_ended_queue.push_left("JH")
second_double_ended_queue.push_left("LL")

second_double_ended_queue.print_structure()

second_double_ended_queue.pop_left()




first_double_ended_queue.print_structure()
second_double_ended_queue.print_structure()
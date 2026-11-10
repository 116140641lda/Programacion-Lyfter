class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



def bubble_sort (head):

    if head is None:
        return head

    switch = True

    while switch:
        switch = False
        actual = head

        while actual.next is not None:
            if actual.data > actual.next.data :
                actual.data, actual.next.data = actual.next.data, actual.data
                switch = True
            actual = actual.next
    return head




node_4 = Node(-50)
node_3 = Node(10,node_4)
node_2 = Node(-15,node_3)
head = Node(4,node_2)


bubble_sort(head)

actual = head
while actual:
        print(actual.data)
        actual = actual.next

    
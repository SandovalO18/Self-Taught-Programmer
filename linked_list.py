import random

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

    def print_node(self):
        print(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self,data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end = " ")
            node = node.next
        print("\n")

    def search(self,target):
        current = self.head
        while current != None:
            if current.data == target:
                print("Found it!")
                return True
            else:
                current = current.next
        print("Not found!")
        return False


the_list = LinkedList()
the_list.append_node("Tuesday")
the_list.append_node("Wednesday")
#the_list.print_list()

for j in range(0,20):
    j = random.randint(1,30)
    the_list.append_node(j)
the_list.print_list()
the_list.search(10)
        
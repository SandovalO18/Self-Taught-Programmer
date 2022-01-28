class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()

for c in "Hello":
    stack.push(c)
reversed_string = ""
for i in range(len(stack.items)):
    reversed_string += stack.pop()
print(reversed_string)

list1 = [1, 2, 3, 4, 5]
list2 = []

stack = Stack()
for item in list1:
    stack.push(item)


for i in range(len(stack.items)):
    list2.append(stack.pop())

print(list2)
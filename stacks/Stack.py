class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items

    def reverse_string(self, stack, input_str):
        for i in range(len(input_str)):
            stack.push(input_str[i])

        rev_str = ""
        while not stack.is_empty():
            rev_str += stack.pop()

        return rev_str





stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.get_stack())
# print(stack.pop())
# print(stack.get_stack())
# print(stack.peek())
# print(stack.is_empty())
# stack.pop()
# stack.pop()
# print(stack.get_stack())
# print(stack.is_empty())

input_string = "Hello"
# One liner to reverse the string
# print(input_string[::-1])
print(stack.reverse_string(stack, input_string))
class Stack:
    def __init__(self, stack: list) -> list:
        self.stack = stack

    def push(self, new):
        self.stack.append(new)
    
    def pop(self):
        return self.stack.pop()

    def __str__(self) -> str:
        return str(self.stack)


s1 = Stack([34])
s1.push(["qwerty"])
s1.push(["Aziz"])
print(s1.pop())
print(s1.pop())
print(s1)

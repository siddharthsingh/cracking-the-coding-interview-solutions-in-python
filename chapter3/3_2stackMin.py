class Stack():
    def __init__(self):
        self.stack = []
        self.min = [999999999]

    def push(self,val):
        self.stack.append(val)
        if val<=self.min[-1]:
            self.min.append(val)

    def pop(self):
        if not self.stack:raise  Exception("Empty Stack")
        if self.stack[-1]==self.min[-1]:
            self.min.pop()
        return self.stack.pop()

    def ret_min(self):
        return self.min[-1]

a = Stack()

a.push(5)
a.push(3)
a.push(1)
a.push(10)
print(a.stack)
print(a.ret_min())
a.push(0)
a.push(5)
print(a.ret_min())


a.pop()
a.pop()
print(a.ret_min())
a.pop()
a.pop()
print(a.ret_min())





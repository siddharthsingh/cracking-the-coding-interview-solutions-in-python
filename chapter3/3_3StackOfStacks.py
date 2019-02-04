class StackOfStacks():
    def __init__(self,limit):
        if limit < 1:
            raise Exception("limit cannot be less than 1")
        self.limit = limit
        self.stack_of_stack = [[]]

    def push(self, val):
        if len(self.stack_of_stack[-1]) == self.limit:
            self.stack_of_stack.append([])
        self.stack_of_stack[-1].append(val)

    def pop(self):
        val = self.stack_of_stack[-1].pop()
        if not self.stack_of_stack[-1]:
            self.stack_of_stack.pop()
        return val

    def pop_at(self,index):

        stack_number = index//self.limit
        pos = index-stack_number*self.limit
        val = self.stack_of_stack[stack_number][pos]
        for s in range(stack_number,len(self.stack_of_stack)):
            limit_=len(self.stack_of_stack[s])
            for i in range(pos, limit_):
                if i == self.limit-1 and s<len(self.stack_of_stack)-1:
                    next_ = self.stack_of_stack[s+1][0]
                elif i < limit_-1:
                    next_ = self.stack_of_stack[s][i+1]
                else:
                    return val
                self.stack_of_stack[s][i] =  next_




a = StackOfStacks(2)

a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
print(a.stack_of_stack)
print(a.pop_at(3))
print(a.pop())
print(a.stack_of_stack)

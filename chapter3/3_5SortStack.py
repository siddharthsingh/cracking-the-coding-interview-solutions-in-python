class SortStack():
    def __init__(self):
        self.stack = []

    def sort(self):
        new_list = [self.stack[0]]

        for element in self.stack[1:]:
            pos = len(new_list)-2
            if element>new_list[-1]:
                new_list.append(element)
            else:
                new_list.append(new_list[-1])
            while pos >= 0 and element < new_list[pos]:
                new_list[pos+1] = new_list[pos]
                pos -= 1
            new_list[pos+1] = element
        self.stack = new_list

    def pop(self):
        if not self.stack:
            raise Exception("Stack Empty")
        return self.stack.pop()

    def push(self,val):
        self.stack.append(val)

    def peek(self):
        if not self.stack:
            raise Exception("Stack Empty")
        return self.stack[-1]

stack = SortStack()
for x in [4,5,2,4,52,1,4,5,1,7,4]:
    stack.push(x)

print(stack.stack)
stack.sort()
print(stack.stack)

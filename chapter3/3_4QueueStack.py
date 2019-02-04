class MyQueue():
    def __init__(self):
        self.stack = [[],[]]
        self.push_to = 0
        self.pop_from = 1

    def queue(self,val):
        self.stack[self.push_to].append(val)

    def dequeue(self):
        if self.stack[self.pop_from]:
            return self.stack[self.pop_from].pop()
        if not self.stack[self.push_to]:
            raise Exception("Empty Queue")
        self.stack[self.pop_from] = list(reversed(self.stack[self.push_to]))
        self.stack[self.push_to] = []
        return self.stack[self.pop_from].pop()

q = MyQueue()
q.queue(1)
q.queue(2)
q.queue(3)
q.queue(4)
print(q.stack)
print(q.dequeue())
print(q.dequeue())
q.queue(5)
q.queue(6)
print(q.stack)

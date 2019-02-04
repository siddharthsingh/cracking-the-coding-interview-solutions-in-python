class Node():
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None


class shelter():

    def __init__(self):
        self.queue = None

    def enqueue(self,animal):
        if not animal or animal not in ('cat','dog'):
            raise Exception("Animal not supported")

        node = Node(animal)

        if not self.queue:
            self.queue = node
        else:
            self.queue.next = node
            node.prev = self.queue
            self.queue = node

    def dequeue(self):
        if not self.queue:
            raise Exception("Empty queue")
        animal = self.queue.name
        if self.queue.prev:
            self.queue = self.queue.prev
            self.queue.next = None
        else:
            self.queue = None

        return animal

    def dequeue_animal(self,animal):
        if not self.queue:
            raise Exception("Empty queue")
        if self.queue.name == animal:
            if self.queue.prev:
                self.queue = self.queue.prev
                self.queue.next = None
            else:
                self.queue = None
            return animal
        temp = self.queue
        while temp:
            if temp.name == animal:
                if temp.prev:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                else:
                    temp.next.prev = None
                return animal
            temp = temp.prev
        return "no "+animal+" in shelter"

    def print_queue(self):
        temp = self.queue
        while temp:
            print(temp.name,end=", ")
            temp = temp.prev
        print("")

sh = shelter()
sh.enqueue('cat')
sh.enqueue('cat')
sh.enqueue('dog')
sh.enqueue('dog')
sh.enqueue('cat')
sh.enqueue('dog')
sh.enqueue('cat')
sh.enqueue('cat')
sh.print_queue()
print(sh.dequeue())
sh.print_queue()
print(sh.dequeue_animal('cat'))
print(sh.dequeue_animal('cat'))
sh.print_queue()


class MaxHeap():
    def __init__(self):
        self.heap = []

    def __repr__(self):
        print(self.heap)
        return ",".join(map(str,self.heap))
    def __len__(self):
        return len(self.heap)

    def max(self):
        if not self.heap:
            raise Exception("Empty heap")
        return self.heap[0]

    def extract_max(self):
        if not self.heap:
            raise Exception("Empty heap")
        self.heap[0] , self.heap[-1] = self.heap[-1], self.heap[0]
        val = self.heap[-1]
        del self.heap[-1]
        self.max_heapify(0)
        return val


    def build_max_heap(self):
        if not self.heap:
            return
        for i in range(len(self.heap)//2,-1,-1):
            print(i)
            self.max_heapify(i)

    def max_heapify(self,i):
        left = 2*i+1
        right = 2*i+2
        largest = i
        if left<len(self.heap) and self.heap[i]<self.heap[left]:
            largest = left
        if right<len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if i == largest:
            return
        self.heap[largest],self.heap[i] = self.heap[i],self.heap[largest]
        self.max_heapify(largest)

    def insert(self,val):
        i = len(self.heap)
        self.heap.append(val)
        parent = (i-1)//2
        while parent>=0 and i!=0 and self.heap[i]>self.heap[parent]:
            self.heap[parent],self.heap[i] = self.heap[i],self.heap[parent]
            i = parent
            parent = (i - 1) // 2

a = MaxHeap()
a.insert(20)
a.insert(12)
a.insert(14)
a.insert(17)
a.insert(16)
a.insert(15)
print(a)

b = MaxHeap()
b.heap = [1,2,3,4,5,6,7,8]
b.build_max_heap()
print(b)
print(b.extract_max())
print(b.extract_max())
print(b.extract_max())
print(len(b))
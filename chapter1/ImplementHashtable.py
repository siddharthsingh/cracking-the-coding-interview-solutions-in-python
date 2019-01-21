class Node():
    def __init__(self):
        self.value = None
        self.key = None
        self.next = None

class HashTable():

    def __init__(self):
        self.hashList = []
        for i in range(10):
            self.hashList.append(Node())

    def store(self,key,value):
        preHash = abs(hash(key))
        index = preHash%len(self.hashList)
        temp = self.hashList[index]
        while temp.key and temp.key != key:
            temp = temp.next
        # print(index,'---')


        temp.key = key
        temp.value= value
        temp.next = Node()

    def get(self,key):
        preHash = abs(hash(key))
        index = preHash%len(self.hashList)
        temp = self.hashList[index]
        while temp.key and temp.key!=key:
            temp = temp.next
        if not temp.key:
            # print(index)
            raise KeyError
        return temp.value


ht = HashTable()

ht.store('a','aaaaa')
ht.store('b','bbbb')
ht.store('1','111')
ht.store('2',2222)
ht.store(3,3333)


print(ht.get('a'))
print(ht.get('b'))
print(ht.get('1'))
print(ht.get('2'))
print(ht.get(3))
print(ht.get('x'))

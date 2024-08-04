import ctypes


class DynamicArray:

    def __init__(self):
        self.n = 0
        self.cap = 1
        self.array = self.makeArray(self.cap)

    def reserve(self, new_cap):
        self._resize(new_cap)

    def capacity(self):
        return self.cap

    def include(self, ele):

        for i in range(self.n):
            if self.array[i] == ele:
                return True

        return False

    def emplace(self, index, item):

        if index < 0 or index > self.n:
            print('Enter An Appropriate Index')
            return

        if self.n == self.cap:
            self._resize(self.cap * 2)

        for i in range(self.n - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]

        self.array[index] = None
        self.n += 1

    def Assign(self, B):

        if self.n != B.n:
            raise ValueError('Sizes Are Not Equal')

        for i in range(self.n):
            B.array[i] = self.array[i]

    def __str__(self):
        return f'The Dynamic Array Has {[self.array[i] for i in range(self.n)]} elements'

    def insert(self, index, item):

        if index < 0 or index > self.n:
            print('Enter An Appropriate Index')
            return

        if self.n == self.cap:
            self._resize(self.cap * 2)

        for i in range(self.n - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]

        self.array[index] = item
        self.n += 1

    def pushBack(self, ele):

        if self.n == self.cap:
            self._resize(self.cap * 2)

        self.array[self.n] = ele
        self.n += 1

    def popBack(self):

        if self.n == 0:
            print('Cannot Delete The Last Element')
            return

        self.array[self.n - 1] = 0
        self.n -= 1

    def removeAt(self, index):

        if not 0 <= index < self.n:
            raise IndexError('Index Is Not Valid')

        for i in range(index, self.n - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.n] = 0
        self.n -= 1

    def clear(self):

        for i in range(self.n):
            self.array[i] = 0

        self.n = 0

    def size(self):
        return self.n

    def isEmpty(self):
        if self.n == 0:
            return True
        return False

    def __getitem__(self, key):

        if not 0 <= key < self.n:
            raise IndexError('Check Your Index Again')

        return self.array[key]

    def __setitem__(self, key, newvalue):
        if self.n == self.cap:
            self._resize(self.cap * 2)
        self.array[key] = newvalue

    def shrinkToFit(self):
        self.cap = self.n

    def _resize(self, newcap):

        B = self.makeArray(newcap)

        for i in range(self.n):
            B[i] = self.array[i]

        self.array = B
        self.cap = newcap

    def makeArray(self, newcap):

        return (newcap * ctypes.py_object)()


arr = DynamicArray()
arr.pushBack(34)
arr.pushBack(54)
arr.pushBack(32)
arr.pushBack(54)
arr.pushBack(0)

arr.insert(2, 312)
print(arr)
arr.removeAt(4)
arr.clear()
print(arr)




from DynamicArray import DynamicArray

class Queue:

    def __init__(self):
        self.array=DynamicArray(5)
    def Enqueue(self,ele):
        if self.array.n==self.array.cap:
            print('Queue Is Full')
        else:
            self.array.pushBack(ele)
    def Dequeue(self):
        for i in range(self.array.n-1):
            self.array[i]=self.array[i+1]
        self.array[self.array.n-1]=None
        self.array.n-=1
    def Peek(self):
        return self.array[0]
    def isEmpty(self):
        return self.array.n==0
    def Size(self):
        return self.array.n
    def Print(self):
        for i in range(self.array.n-1,-1,-1):
            print(self.array[i])
        print()

if __name__=='__main__':
    q=Queue()
    q.Enqueue(45)
    q.Enqueue(56)
    q.Enqueue(67)
    q.Print()
    q.Dequeue()
    q.Print()
    print(q.Peek())

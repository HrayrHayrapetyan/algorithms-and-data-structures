class Queue:

    def __init__(self):
        self.array=[0]*5
        self.front=0
        self.rear=0
        self.size=0

    def Enqueue(self,data):
        if self.size==5:
            print('Queue is Full')
            return
        self.array[self.rear]=data
        self.rear=(self.rear+1)%5
        self.size+=1

    def Dequeue(self):
        if not self.isEmpty():
            data=self.front
            self.front+=1
            self.size-=1
            return data
    def isEmpty(self):
        return self.size==0

    def Size(self):
        return self.size
    def Peek(self):
        return self.array[self.front]
    def Print(self):
        for i in range(self.size):
            print(self.array[(self.front+i)%5])
        print()

if __name__=='__main__':
    q=Queue()
    q.Enqueue(45)
    q.Enqueue(56)
    q.Enqueue(32)
    q.Enqueue(90)
    q.Print()
    q.Dequeue()
    q.Dequeue()
    q.Enqueue(45)
    q.Enqueue(0)
    q.Print()
    q.Dequeue()
    q.Dequeue()
    q.Print()
    print(q.Size())
    print(q.Peek())



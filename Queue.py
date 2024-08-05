
class Queue:
    def __init__(self):
        self.array=[]
    def Enqueue(self,item):
        self.array.append(item)
    def Dequeue(self):
        self.array.pop(0)
    def Peek(self):
        return self.array[0]
    def isEmpty(self):
        return len(self.array)==0
    def Size(self):
        return len(self.array)
    def Print(self):
        print(self.array)


if __name__=='__main__':
    q=Queue()
    q.Enqueue(45)
    q.Enqueue(56)
    q.Enqueue(67)
    q.Print()
    q.Dequeue()
    q.Print()
    print(q.Peek())
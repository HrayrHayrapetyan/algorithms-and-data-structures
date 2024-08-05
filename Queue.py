
class Queue:
    def __init__(self):
        self.array=[]
    def Enqueue(self,ele):
        self.array.append(ele)
    def Dequeue(self):
        self.array.pop()
    def Peek(self):
        return self.array[0]
    def isEmpty(self):
        return len(self.array)==0
    def Size(self):
        return len(self.array)
    def Print(self):
        for i in range(len(self.array)-1,-1,-1):
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
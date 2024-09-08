from Double_Linked import Double_Linked

class deque:

    def __init__(self):
        self.data=Double_Linked()

    def push_Front(self,value):
        self.data.push_Front(value)

    def pop_Front(self):
        self.data.pop_Front()

    def push_Back(self,value):
        self.data.push_Back(value)

    def pop_Back(self):
        self.data.pop_Back()

    def front(self):
        return self.data.front()

    def back(self):
        return self.data.tail

    def empty(self):
        return self.data.isEmpty()

    def size(self):
        return self.data.Size()
    def clear(self):
        self.data.clear()

    def insert(self,index,value):
        self.data.insert(index,value)

    def erase(self,index):
        self.data.erase(index)

    def __getitem__(self, index):
        return self.data[index]

    def print(self):
        self.data.print_List()

if __name__=="__main__":

    dq=deque()
    dq.push_Front(43)
    dq.push_Front(54)
    dq.push_Front(567)
    dq.push_Front(12)
    dq.push_Back(0)
    dq.print()
    dq.insert(4,100)
    dq.print()
    print(dq[0])
    dq.pop_Back()
    dq.print()
    dq.pop_Front()
    dq.print()

    print(dq[1])
    dq.print()
    dq.push_Front(102)
    dq.push_Back(900)
    dq.print()
    dq.insert(2,1000)
    dq.print()





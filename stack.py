from DynamicArray import DynamicArray

class Stack:
    def __init__(self):
        self.elements=DynamicArray(5)

    def push(self,ele):
        if self.elements.n==self.elements.cap:
            print('Stack Is Full')
            return
        else:
            self.elements.pushBack(ele)
    def pop(self):
        if self.Top()==-1:
            print('Stack Is Empty')
            return
        else:
            self.elements.popBack()
    def Top(self):
        return self.elements.n-1
    def  isEmpty(self):
        return self.Top()==-1
    def Size(self):
        return self.elements.n

    def Print(self):
        for i in range(self.elements.n-1,-1,-1):
            print(self.elements.array[i])
        print()

if __name__=='__main__':
    st=Stack()
    st.push(45)
    st.push(12)
    st.push(67)
    st.push(0)
    st.Print()
    st.pop()
    st.pop()
    print(st.Top())
    print(st.isEmpty())
    st.Print()
    print(st.Size())
    st.push(12)
    st.push(45)
    st.push(54)
    st.push(56)



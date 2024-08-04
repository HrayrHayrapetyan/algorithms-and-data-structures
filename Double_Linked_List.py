
class Node:
    def __init__(self,data=None):
        self.next=None
        self.prev=None
        self.data=data

class Double_Linked:
    def __init__(self):
        self.head=None
        self.tail=None

    def push_Front(self, data):

        newNode = Node(data)

        if self.head == None:
            self.head =self.tail=newNode
        else:
            newNode.next = self.head
            self.head.prev=newNode
            self.head=newNode

    def pop_Front(self):
        if self.head==None:
            return None
        if self.head==self.tail:
            self.head=self.tail=None
        self.head=self.head.next
        self.head.prev=None

    def push_Back(self,data):

        newNode=Node(data)
        self.tail.next=newNode
    def pop_Back(self):

        if self.head is None:
            raise IndexError('List Is Empty')

        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None

    def insert_After(self, prev_Node, data):

        curr = self.head
        while (curr.data != prev_Node.data):
            curr = curr.next

        newNode = Node(data)
        newNode.next = curr.next
        curr.next = newNode
    def clear(self):
        self.head=self.tail=None
    def isEmpty(self):
        return self.head is None

    def front(self):
        return self.head

    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def merge_Other(self,ls):
        if self.head is None or ls.head is None:
            raise IndexError('List Is Emtpy')
        self.tail=ls.head

    def sort(self):

        swapped = True
        while swapped:
            swapped = False
            curr = self.head

            while curr.next:
                if curr.data > curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data
                    swapped = True
                curr = curr.next

    def remove_Duplicate(self):

        curr=self.head
        while curr is not None:
            tmp=curr
            while tmp.next is not None:
                if tmp.next.data==curr.data:
                    tmp.next=tmp.next.next
                else:
                    tmp=tmp.next
            curr=curr.next

    def print_List(self):

        curr=self.head

        while curr!=None:
            print(curr.data,end=' ')
            curr=curr.next
        print()

if __name__=='__main__':

    ls=Double_Linked()
    ls.push_Front(45)
    ls.push_Front(435)
    ls.push_Front(78)
    ls.push_Front(12)
    ls.push_Front(89)
    ls.push_Back(100)
    ls.print_List()
    ls.pop_Back()
    ls2=Double_Linked()
    ls2.push_Front(12)
    ls2.push_Front(678)
    ls2.push_Front(0)
    ls2.print_List()
    ls.merge_Other(ls2)
    ls.sort()
    ls.print_List()

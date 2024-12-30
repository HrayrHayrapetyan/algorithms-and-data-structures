from wsgiref.validate import header_re


class Node:
    def __init__(self,data=None):
        self.next=None
        self.prev=None
        self.data=data

class Double_Linked:
    def __init__(self):
        self.head=None
        self.tail=None

    def __getitem__(self, index):

        curr=self.head

        while index>0:
            curr=curr.next
            index-=1
        return curr.data

    def erase(self,index):
        curr=self.head

        while index>=0:
            curr=curr.next
            index-=1

        curr.next=curr.next.next


    def Size(self):
        curr=self.head
        count=0
        while curr:
            curr=curr.next
            count+=1
        return count

    def push_Front(self, data):

        newNode = Node(data)
        if self.head is  None:
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
        if self.tail is None:
            self.head=self.tail=None
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
    def pop_Back(self):

        if self.tail is None:
            return

        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None

    def insert_After(self, prev_Node, data):

        curr=self.head
        newNode=Node(data)

        while curr is not None and curr.data!=prev_Node.data:
            curr=curr.next

        if curr is None:
            raise ValueError('The Given Node Is Not In The List')

        newNode.next=curr.next
        newNode.prev=curr
        curr.next=newNode

        if newNode.next is None:
            self.tail=newNode


    def clear(self):
        self.head=self.tail=None
    def isEmpty(self):
        return self.head is None

    def front(self):
        return self.head

    def insert(self,index,value):
        curr=self.head
        while index>1:
            curr=curr.next
            index-=1

        newnode=Node(value)
        newnode.next=curr.next
        curr.next=newnode

    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def merge_Other(self, other_List):
        curr1 = self.head
        curr2 = other_List.head
        ls3 = Double_Linked()
        dummynode = Node()
        mergedcurr = dummynode

        while curr1 is not None and curr2 is not None:
            if curr1.data <= curr2.data:
                mergedcurr.next = curr1
                curr1.prev=mergedcurr
                curr1 = curr1.next
            else:
                mergedcurr.next = curr2
                curr2.prev=mergedcurr
                curr2 = curr2.next
            mergedcurr = mergedcurr.next

        if curr1 is not None:
            mergedcurr.next = curr1
            curr1.prev=mergedcurr
        else:
            mergedcurr.next = curr2
            curr2.prev=mergedcurr

        ls3.head = dummynode.next

        if ls.head:
            ls.head.prev=None
        curr=ls3.head
        while curr and curr.next:
            curr=curr.next
        ls3.tail=curr
        return ls3

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
    ls.sort()
    ls2.sort()
    ls.print_List()
    ls3=ls.merge_Other(ls2)
    ls3.print_List()

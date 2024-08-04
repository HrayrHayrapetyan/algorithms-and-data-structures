class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push_Front(self,data):

       newNode=Node(data)

       if self.head==None:
           self.head=newNode
       else:
           newNode.next=self.head
           self.head=newNode
    def pop_Front(self):
        if self.head==None:
            return
        self.head=self.head.next

    def insert_After(self,prev_Node,data):

        curr=self.head
        while(curr.data!=prev_Node.data):
            curr=curr.next

        newNode=Node(data)
        newNode.next=curr.next
        curr.next=newNode

    def erase_After(self,prev_node):

        curr=self.head
        while(curr.data!=prev_node.data):
            curr=curr.next

        curr.next=curr.next.next

    def clear(self):
        self.head=None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def front(self):
        return self.head

    def reverse(self):
        prev=None
        curr=self.head

        while curr is not None:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        self.head=prev

    def merge_Other(self,other_List):
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=other_List.head
    def sort(self):

        swapped=True
        while swapped:
            swapped=False
            curr=self.head

            while curr.next:
                if curr.data>curr.next.data:
                    curr.data,curr.next.data=curr.next.data,curr.data
                    swapped=True
                curr=curr.next

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
            print(curr.data,end='->')
            curr=curr.next
        print()

if __name__=='__main__':

    ls=LinkedList()
    ls.head=Node(45)
    ls.head.next=Node(56)
    ls.head.next.next=Node(21)
    ls.push_Front(78)
    ls.insert_After(Node(56),34)
    ls.push_Front(562)
    ls.push_Front(56)
    ls.erase_After(Node(562))
    ls.erase_After(Node(56))

    ls2=LinkedList()
    ls2.push_Front(66)
    ls2.push_Front(66)
    ls2.push_Front(34)
    ls2.print_List()
    ls.merge_Other(ls2)
    ls.print_List()

    ls.sort()
    ls.print_List()
    ls.remove_Duplicate()
    ls.print_List()





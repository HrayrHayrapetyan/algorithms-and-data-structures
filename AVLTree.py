class Node:

    def __init__(self,key):
        self.right=None
        self.left=None
        self.height=1
        self.key=key


class AVLTree:

    def __init__(self):
        self.root=None

    def insert(self,value):
        if not self.root:
            self.root=Node(value)
            return
        self.insert_Helper(self.root,value)

    def getHeight(self,node):
        if not node:
            return 0
        return node.height

    def getBalance(self,node):
        return self.getHeight(node.left)-self.getHeight(node.right)

    def rightRotate(self,node):
        y=node.left
        tmp=y.right

        y.right=node
        node.left=tmp

        y.height=max(self.getHeight(y.left),self.getHeight(y.right))+1
        node.height=max(self.getHeight(node.left),self.getHeight(node.right))+1

        return y

    def leftRotate(self,node):
        y=node.right
        tmp=y.left

        y.left=node
        node.right=tmp

        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1

        return y


    def insert_Helper(self,node,value):
        if not node:
            return Node(value)
        if node.key>value:
            node.left=self.insert_Helper(node.left,value)
        elif node.key<value:
            node.right=self.insert_Helper(node.right,value)
        else:
            return node

        node.height=max(self.getHeight(node.left),self.getHeight(node.right))+1
        balance=self.getBalance(node)

        if balance <-1 and node.right.key<value:
            return self.leftRotate(node)
        if balance <-1 and node.right.key>value:
            node.right=self.rightRotate(node.right)
            return self.leftRotate(node)
        if balance >1 and node.left.key>value:
            return self.rightRotate(node)
        if balance >1 and node.left.key<value:
            node.left=self.leftRotate(node.left)
            return self.rightRotate(node)

        return node

    def delete(self,value):
        self.delete_Helper(self.root,value)

    def min_node(self,node):

        while node.left:
            node=node.left
        return node

    def inorder(self):
        if not self.root:
            return
        self.inorder_Helper(self.root)

    def inorder_Helper(self,node):
        if not node:
            return
        self.inorder_Helper(node.left)
        print(node.key)
        self.inorder_Helper(node.right)


    def delete_Helper(self,node,value):
        if not node:
            return
        if node.key>value:
            node.left=self.delete_Helper(node.left,value)
        elif node.key<value:
            node.right=self.delete_Helper(node.right,value)
        else:
            if not node.left or not node.right:
                return node.right if not node.left else node.left
            else:
                successor=self.min_node(node.right)
                node.key=successor.key
                node.right=self.delete_Helper(node.right,successor.value)

            balance=self.getBalance(node)

            if balance <-1 and self.getBalance(node.right)>0:
                node.right=self.rightRotate(node.right)
                self.leftRotate(node)
            if balance <-1 and self.getBalance(node.right)<0:
                self.leftRotate(node)
            if balance >1 and self.getBalance(node.left):
                self.rightRotate(node)
            if balance >1 and self.getBalance(node.left)<0:
                node.left=self.leftRotate(node.left)
                self.rightRotate(node)

        return node

if __name__=="__main__":

    avl=AVLTree()
    avl.insert(30)
    avl.insert(45)
    avl.insert(50)
    avl.insert(20)

    avl.inorder()




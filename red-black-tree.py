class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.p = None
        self.color = 'R'
        self.key = key


class RBTree:
    def __init__(self) -> None:
        self.root = None
        self.nil = Node(None)
        self.nil.color = 'B'

    def inorderTraversal(self, node):
        if node != self.nil:
            self.inorderTraversal(node.left)
            print(f"Key: {node.key}, Color: {node.color}")
            self.inorderTraversal(node.right)

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y

    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def treeMinimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def insert(self, z):
        if self.root is None:
            self.root = z
            self.root.color = 'B'
            return
        z.left = self.nil
        z.right = self.nil
        y = self.nil
        x = self.root

        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.color = 'R'
        self.insertFixUp(z)

    def insertFixUp(self, z):
        while z.p != self.nil and z.p.color == 'R':
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 'R':
                    z.p.color = 'B'
                    y.color = 'B'
                    z.p.p.color = 'R'
                    z = z.p.p
                elif z == z.p.right:
                    z = z.p
                    self.leftRotate(z)
                z.p.color = 'B'
                z.p.p.color = 'R'
                self.rightRotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == 'R':
                    z.p.color = 'B'
                    y.color = 'B'
                    z.p.p.color = 'R'
                    z = z.p.p
                elif z == z.p.left:
                    z = z.p
                    self.rightRotate(z.p.p)
                z.p.color = 'B'
                z.p.p.color = 'R'
                self.leftRotate(z.p.p)
        self.root.color = 'B'

    def delete(self, z):
        y = z
        origin_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.treeMinimum(z.right)
            origin_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if origin_color == 'B':
            self.deleteFixUp(x)

    def deleteFixUp(self, x):
        while x != self.root and x.color == 'B':
            if x == x.p.left:
                sibling = x.p.right
                if sibling.color == 'R':
                    sibling.color = 'B'
                    self.leftRotate(x.p)
                if sibling.left.color == 'B' and sibling.right.color == 'B':
                    sibling.color = 'R'
                    x = x.p
                elif sibling.right.color == 'B':
                    sibling.left.color = 'B'
                    sibling.color = 'R'
                    self.rightRotate(sibling)
                sibling.color = x.p.color
                x.p.color = 'B'
                sibling.right.color = 'B'
                self.leftRotate(x.p)
                x = self.root
            else:
                sibling = x.p.left
                if sibling.color == 'R':
                    sibling.color = 'B'
                    self.rightRotate(x.p)
                if sibling.left.color == 'B' and sibling.right.color == 'B':
                    sibling.color = 'R'
                    x = x.p
                elif sibling.left.color == 'B':
                    sibling.right.color = 'B'
                    sibling.color = 'R'
                    self.leftRotate(sibling)
                sibling.color = x.p.color
                x.p.color = 'B'
                sibling.left.color = 'B'
                self.rightRotate(x.p)
                x = self.root
        x.color = 'B'


if __name__ == '__main__':
    rbTree = RBTree()

    rbTree.insert(Node(45))
    rbTree.insert(Node(9))
    rbTree.insert(Node(4))
    rbTree.insert(Node(450))
    rbTree.insert(Node(5))

    print("Inorder traversal of the RBTree:")
    rbTree.inorderTraversal(rbTree.root)

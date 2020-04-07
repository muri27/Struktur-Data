class Node:
    
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTreeInOrder(self):
        if self.left:
            self.left.PrintTreeInOrder()
        print(self.data, end=" ")
        if self.right:
            self.right.PrintTreeInOrder()
    
    def PreorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def inorderTraversal(self,root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
    
    def PostorderTraversal(self,root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

#TUGAS 2    
    #METHOD PRINTTREEPOSTORDER(3)
    def PrintTreePostOrder(self):
        if self.left:
            self.left.PrintTreePostOrder()
        if self.right:
            self.right.PrintTreePostOrder()
        print(self.data, end=" ")
        
    #METHOD PRINTTREEPREORDER(3)
    def PrintTreePreOrder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.PrintTreePreOrder()
        if self.right:
            self.right.PrintTreePreOrder()

#TUGAS 3
    #METHOD FINDMAX (5)
    def findMax(self, root):
        if root.right is None:
            return root.data
        return root.findMax(root.right)
    
    #METHOD FINDMIN (6)
    def findMin(self, root):
        if root.left is None:
            return root.data
        return root.findMin(root.left)
    
    #METHOD CARI (7)
    def cari(self, data):
        if data < self.data:
            if self.left is None:
                return False
            return self.left.cari(data)
        elif data > self.data:
            if self.right is None:
                return False
            return self.right.cari(data)
        else:
            return True
    
    #METHOD COUNT (8)
    def count(self, root):
        counter = 1
        if root is None:
            return -1
        else:
            if root.left is not None:
                counter += self.count(root.left)
            if root.right is not None:
                counter += self.count(root.right)
        return counter
    
        
        
root = Node(4)
root.insert(3)
root.insert(2)
root.insert(5)
root.insert(6)
root.insert(1)
root.insert(9)
root.insert(8)

#3
root.PrintTreePreOrder()
print()
root.PrintTreePostOrder()
print()

#4
print(root.inorderTraversal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))
print()

#5
print(root.findMax(root))
#6
print(root.findMin(root))
#7
print(root.count(root))
#8
print(root.cari(2))
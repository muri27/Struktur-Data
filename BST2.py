class Node: 
    def __init__(self, nilai): 
        self.kiri = None
        self.kanan = None
        self.data = nilai
  

def insert(akar, node): 
    if akar is None: 
        akar = node 
    else: 
        if akar.data < node.data: 
            if akar.kanan is None: 
                akar.kanan = node 
            else: 
                insert(akar.kanan, node) 
        else: 
            if akar.kiri is None: 
                akar.kiri = node 
            else: 
                insert(akar.kiri, node) 
  
def preorder(akar): 
    if akar:
        print(akar.data, end=" ") 
        preorder(akar.kiri) 
        preorder(akar.kanan)

def counter(akar):
    count = 1
    if akar is None:
        return -1
    else:
        if akar.kiri is not None:
            count += counter(akar.kiri)
        if akar.kanan is not None:
            count += counter(akar.kanan)
    return count
        
def minNode(node): 
    current = node   
    while(current.kiri is not None): 
        current = current.kiri    
    return current  

def deleteNode(akar, nilai): 
    if akar is None: 
        return akar  

    if nilai < akar.data: 
        akar.kiri = deleteNode(akar.kiri, nilai) 
  
    elif(nilai > akar.data): 
        akar.kanan = deleteNode(akar.kanan, nilai) 
  
    else: 
    
        if akar.kiri is None : 
            temp = akar.kanan  
            akar = None 
            return temp  
              
        elif akar.kanan is None : 
            temp = akar.kiri  
            akar = None
            return temp 
  
        temp = minNode(akar.kanan) 
        akar.data = temp.data 
        akar.kanan = deleteNode(akar.kanan , temp.data) 
  
  
    return akar 
 
n = int(input())
bst = list(map(int, input().split()))
r = Node(int(bst[0]))
for i in range(len(bst)):
    if bst[i] != bst[0]:
        insert(r, Node(int(bst[i])))
m = int(input())
preorder(r)
deleteNode(r, m)
print()
preorder(r)
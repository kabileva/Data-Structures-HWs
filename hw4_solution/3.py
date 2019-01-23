class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self,item):
        self.key = item
    
    def getRootVal(self):
        return self.key
    
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    
def preorder(tree):
    
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
       
def postorder(tree):
    
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
    
        
def inorder(tree):
    
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
        
def wrPost(tree):
    tmpStack = Stack()
    printStack = Stack()
    tmpStack.push(tree)
    while not tmpStack.isEmpty():
        tree = tmpStack.pop()
        printStack.push(tree)
        if tree.getLeftChild():
            tmpStack.push(tree.getLeftChild())
        if tree.getRightChild():
            tmpStack.push(tree.getRightChild())
    while not printStack.isEmpty():
        print(printStack.pop().getRootVal())
        
def wrPre(tree):
    nodeStack = Stack()
    nodeStack.push(tree)  
    while not nodeStack.isEmpty():
        tree = nodeStack.pop()
        print(tree.getRootVal())        
        if tree.getRightChild():
            nodeStack.push(tree.getRightChild())
        if tree.getLeftChild():
            nodeStack.push(tree.getLeftChild())  
        
    
  
tree = BinaryTree('A')
tree.insertLeft('B')
tree.getLeftChild().insertLeft('D')
tree.getLeftChild().insertRight('E')
tree.getLeftChild().getLeftChild().insertLeft('H')
tree.getLeftChild().getLeftChild().insertRight('I')
tree.insertRight('C')
tree.getRightChild().insertLeft('F')
tree.getRightChild().insertRight('G')

print("Here's the example of program's output")
print("I used the complete binary tree from previous problem ([A,B,C,D,E,F,G,H,I])")
print()

print('postorder() function output with recursion: '),
postorder(tree)
print()

print('postorder() function output without recursion: '),
wrPost(tree)
print()


print('preorder() function output with recursion: '),
preorder(tree)
print()

print('preorder() function output without recursion: '),
wrPre(tree)
print()

    
from ADT.tree import BinaryTree
from ADT.stack import Stack
from ADT.queue import Queue
f = input("Please type the name of your file, i.e. 'name.txt'n which is stored in the same directory as the program code file (sequence of tree-elements should be printed in one line in the file) and press 'Enter': \n")
file = open(f, 'r')
storedTree = file.readline().strip().split()
#storedTree = ['cat','apple','but','pull','line','food','me','say']
stack = Stack() 

tree = BinaryTree(storedTree[0]) #define the root
storedTree.remove(storedTree[0])

stack.push(tree)

current = tree

for node in storedTree:
    if not stack.isEmpty():
        if node<stack.top().getRootVal(): #store in left subtree
            current.insertLeft(node)
            current = current.getLeftChild()
            stack.push(current)
        else:                             #store in right subtree
            while (not stack.isEmpty() and node>stack.top().getRootVal()):
                
                current = stack.pop()
            current.insertRight(node)
            current = current.getRightChild()
            stack.push(current)
            
            
def level_print(tree):
    Pqueue = Queue() #parent nodes
    Cqueue = Queue() #children
    Pqueue.enqueue(tree)
    while not Pqueue.isEmpty():
        while not Pqueue.isEmpty():
            node = Pqueue.dequeue()
            print(node.getRootVal(), end=' ')
            if node.getLeftChild():
                Cqueue.enqueue(node.getLeftChild())
            if node.getRightChild():
                Cqueue.enqueue(node.getRightChild())
        print()
        while not Cqueue.isEmpty():
            Pqueue.enqueue(Cqueue.dequeue())
        

level_print(tree)    
    
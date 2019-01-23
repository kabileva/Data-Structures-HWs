
from ADT.stack import Stack
from ADT.tree import BinaryTree
    
def isSign(value): 
    if value in ['+','-','*','/']:
        return True
    
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
     
def exp_to_list(expression):
    exp_l = []
    tmp = ''
    for i in expression:
        if (i in '1234567890') or (i=='.'):
            tmp += i
             
        elif isSign(i) or (i in ['(',')']):
            if tmp != '':
                exp_l.append(tmp)
            exp_l.append(i)
            tmp = ''
    return exp_l

def BuildTree(exp_l):
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    current = tree
    
    for op in exp_l:
        if op == '(':
            current.insertLeft('')
            new = current.getLeftChild()
            stack.push(current)
            current = new
        elif op.isdigit() or isFloat(op):
            current.setRootVal(op)
            current = stack.pop()
        elif isSign(op):
            current.setRootVal(op)
            current.insertRight('')
            stack.push(current)
            current = current.getRightChild()
        elif op == ')':
            current = stack.pop()
        else:
            raise ValueError            
    return tree

        
def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        post_l.append(tree.getRootVal())
        
def op_result(a,b,c):
    if c=='+':
        return float(a)+float(b)
    elif c=='-':
        return float(a)-float(b)
    elif c=='*':
        return float(a)*float(b)
    elif c=='/':
        return float(a)/float(b)       
    
def Evaluation(post_l):
    expr = Stack()
    for i in post_l:
        if i.isdigit() or isFloat(i):
            expr.push(i)
        elif isSign(i):
            b=expr.pop()
            a=expr.pop()
            expr.push(op_result(a,b,i))
    print ('The result is:', expr.top())
    return expr.top()
                
def main(expression):
    exp = exp_to_list(expression)

    tree = BuildTree(exp)
    global post_l
    post_l = []
    postorder(tree)
    Evaluation(post_l)

while True:
    expression = input('Print an expression: ')
    main(expression)
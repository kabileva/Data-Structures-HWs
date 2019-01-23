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



def precedence(a):
     if a=='(':
          return 1
     elif a=='+' or a=='-':
          return 2
     elif a=='*' or '/':
          return 3
     
def isSign(a):
     if a in ['+','-','*','/']:
          return True
     
def op_result(a,b,c):
     if c=='+':
          return int(a)+int(b)
     elif c=='-':
          return int(a)-int(b)
     elif c=='*':
          return int(a)*int(b)
     elif c=='/':
          return int(a)/int(b)
     
def toPostfix(expression):
     stack = Stack()
     exp_l = []
     tmp = ''
     for i in expression:
          if i in '1234567890':
               tmp += i
              
          elif isSign(i) or (i in ['(',')']):
               if tmp != '':
                    exp_l.append(tmp)
               exp_l.append(i)
               tmp = ''
     
     post_l = []
     for i in exp_l:
          if i.isdigit():
                      
               post_l.append(i)
               
          elif i == '(':
               stack.push(i)
          elif i == ')':
               if not stack.isEmpty():
                    top = stack.pop()
                    while top != '(':
                         post_l.append(top)
                         top = stack.pop()
               
          elif isSign(i):
               while (not stack.isEmpty() and precedence(stack.top())>=precedence(i)):
                    post_l.append(stack.pop())
               stack.push(i)
     while not stack.isEmpty():
          post_l.append(stack.pop())
          
   
     return post_l
                    
     
def Evaluation(post_l):
     expr = Stack()
     for i in post_l:
          if i.isdigit():
               expr.push(i)
          elif isSign(i):
               b=expr.pop()
               a=expr.pop()
               expr.push(op_result(a,b,i))
     print 'The result is:', expr.top()
     return expr.top()
                   
while True:     
     print '____________________________________________' 
     print
     expr = raw_input('Please write a fully parethesized infix expression: ')
     
     Evaluation(toPostfix(expr))
     print
     

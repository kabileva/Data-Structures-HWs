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
     
     def stack_to_list(self):
          
          l = []
              
          while not self.isEmpty():
               t = []
               for i in range(2):
                    t.append(self.pop())
               t.reverse()
               l.append(t)
          return l
     
     def stack_to_polynomial(self, order):
          final = 'P' + order + '(x) = '
            
          l = self.stack_to_list() 
         
          def getKey(item):
               return item[-1] 
          
          
          l = sorted(l, key = getKey)
          l.reverse()
          for i in range(len(l)):
               if l[i][0]>'1':
                    final = final + l[i][0] + 'x'
               elif l[i][0]=='1':
                    final = final + 'x'
               if l[i][1]>'1':
                    final = final + '**' + l[i][1]
               elif l[i][1] == '0':
                    final = final.rstrip('x')
                    if final[-1]==' ':
                         final = final + '1'
               if i<(len(l)-1):
                    final = final + ' + '
          for j in l:
               for i in range(2):
                    self.push(j[i]) 
          print          
          print final
          print
          return self   
     
     
def pol_to_stack(p):
     stack = Stack()
     i=0
     while i < (len(p)):
                    
          if p[i].isdigit():
               stack.push(p[i])
               i += 1
          else:
               i += 1    
     return stack       



class Polynomial_Calculus_ADT():
     

     def __init__(self):
          
          print '____________'
          print
          polynomial1 = raw_input("Enter the polynomial in the form  '(A, B), (C, D)', where A,B,C,D are integers, to get the polynomial in the form of 'Ax**B + Cx**D' and press 'Enter' ")
          print
          polynomial2 = raw_input("Enter the second polynomial and press 'Enter' ") 
          print
          
          
          self.operation = raw_input("Specify the operation. Enter 'a' to add polynomials, 'm' to multiply and 'd' to differentiate ")
          
          self.stack_1 = pol_to_stack(polynomial1)
          self.stack_2 = pol_to_stack(polynomial2)
                   
         
     def add(self, stack_1, stack_2, index='_add'):
          
          
          if stack_1.size() > stack_2.size():
               self.stack_max = stack_1
               self.stack_min = stack_2
          else:
               self.stack_max = stack_2
               self.stack_min = stack_1          
          stack_add = Stack()
          while not self.stack_max.isEmpty():
               if not self.stack_min.isEmpty():
                    if self.stack_max.top() != self.stack_min.top():
                         stack_add.push(self.stack_max.pop())
                         stack_add.push(self.stack_max.pop())
                    else:
                         self.stack_max.pop()
                         stack_add.push(self.stack_min.pop())
                         stack_add.push(str(int(self.stack_min.pop())+int(self.stack_max.pop())))
          while not self.stack_min.isEmpty():
               stack_add.push(self.stack_min.pop())
               stack_add.push(self.stack_min.pop())
          stack_addf=Stack()
          while not stack_add.isEmpty():
               stack_addf.push(stack_add.pop())

          return stack_addf.stack_to_polynomial(index)
          
     def multiplicate(self, stack_1, stack_2):
          
          
          l1 = stack_1.stack_to_list()
          l2 = stack_2.stack_to_list()
          
          store1 = Stack()
          store_t = Stack()
          store2 = Stack()
          
          for i in l1:
               for j in l2:
                    store1.push(str(int(i[0])*int(j[0])))
                    store1.push(str(int(i[1])+int(j[1])))

          stack_mult=Stack()
          
          if store1.size()>2:
               while not store1.isEmpty():
                    for i in range(2):
                         
                         store_t.push(store1.pop())
                   
                    for i in range(2):
                    
                         stack_mult.push(store_t.pop())
               
                                         
                    self.add(store1,stack_mult, '_mult')
          else:
               
               return store1.stack_to_polynomial('_mult')           
          
     def differentiate(self, stack_1, stack_2):
          stack_1_d = Stack()
          while not stack_1.isEmpty():
               c = stack_1.pop()
               d = stack_1.pop()
               
               stack_1_d.push(str(int(c)*int(d)))
               stack_1_d.push(str(int(c)-1))
              
          stack_1_d.stack_to_polynomial('1_diff')

          stack_2_d = Stack()
          while not stack_2.isEmpty():
               a = stack_2.pop()
               b = stack_2.pop()
               stack_2_d.push(str(int(a)*int(b)))
               stack_2_d.push(str(int(a)-1))               
          stack_2_d.stack_to_polynomial('2_diff')
    
     def operand(self, stack_1, stack_2):
          
          if self.operation == 'a':
               self.add(stack_1, stack_2)
          elif self.operation == 'm':
               self.multiplicate(stack_1, stack_2)
          elif self.operation == 'd' or self.operation == 'D':
               self.differentiate(stack_1, stack_2)

while True:               
     a = Polynomial_Calculus_ADT()     
     s1 = a.stack_1
     s2 = a.stack_2
     a.operand(s1, s2)
          
          
         
     
               
                    
     
                    
                    
                    
     
          
          
          
               
     
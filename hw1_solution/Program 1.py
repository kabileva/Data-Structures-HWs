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
     
     def stack_to_polynomial(self, order=''):
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

while True:
     
     print '____________'
     print
     polynomial1 = raw_input("Enter the polynomial in the form  '(A, B), (C, D)', where A,B,C,D are integers, to get the polynomial in the form of 'Ax**B + Cx**D' and press 'Enter' ")
     print
     pol_to_stack(polynomial1).stack_to_polynomial()
     

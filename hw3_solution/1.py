
from math import floor, log10

while True:
    print '---------------------------------------------'
    print 
    
    a = input('Please, enter an integer in base 10: ' )
    print 'A number of digits is', int(floor(log10(a))+1)    
    print
   
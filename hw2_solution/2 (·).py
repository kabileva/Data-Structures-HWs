import time
class AirQueue:
    
    def __init__(self):
        self.first = []
        self.business =[]
        self.economy =[]
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item,priority):
        self.priority = priority
        if self.priority == '1':
            self.first.insert(0,item)
        elif self.priority == '2':
            self.business.insert(0,item)
        elif self.priority == '3':
            self.economy.insert(0,item)
            
    def dequeueFirst(self):
        return self.first.pop()
    
    def dequeueBusiness(self):
        return self.business.pop()
    
    def dequeueEconomy(self):
        return self.economy.pop()
    
    def dequeueAll(self):
        while self.first != []:
            print self.first.pop(),
        while self.business != []:
            print self.business.pop(),
        while self.economy != []:
            print self.economy.pop(),
 
def AirFlightPassengers(): 
    AirFlight = AirQueue()   
    a = True
    while a:
        passenger = raw_input()
        
        if passenger == 'done':
            a = False
        else:
            AirFlight.enqueue(passenger, passenger[-2])
    AirFlight.dequeueAll()

AirFlightPassengers()

time.sleep(120)



    

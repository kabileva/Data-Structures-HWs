def HanoiTower(height,Pole1, Pole2, Pole3):
    if height >= 1:
        HanoiTower(height-1,Pole1,Pole2,Pole3)
        
        Disk(Pole1,Pole3)
        
        HanoiTower(height-1,Pole2,Pole3,Pole1)

def Disk(pos1,pos2):
    print "Move disk from",pos1,"to",pos2 

while True:
    print 
    print '---------------------------------------------'
    print
    height = input('Enter an enteger greater or equal to 1 for the height of Hanoi Tower: ')
    HanoiTower(height,"Left pole","Middle pole", 'Right pole')

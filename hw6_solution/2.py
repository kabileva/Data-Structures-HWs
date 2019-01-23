from ADT.VertGraph import Vertex
from ADT.VertGraph import Graph
from ADT.stack import Stack

def DFS(startVert,s):
    
    stack = Stack() #main stack
    stack.push(startVert)
    while not stack.isEmpty():
        currentVert = stack.pop()
        if currentVert.getCondition()=='undiscovered':
            s.add(currentVert)
           
            currentVert.setCondition('discovered')
            stack_adj = Stack() #stack for adjacency verices
            for vert in currentVert.getConnections():
                
                if (vert.getCondition() == 'undiscovered'):
                    stack_adj.push(vert)
                    
            while not stack_adj.isEmpty(): #swap
                stack.push(stack_adj.pop())
        
                
def ConnectedComponents(V):              
    for vert in V.vertList.values():
        if vert.getCondition()=='undiscovered':
            s = set()        
            DFS(vert,s)
            V.connectedGroups.append(s)
##Sample graph
V = Graph()
V.addEdge('V0','V1')
V.addEdge('V1','V0')    #V0--V1--V2--V3
V.addEdge('V1','V2')    #         |
V.addEdge('V2','V3')    #         V4
V.addEdge('V3','V2')    #
V.addEdge('V2','V1')    #V5---V6
V.addEdge('V2','V4')
V.addEdge('V4','V2')
V.addEdge('V5','V6')
V.addEdge('V6','V5')
                    
ConnectedComponents(V)                
group_ind = 1

for i in V.connectedGroups:
    print(group_ind,end=': ')
    for vert in i:
        print(vert, end =', ')
    print()
    group_ind+=1    




   




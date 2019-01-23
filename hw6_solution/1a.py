from ADT.VertGraph import Vertex
from ADT.VertGraph import Graph
from ADT.stack import Stack

def DFS(startVert):
    tree = Graph() #Breadth first spanning tree
    stack = Stack() #main stack
    stack.push(startVert)
    while not stack.isEmpty():
        currentVert = stack.pop()
        if currentVert.getCondition()=='undiscovered':
            print(currentVert, 'is adding to the DF-spanning tree now')
            
            currentVert.setCondition('discovered')
            stack_adj = Stack() #stack for adjacency verices
            for vert in currentVert.getConnections():
                if (vert.getCondition() == 'undiscovered'):
                    tree.addEdge(currentVert.getId(), vert.getId())
                    stack_adj.push(vert)
                    
            while not stack_adj.isEmpty(): #swap
                stack.push(stack_adj.pop())
    return tree          
                ###=================

V = Graph()

'''
#Graph from the lecture

V.addEdge('V0','V1')
V.addEdge('V0','V2')
V.addEdge('V1','V3')
V.addEdge('V1','V4')
V.addEdge('V2','V5')
V.addEdge('V2','V6')
V.addEdge('V3','V7')
V.addEdge('V4','V7')
V.addEdge('V5','V7')
V.addEdge('V6','V7')

V.addEdge('V1','V0')
V.addEdge('V2','V0')
V.addEdge('V1','V3')
V.addEdge('V4','V1')
V.addEdge('V5','V2')
V.addEdge('V6','V2')
V.addEdge('V7','V3')
V.addEdge('V7','V4')
V.addEdge('V7','V5')
V.addEdge('V7','V6')

'''
#Sample graph

V.addEdge('V0','V1')    #V0---V1---V2
V.addEdge('V1','V0')    #|     |    |
V.addEdge('V1','V2')    #V7---V9---V3
V.addEdge('V2','V1')    #|     |    |
V.addEdge('V2','V3')    #V6---V5---V4
V.addEdge('V3','V3')
V.addEdge('V3','V4')
V.addEdge('V4','V3')
V.addEdge('V5','V4')
V.addEdge('V4','V5')
V.addEdge('V6','V5')
V.addEdge('V5','V6')
V.addEdge('V6','V7')
V.addEdge('V7','V6')
V.addEdge('V7','V0')
V.addEdge('V0','V7')
V.addEdge('V1','V9')
V.addEdge('V9','V1')
V.addEdge('V9','V5')
V.addEdge('V5','V9')
V.addEdge('V9','V7')
V.addEdge('V7','V9')
V.addEdge('V9','V3')
V.addEdge('V3','V9')


###==========================


startV = V.getVertex('V0')
tree = DFS(startV)



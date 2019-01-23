from ADT.VertGraph import Vertex
from ADT.VertGraph import Graph
from ADT.queue import Queue



def BFS(startVert):
  tree = Graph() #breadth-first spanning tree
  startVert.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(startVert)
  while not vertQueue.isEmpty():
    currentVert = vertQueue.dequeue()
    print(currentVert, 'is adding to the tree now')
    for vert in currentVert.getConnections():
      
      if (vert.getCondition() == 'undiscovered'):
        
        vert.setCondition('discovering') 
        
        tree.addEdge(currentVert.getId(),vert.getId())
                
        vert.setPred(currentVert.getId())
        vertQueue.enqueue(vert)
    
    currentVert.setCondition('discovered')
  return tree

  

###=================
V = Graph()
'''
##Graph from the lecture for example

V.addEdge('V0','V2')
V.addEdge('V2','V0')

V.addEdge('V0','V1')
V.addEdge('V1','V0')

V.addEdge('V1','V3')
V.addEdge('V3','V1')

V.addEdge('V1','V4')
V.addEdge('V4','V1')

V.addEdge('V2','V5')
V.addEdge('V5','V2')

V.addEdge('V2','V6')
V.addEdge('V6','V2')

V.addEdge('V3','V7')
V.addEdge('V7','V3')

V.addEdge('V4','V7')
V.addEdge('V7','V4')

V.addEdge('V6','V7')
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
tree = BFS(startV)

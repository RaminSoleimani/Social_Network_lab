# -*- coding: utf-8 -*-
"""
@author: Ramin Soleimani
@email:  ramin.soleimani222@gmail.com
"""""""""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import time
from matplotlib.pyplot import figure



"""a) Complete the code of the loadDataZachary function."""


print("####Excercise1 a) Complete the code of the loadDataZachary function.######################################")



def loadDataZachary(fileName):
  """
  This method loads from file the adjacency matrix of Zachary network.

  :param file: Full path and name of the file containing the adjacency matrix of the Zachary social network
  :return: G: Graph with the social network
  """

  "Initialize a graph"
  G = nx.Graph()

  "Open file"
  f = open(fileName)

  line = f.readline().rstrip("\n").rstrip("\r")
  while line:
     if(line[0]!="%"):
        ls =line.split(' ')
        num,nums=int(ls[0]),int(ls[1])
        G.add_edge(num,nums)
     line = f.readline().rstrip("\n").rstrip("\r")

  "Closing the file"
  f.close()

  return G, 'Zachary'

G,socialNetwork = loadDataZachary('./data/out.ucidata-zachary.txt')
figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)


nx.draw(G, node_color='blue', with_labels=True ,node_size=500)

plt.savefig("Session3 ZacharyGraph.png")
plt.title("ZacharyGraph" , color='blue', fontweight='bold')
plt.show()
#nx.draw(G,with_labels=True )


"""Excercise1 b) Complete the code to visualize the Zachary network."""
print("####Excercise1 b) Complete the code to visualize the Zachary network.######################################")

plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.subplot(122)
nx.draw_shell(G, with_labels=True, font_weight='bold')
##plt.show()

plt.savefig("Session3 ZacharyGraph Visualiztion.png")
plt.title("Graph of {} Network.".format(socialNetwork))

"TODO: Exercise 1b. Show zachary graph"


plt.axis('off')
plt.show()    

"""Excercise2 a) Complete the code of the loadDataInfectious function."""
print("####Excercise2 Complete the code of the loadDataInfectious function ######################################")
def loadDataInfectious(fileName):

  G= nx.Graph()

  f = open(fileName)
  line = f.readline().rstrip("\n").rstrip("\r")
  
  while line:
    if(line[0]!="%"):
      ls=line.split(' ')
      G.add_edge(ls[0],ls[1], weight=ls[2], timestamp=ls[3])


    "TODO: Exercise 2a. read each line of the file and parse its contents to create the graph. " \
    "Be aware that each line has 4 elements: node1, node2, edge weigth and timestamp"
    
    line = f.readline().rstrip("\n").rstrip("\r")
  f.close()

  return G, 'Infectious'

"""Excercise2 b) Complete the code to visualize the Infectious network."""
print("### Excercise2 b) Complete the code to visualize the Infectious network.######################################")
G, socialNetwork = loadDataInfectious('./data/out.sociopatterns-infectious.txt')
figure(num=None, figsize=(16, 8), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(G, node_color='blue', with_labels=True ,node_size=50)

##plt.show()

plt.savefig("Session2 Infectious network.png")
plt.title("Graph of {} Network.".format(socialNetwork))

"TODO: Exercise 1b. Show zachary graph"


plt.axis('off')
plt.show()
##nx.draw(G, with_labels=True)

# Write your code here
"""Exercise3 a) Modify the code of the loadDataInfectious function to convert timestamp field to a datetime field"""
# Write your code here
def loadDataInfectious(fileName):

  G = nx.Graph()

  f = open(fileName)
  line = f.readline().rstrip("\n").rstrip("\r")
  # 
  maxtime = datetime.strptime('2000', '%Y')
  mintime = datetime.now()
  timestamp=[]
  nodes=[]
  edges=[]
  weight=[]
  datetimearray=[]
  while line:
    if(line[0]!="%"):
      ls=line.split(' ')
      nodes.extend([int(ls[0]),int(ls[1])]) 
      edges.append((int(ls[0]),int(ls[1]),int(ls[2]),int(ls[3]))) 
      timestamp.append(int(ls[3]))
      dt=datetime.fromtimestamp(int(ls[3]))
     
      if(dt.hour== 12  ):
        G.add_edge(int(ls[0]),int(ls[1]), weight=int(ls[2]), timestamp=int(ls[3]))
        datetimearray.append(dt)
        ##print(datetimearray)
      
    line = f.readline().rstrip("\n").rstrip("\r")
  f.close()
  timestamp.sort()
  
  mintime=datetime.fromtimestamp(timestamp[0])
  maxtime=datetime.fromtimestamp(timestamp[-1])
  print(mintime)
  print(maxtime)
  print (len(list(G.nodes)))
 ## print(edges)


  #print(timestamp)

  return G, 'Infectious', mintime, maxtime

"""Exercise3 b) Complete the code to visualize first hour of the Infectious network."""
print("###Complete the code to visualize first hour of the Infectious network.#############################")
fileName="./data/out.sociopatterns-infectious.txt"
G, socialNetwork, mintime,maxtime = loadDataInfectious(fileName)
figure(num=None, figsize=(16, 8), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(G, node_color='blue', with_labels=True ,node_size=50)

##plt.show()

plt.savefig("Session3 first hour of the Infectious network.png")
plt.title("First hour of Infectios network")

"TODO: Exercise 1b. Show zachary graph"


plt.axis('off')
plt.show()






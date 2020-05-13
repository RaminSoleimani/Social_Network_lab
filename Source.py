# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import time

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
  ##print(mintime)
  ##print(maxtime)
  ##print (len(list(G.nodes)))
 ## print(edges)


  #print(timestamp)

  return G, '1st hour of Infectious', mintime, maxtime

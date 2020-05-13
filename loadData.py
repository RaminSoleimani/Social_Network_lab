# -*- coding: utf-8 -*-
u'''

Loading File Data of social networks

Arguments:
  -f,--filename: File containing
  -s,--socialNetwork: name of the Social Network to be loaded from filename

Created on 26/1/2019

@author: Oriol Ramos Terrades (oriolrt@cvc.uab.cat)
@Institution: Computer Vision Center - Universitat Autonoma de Barcelona
'''



import networkx as nx
import matplotlib.pyplot as plt
import sys
import getopt
from datetime import datetime, timedelta


#def loadDataZachary(fileName):
#  """
#  This method loads from file the adjacency matrix of Zachary network.
#
#  :param fileName: Full path and name of the file containing the adjacency matrix of the Zachary social network
#  :return: G: Graph with the social network
#  """
#
#
#  "Initialize a graph"
#  G = nx.Graph()
#
#
#  "Open file"
#  f = open(fileName)
#
#
#  line = f.readline().rstrip("\n").rstrip("\r")
#  while line:
#    if(line[0]!="%"):
#        ls =line.split(' ')
#        num,nums=int(ls[0]),int(ls[1])
#        G.add_edge(num,nums)
#    "TODO: Exercise 1. read each line of the file and parse its contents to create the graph"
#
#    line = f.readline().rstrip("\n").rstrip("\r")
#
#  "Closing the file"
#  f.close()
#
#  return G
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

  return G



def loadDataInfectious(fileName):
  """
  This method loads from file the adjacency matrix of Infectious network.

  :param fileName: Full path and name of the file containing the adjacency matrix of the Infectious social network
  :return: G, mintime, maxtime: Graph with the social network, first infectious case and last infectious case
  """

  "Initialize a graph"

  G = nx.Graph()


  f = open(fileName)
  line = f.readline().rstrip("\n").rstrip("\r")
  maxtime = datetime.strptime('2000', '%Y')
  mintime = datetime.now()
  timestamp=[]
  nodes=[]
  edges=[]


  while line:
    if(line[0]!="%"):
      ls=line.split(' ')
      nodes.extend([int(ls[0]),int(ls[1])]) 
      edges.append((int(ls[0]),int(ls[1]),int(ls[2]),int(ls[3]))) 
      timestamp.append(int(ls[3]))
      dt=datetime.fromtimestamp(int(ls[3]))
      if(dt.hour==12):
        G.add_edge(int(ls[0]),int(ls[1]), weight=int(ls[2]), timestamp=int(ls[3]))
    
    "TODO: Exercise 2. read each line of the file and parse its contents to create the graph. " \
    "Be aware that each line has 4 elements: node1, node2, edge weigth and timestamp"


    line = f.readline().rstrip("\n").rstrip("\r")
  f.close()

  return G,mintime,maxtime

if __name__ == '__main__':

  fullCmdArguments = sys.argv
  unixOptions = "hvf:s:"
  gnuOptions = ["help", "verbose", "filename=","socialNetwork"]
  isInfectious = False
  isZachary = False



  try:
    arguments, values = getopt.getopt(fullCmdArguments[1:], unixOptions, gnuOptions)
  except getopt.error as err:
    # output error, and return with an error code
    print(str(err))
    sys.exit(2)

  # evaluate given options
  for currentArgument, currentValue in arguments:
    if currentArgument in ("-v", "--verbose"):
      print("enabling verbose mode")
    elif currentArgument in ("-h", "--help"):
      print(__doc__)
      sys.exit(0)
      # print ("displaying help")
    elif currentArgument in ("-f", "--filename"):
      fileName = currentValue
    elif currentArgument in ("-s", "--socialNetwork"):
      socialNetwork = currentValue

  if 'fileName' not in locals():
    print("Wrong parameters. See the help.")
    print(__doc__)
    sys.exit(-1)


  if socialNetwork.lower()=="zachary":
    isZachary = True
    G = loadDataZachary(fileName)

  if socialNetwork.lower() == "infectious":
    isInfectious = True
    G,mintime,maxtime = loadDataInfectious(fileName)



  if G.size()==0:
    print("Functions have to be implemented. Showing a random graph instead")
    G = nx.petersen_graph()
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.subplot(122)
    nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
    plt.show()

    sys.exit(0)

  plt.title("Graph of {} Network.".format(socialNetwork))

  if isZachary:
    "TODO: Exercise 1. Show zachary graph"


    plt.axis('off')
    plt.show()


  if isInfectious:
    pos = nx.spring_layout(G)
    "TODO: Exercise 2. Show Infectious  graph"




    plt.axis('off')
    plt.show()

    "TODO: Exercise 3. Show first hour of the Infectious  graph"
    selNodes = set([u for (u, v, d) in G.edges(data=True) if d['datetime'] < mintime + timedelta(hours=1)] + \
                   [v for (u, v, d) in G.edges(data=True) if d['datetime'] < mintime + timedelta(hours=1)])

    G1 = G.subgraph(selNodes)
    pos = nx.spring_layout(G1)

    plt.title("Subgraph of {} network. First hour".format(socialNetwork))

    plt.axis('off')
    plt.show()

  print("Graph loaded")
  sys.exit(0)

# -*- coding: utf-8 -*-
"""
@author: Ramin Soleimani
@email:  ramin.soleimani222@gmail.com
"""""""""
"""Importing Libraries"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms import community

import loadData as ld
import plot_aux 


"""Loading graphes"""

XarxaNetwork = 'Simple Network'
fileName = './data/Xarxa1.txt'

print('File name: ',fileName)
#GX = ld.loadDataZachary(fileName)
GX=nx.read_edgelist(fileName,create_using=nx.Graph(),nodetype=int)

ZacharyNetwork = './data/Zachary'
fileName = './data/out.ucidata-zachary.txt'

print('File name: ',fileName)
GZ = ld.loadDataZachary(fileName)

InfectiousNetwork = '1st hour of Infectious'
fileName = './data/out.sociopatterns-infectious.txt'
print('File name: ',fileName)

# loading the full data
GI,mintime,maxtime = ld.loadDataInfectious(fileName)




"""Exercise 1: Cliques with NetworkX. For networks Xarxa1, Zachary and first hour of Infectious
a) Find all the cliques of the loaded graph (see the function find_cliques in the documentation). "
b) Compute the highest order of cliques."""

# a) All cliques for the Xarxa Network. Replace []
cliquesX = (list(nx.find_cliques(GX)))

if len(cliquesX) >0:
  biggestCliqueX = cliquesX[np.argmax([len(x) for x in cliquesX])]
else:
  biggestCliqueX = []

# b) Highest clique order
maxOrderX = len(biggestCliqueX)

# a) All cliques for the Zachary Network. Replace []
cliquesZ = (list(nx.find_cliques(GZ)))

if len(cliquesZ) >0:
  biggestCliqueZ = cliquesZ[np.argmax([len(x) for x in cliquesZ])]
else:
  biggestCliqueZ = []
# b) Highest clique order
maxOrderZ = len(biggestCliqueZ)

# a) All cliques for the 1st hour of Infectious Network. Replace []
cliquesI = (list(nx.find_cliques(GI)))

if len(cliquesI) >0:
  biggestCliqueI = cliquesI[np.argmax([len(x) for x in cliquesI])]
else:
  biggestCliqueI = []
# b) Highest clique order
maxOrderI = len(biggestCliqueI)

plot_aux.plotBiggestClique(GX, biggestCliqueX, XarxaNetwork)
plot_aux.plotBiggestClique(GZ, biggestCliqueZ, ZacharyNetwork)
plot_aux.plotBiggestClique(GI, biggestCliqueI, InfectiousNetwork)




"""Exercise 2: K-cores with NetworkX.
For networks Xarxa1, Zachary and first hour of Infectious find the K core subgraph with highest K.

a) Compute the k_core subgraph of the loaded graph. """

print("###k_core subgraph of the graphs########################################")
   

k_coresX = nx.k_core(GX)

if not None:
  plot_aux.plotKCores(GX, k_coresX, XarxaNetwork)

k_coresZ = nx.k_core(GZ)

if not None:
  plot_aux.plotKCores(GZ, k_coresZ, ZacharyNetwork)

k_coresI = nx.k_core(GI)

if not None:
  plot_aux.plotKCores(GI, k_coresI, InfectiousNetwork)




"""Exercise 3: Community detection.
For networks Xarxa1, Zachary and first hour of Infectious find their communities with two different methods.

a) Compute the communities of the loaded graph using the Girvan-Newman algorithm (see the function girvan_newman in the documentation)"""
print("###computing the communities of the loaded graphs using the Girvan-Newman algorithm##############")    

communitiesX = []
communities_generator = community.girvan_newman(GX)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
sorted(map(sorted, next_level_communities))
communitiesX=next_level_communities

plot_aux.plotCommunities(GX,communitiesX,"Girvan-Newman",XarxaNetwork)

communitiesZ = []
communities_generator = community.girvan_newman(GZ)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
sorted(map(sorted, next_level_communities))
communitiesZ=next_level_communities

plot_aux.plotCommunities(GZ,communitiesZ,"Girvan-Newman",ZacharyNetwork)

communitiesI = []
communities_generator = community.girvan_newman(GI)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
sorted(map(sorted, next_level_communities))
communitiesI=next_level_communities

plot_aux.plotCommunities(GI,communitiesI,"Girvan-Newman",InfectiousNetwork)



"""b) Compute the communities of the loaded graph using the percolation
    algorithm (see the function k_clique_algorithm in the documentation)
Find communities using the K-Clique  Algorithm"""
print("###Compute the communities of the loaded graph using the percolation algorithms####################################")
print("\n")
print("###Simple graph communities ########################################################################################")
for order in range(3,maxOrderX+1):
  print("\nCommunity detection for cliques of order {} of Simple graph".format(order))
  communitiesX = community.k_clique_communities(GX,order,cliquesX )
  plot_aux.plotCommunities(GX, (list(communitiesX)), "K-Clique",XarxaNetwork)

print("\n")
print("###Zachary graph communities ########################################################################################")

for order in range(3,maxOrderZ+1):
  print("\nCommunity detection for cliques of order {}  of Zachary Network".format(order))
  communitiesZ = community.k_clique_communities(GZ,order,cliquesZ )
  plot_aux.plotCommunities(GZ, (list(communitiesZ)), "K-Clique",ZacharyNetwork)
print("\n")
print("###InfectiousNetwork graph communities #####################################################################################")
  

for order in range(3,maxOrderI+1):
  
  print("\nCommunity detection for cliques of order {} of InfectiousNetwork".format(order))
  communitiesI = community.k_clique_communities(GI,order,cliquesI )
  plot_aux.plotCommunities(GI, (list(communitiesI)), "K-Clique",InfectiousNetwork)



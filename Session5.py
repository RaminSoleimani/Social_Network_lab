# -*- coding: utf-8 -*-
"""
@author: Ramin Soleimani
@email:  ramin.soleimani222@gmail.com
"""""""""
"""Importing Libraries"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from Source import loadDataZachary ,loadDataInfectious
from matplotlib.pyplot import figure

def plotCentralities(G,centralities,socialNetwork):

  numMeasures = len(centralities)
  ax = [0]*numMeasures
  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  pos = nx.spring_layout(G)

  for i, measure in enumerate(centralities):
    ax[i] = plt.subplot(1, numMeasures, i + 1)

    nx.draw(G, pos, with_labels=True, font_weight='bold', font_size=10, font_family='sans-serif', alpha=0.5)
    nx.draw_networkx_nodes(G, pos,
                           nodelist=centralities[measure]['Nodes'],
                           node_color='b',
                           node_size=500,
                           alpha=0.5)
    ax[i].text(0, -0.1, "\n".join(
      ["{}: {}".format(str(u), v) for u, v in zip(centralities[measure]['Nodes'],  ['{:0.2f}'.format(x) for x in centralities[measure]['values']])]),
               transform=ax[i].transAxes, fontsize=8,
               verticalalignment='bottom', bbox=props)
    ax[i].set_title("{}".format(measure))
  plt.suptitle("Centralities measures of {} Network.".format(socialNetwork))
  plt.axis('off')
  fig = plt.gcf()
  fig.set_size_inches(8.27, 4)


  plt.show()
  
  """Exercise1 Download the materials to a local folder, launch your Python IDE and open the SNAActorLevel.py file.
  Set up your project and configure your python interpreter with the required dependencies. For the Zachary network, 
  compute the following centrality measures"""
print("###loading ZacharyData and creating and visualizing its graph###################################")
      
filename="./data/out.ucidata-zachary.txt"

G,socialNetwork=loadDataZachary(filename)

figure(num=None, figsize=(16, 8), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(G, node_color='blue', with_labels=True ,node_size=200)
plt.savefig("Session5 ZacharyGraph.png")
plt.title("ZacharyGraph")
plt.axis('off')
plt.show()

"""Exercisse1 a) Compute the degree centrality."""

print("###Computing Degree Centrality of Zachary network###############################################")
centralities = {}

nodes=nx.degree_centrality(G)

top5Nodes = sorted(nodes.items(), key=lambda kv: kv[1], reverse=True)[:5]

centralities['degree'] = {'Nodes': [x[0] for x in top5Nodes], 'values': [x[1] for x in top5Nodes] }

print('centralities: ',centralities['degree'])

"""Exercise1 b) Compute the eigenvector centrality."""
print("###Computing Eigenvector Centrality of Zachary network###############################################")
nodes=nx.eigenvector_centrality(G)
top5Nodes = sorted(nodes.items(), key=lambda kv: kv[1], reverse=True)[:5]
centralities['eigenvector'] = {'Nodes': [x[0] for x in top5Nodes], 'values':  [x[1] for x in top5Nodes]}
print('centralities: ',centralities['eigenvector'])

"""Exercise1 c) Compute the betweenness centrality."""
print("###Computing Betweenness Centrality of Zachary network###############################################")
  
nodes=nx.betweenness_centrality(G)
top5Nodes = sorted(nodes.items(), key=lambda kv: kv[1], reverse=True)[:5]
centralities['betweenness'] = {'Nodes': [x[0] for x in top5Nodes],
                                 'values':  [x[1] for x in top5Nodes]}
print('centralities: ',centralities['betweenness'])

""""Exercise1 Zachary plot with centralities"""
print("###Zachary plot with centralities###############################################")
plotCentralities(G, centralities, socialNetwork)

"""Exercise 2: Actor level analysis with NetworkX. Download the materials to a local
folder, launch your Python IDE and open the SNAActorLevel.py file. Set up your project
and configure your python interpreter with the required dependencies. For the first hour 
of the Infectious network, compute the following centrality measures to generate a plot
."""


fileName = './data/out.sociopatterns-infectious.txt'
print('File name: ',fileName)

# loading the full data
G,socialNetwork, mintime, maxtime = loadDataInfectious(fileName)
print("Nomber of node is ",len(list(G.nodes)))

"""Exercisse2 a) Compute the degree centrality."""

print("###Computing Degree Centrality of 1st hour of Infectious network###############################################")
centralities = {}

nodes=nx.degree_centrality(G)

top5Nodes = sorted(nodes.items(), key=lambda kv: kv[1], reverse=True)[:5]

centralities['degree'] = {'Nodes': [x[0] for x in top5Nodes], 'values': [x[1] for x in top5Nodes] }

print('centralities: ',centralities['degree'])

"""Exercise2 b) Compute the eigenvector centrality."""
print("###Computing Eigenvector Centrality of 1st hour of Infectious network###############################################")
nodes=nx.eigenvector_centrality(G)
top5Nodes = sorted(nodes.items(), key=lambda kv: kv[1], reverse=True)[:5]
centralities['eigenvector'] = {'Nodes': [x[0] for x in top5Nodes], 'values':  [x[1] for x in top5Nodes]}
print('centralities: ',centralities['eigenvector'])

"""Exercise2 c) Compute the betweenness centrality."""
print("###Computing betweenness Centrality of 1st hour of Infectious network###############################################")

nodes=nx.betweenness_centrality(G)
top5Nodes = sorted(nodes.items(), key=lambda kv: kv[1], reverse=True)[:5]
centralities['betweenness'] = {'Nodes': [x[0] for x in top5Nodes],
                                 'values':  [x[1] for x in top5Nodes]}
print('centralities: ',centralities['betweenness'])

"""Exercise2 1st hour plot of the Infectious network with centralities"""

print("###Zachary plot with centralities###############################################")
plotCentralities(G, centralities, socialNetwork)

"""Exercise3 Degree Centrality computation"""




"""a) Extract the adjacency matrix and store it into a numpy array."""

print("###Extracting adjacency mtrix and storing in numpy matrix##########################")
adjacency=nx.to_numpy_matrix(G)
print(adjacency)

"""b) Obtain the number of nodes. c) Compute the normalized degree centrality."""

print("###Compute the normalized degree centrality. #######################################")


def DegreeCentrality(G):
   
    nodes = G.nodes
    DC=[]
  
    num_nodes=nx.number_of_nodes(G)

    degree_nodes=G.degree(nodes)
   
    degrees = [lis[1] for lis in degree_nodes]

    for i in degrees:
      centrality=degrees[i]/(num_nodes-1)
      DC.append(centrality)

    return {x: v for x, v in zip(nodes, DC)}

dc = DegreeCentrality(G)
    
err = [10]*5
for i, x in enumerate(centralities['degree']['Nodes']):
    err[i] = (dc[int(x)] - centralities['degree']['values'][i])

print("Diffence between the top 5 nodes: {}".format(err))

if max(err) < 1.0e-1:
    test = "OK"
else:
    test = "KO"

print("Degree centrality computation test: {}\n".format(test))

"""Exercise 4: Eigenvector Centrality.
Complete the EigenVectorCentrality function to implement the eigenvector centrality using the formula given in the course slides. Follow these steps:

a) Compute the eigenvalues and eigenvectors of the adjacency matrix.

b) Compute the eigenvector centrality"""
def EigenVectorCentrality(G, max_iter=100, tol=1.0e-6, nstart=None, 
						weight='weight'): 

	from math import sqrt 
	if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph: 
		raise nx.NetworkXException("Not defined for multigraphs.") 

	if len(G) == 0: 
		raise nx.NetworkXException("Empty graph.") 

	if nstart is None: 

		# choose starting vector with entries of 1/len(G) 
		x = dict([(n,1.0/len(G)) for n in G]) 
	else: 
		x = nstart 

	# normalize starting vector 
	s = 1.0/sum(x.values()) 
	for k in x: 
		x[k] *= s 
	nnodes = G.number_of_nodes() 

	# make up to max_iter iterations 
	for i in range(max_iter): 
		xlast = x 
		x = dict.fromkeys(xlast, 0) 

		# do the multiplication y^T = x^T A 
		for n in x: 
			for nbr in G[n]: 
				x[nbr] += xlast[n] * G[n][nbr].get(weight, 1) 

		# normalize vector 
		try: 
			s = 1.0/sqrt(sum(v**2 for v in x.values())) 

		# this should never be zero? 
		except ZeroDivisionError: 
			s = 1.0
		for n in x: 
			x[n] *= s 

		# check convergence 
		err = sum([abs(x[n]-xlast[n]) for n in x]) 
		if err < nnodes*tol: 
			return x 

	raise nx.NetworkXError("""eigenvector_centrality(): 
power iteration failed to converge in %d iterations."%(i+1))""") 
ec = EigenVectorCentrality(G)

err = [10]*5
for i, x in enumerate(centralities['eigenvector']['Nodes']):
    err[i] = (ec[int(x)] - centralities['eigenvector']['values'][i])

print("Diffence between the top 5 nodes: {}".format(err))

if max(err) < 1.0e-1:
    test = "OK"
else:
    test = "KO"

print("Eigenvector centrality computation test: {}\n".format(test))

   




























      
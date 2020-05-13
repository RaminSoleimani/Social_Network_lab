# -*- coding: utf-8 -*-
'''
Created on 26/1/2019

@author: Oriol Ramos Terrades (oriolrt@cvc.uab.cat)
@Institution: Computer Vision Center - Universitat Autonoma de Barcelona

'''


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import sys
import getopt
from datetime import datetime, timedelta

def chunks(l, n):
  """Yield successive n-sized chunks from l."""
  #return [l[i:i + n] for i in range(0, len(l), n)]
  for i in range(0, len(l), n):
    yield l[i:i + n]


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

def plotBiggestClique(G,maximumClique,socialNetwork):

  order = len(maximumClique)

  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  pos = nx.spring_layout(G)

  fig = plt.gcf()
  ax = fig.gca()

  nx.draw(G, pos, with_labels=True, font_weight='bold', font_size=10, font_family='sans-serif', alpha=0.5)
  nx.draw_networkx_nodes(G, pos,
                         nodelist=maximumClique,
                         node_color='b',
                         node_size=500,
                         alpha=0.5)
  ax.text(0, -0.1, "Node labels:" + ", ".join(
    [ str(u) for u in maximumClique ]),
             transform=ax.transAxes, fontsize=8,
             verticalalignment='bottom', bbox=props)
  ax.set_title("Highest order of the network {}:  {}.".format(socialNetwork, order))
  plt.axis('off')
  fig.set_size_inches(4, 4)


  plt.show()

def plotKCores(G,K_cores,socialNetwork):

  sizeKCores = K_cores.number_of_nodes()

  props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
  pos = nx.spring_layout(G)

  fig = plt.gcf()
  ax = fig.gca()

  nx.draw(G, pos, with_labels=True, font_weight='bold', font_size=10, font_family='sans-serif', alpha=0.5)
  nx.draw_networkx_nodes(K_cores, pos,
                         node_color='b',
                         node_size=500,
                         alpha=0.5)
  ax.text(0, -0.1, "Node labels:" + ", ".join(
    [ str(u) for u in list(K_cores.nodes()) ]),
             transform=ax.transAxes, fontsize=8,
             verticalalignment='bottom', bbox=props)
  ax.set_title("Number of nodes in the k_core subgraph of network {}:  {}.".format(socialNetwork, sizeKCores))
  plt.axis('off')
  fig.set_size_inches(4, 4)


  plt.show()

def plotCommunities(G, communities,nameMethod,socialNetwork='Unknown'):

    numCommunities = len(communities)
    ax = [0] * (numCommunities+1)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    pos = nx.spring_layout(G)

    numColumns = 3
    numRows = int(np.ceil((numCommunities +1.0)/numColumns))

    "Plot main grah"
    ax[0] = plt.subplot(numRows, numColumns, 1)
    nx.draw(G, pos, with_labels=True, font_weight='bold', font_size=10, font_family='sans-serif', alpha=0.5)
    ax[0].set_title("Complete network")

    for i, comm in enumerate(communities):
      ax[i+1] = plt.subplot(numRows, numColumns, i + 2)
      sg = nx.Graph.subgraph(G,comm)
      sp = nx.spring_layout(sg)

      nx.draw(sg, sp, with_labels=True, font_weight='bold', font_size=10, font_family='sans-serif', alpha=0.5)


      ax[i+1].text(0, -0.1, "Node labels:\n" + "\n".join([ "{}".format(c) for c in  chunks(list(comm),7) ]),
                 transform=ax[i+1].transAxes, fontsize=8, verticalalignment='bottom', bbox=props)
      ax[i+1].set_title("Community {}".format(i+1))
    plt.suptitle("Communities of {} Network using {} algorithm.".format(socialNetwork,nameMethod))
    plt.axis('off')
    fig = plt.gcf()
    fig.set_size_inches(8.27, 4*numRows)

    plt.show()
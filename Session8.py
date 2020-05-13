# -*- coding: utf-8 -*-
"""
@author: Ramin Soleimani
@email:  ramin.soleimani222@gmail.com
"""""""""
"""Importing Libraries"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

"""Exercise 1: Graph traversal. For each of the following graphs, compute: (a) the DFS
algorithm, (b) the BFS algorithm and (c) the beam search algorithm with width 2 starting
on the orange node. Implement these graphs in your own notebook and apply the
algorithms provided by the network library"""

"""Creating graph a,b and c"""

"""Creating and visualizing Graph a"""
a_edges=[('A','B'),('A','C'),('B','C'),('B','D'),('C','D'),('C','E')]
a_G=nx.Graph()
a_G.add_edges_from(a_edges)
color_map = []
for node in a_G:
    if node =='A':
        color_map.append('red')
    else: 
        color_map.append('green')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(a_G, with_labels=True, node_color=color_map ,node_size=500)


plt.savefig("Session8 Graph a.png")
plt.title("Graph a" , color='blue', fontweight='bold')
plt.show()


"""Creating and visualizing Graph b"""

b_edges=[('A','B'),('A','C'),('B','C'),('C','D'),('D','E'),('D','F'),('E','F')]
b_G=nx.Graph()
b_G.add_edges_from(b_edges)
color_map = []
for node in b_G:
    if node =='C':
        color_map.append('red')
    else: 
        color_map.append('green')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(b_G, with_labels=True, node_color=color_map ,node_size=500)


plt.savefig("Session8 Graph b.png")
plt.title("Graph b" , color='blue', fontweight='bold')
plt.show()

"""Creating and visualizing Graph c"""

c_edges=[('A','B'),('B','C'),('C','D'),('D','E')]
c_G=nx.Graph()
c_G.add_edges_from(c_edges)
color_map = []
for node in c_G:
    if node =='B':
        color_map.append('red')
    else: 
        color_map.append('green')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(c_G, with_labels=True, node_color=color_map ,node_size=500)


plt.savefig("Session8 Graph c.png")
plt.title("Graph c" , color='blue', fontweight='bold')
plt.show()

""" Exercise1 (a) the DFS algorithm"""
print("\n###DFS algorithm data and visualization of Graph a ###################")
Tree=nx.dfs_tree(a_G,'A')
print(list(Tree))
print(list(Tree.edges()))
color_map=[]
for node in Tree:
    if node =='A':
        color_map.append('red')
    else: 
        color_map.append('green')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(Tree, with_labels=True, node_color=color_map,node_size=500)


plt.savefig("Session8 Graph a dfs.png")
plt.title("Graph a DFS algorithm" , color='blue', fontweight='bold')
plt.show()

print("\n###DFS algorithm data and visualization of Graph b ###################")
Tree=nx.dfs_tree(b_G,'C')
print(list(Tree))
print(list(Tree.edges()))
color_map=[]
for node in Tree:
    if node =='C':
        color_map.append('red')
    else: 
        color_map.append('green')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(Tree, with_labels=True, node_color=color_map,node_size=500)


plt.savefig("Session8 Graph b dfs.png")
plt.title("Graph B DFS algorithm" , color='blue', fontweight='bold')
plt.show()

print("\n###DFS algorithm data and visualization of Graph c ###################")
Tree=nx.dfs_tree(c_G,'B')
print(list(Tree))
print(list(Tree.edges()))
color_map=[]
for node in Tree:
    if node =='B':
        color_map.append('red')
    else: 
        color_map.append('green')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(Tree, with_labels=True, node_color=color_map,node_size=500)


plt.savefig("Session8 Graph c dfs.png")
plt.title("Graph C DFS algorithm" , color='blue', fontweight='bold')
plt.show()

""" Exercise1 (b) the BFS algorithm"""

""" BFS of Graph a"""
print("\n###BFS algorithm data and visualization of Graph a ###################")
Edges_BFS=nx.bfs_edges(a_G,'A')

print("Edges of BFS algorithm obtained by nx.bfs_edges() ", list(Edges_BFS))

Tree=nx.bfs_tree(a_G,'A')
print("Nodes: ",list(Tree))
print("Edges of Tree obtained from algorithm",list(Tree.edges()))
color_map=[]
for node in Tree:
    if node =='A':
        color_map.append('pink')
    else: 
        color_map.append('blue')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(Tree, with_labels=True, node_color=color_map,node_size=500)


plt.savefig("Session8 Graph a BFS.png")
plt.title("Graph a BFS algorithm" , color='blue', fontweight='bold')
plt.show()

Successors=nx.bfs_successors(a_G,'A')
print("Successors: ",dict(Successors))
Predecessors=nx.bfs_predecessors(a_G,'A')
print("Predecessors: ",dict(Predecessors))

""" BFS of Graph b"""
print("\n###BFS algorithm data and visualization of Graph b ###################")
Edges_BFS=nx.bfs_edges(b_G,'C')

print("\nEdges of BFS algorithm obtained by nx.bfs_edges() ", list(Edges_BFS))

Tree=nx.bfs_tree(b_G,'C')
print("Nodes: ",list(Tree))
print("Edges of Tree obtained from algorithm",list(Tree.edges()))
color_map=[]
for node in Tree:
    if node =='C':
        color_map.append('pink')
    else: 
        color_map.append('blue')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(Tree, with_labels=True, node_color=color_map,node_size=500)


plt.savefig("Session8 Graph b BFS.png")
plt.title("Graph b BFS algorithm" , color='blue', fontweight='bold')
plt.show()

Successors=nx.bfs_successors(b_G,'C')
print("Successors: ",dict(Successors))
Predecessors=nx.bfs_predecessors(b_G,'C')
print("Predecessors: ",dict(Predecessors))


""" BFS of Graph c"""
print("\n###BFS algorithm data and visualization of Graph c ###################")
Edges_BFS=nx.bfs_edges(c_G,'B')

print("\nEdges of BFS algorithm obtained by nx.bfs_edges() ", list(Edges_BFS))

Tree=nx.bfs_tree(c_G,'B')
print("Nodes: ",list(Tree))
print("Edges of Tree obtained from algorithm",list(Tree.edges()))
color_map=[]
for node in Tree:
    if node =='B':
        color_map.append('pink')
    else: 
        color_map.append('blue')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(Tree, with_labels=True, node_color=color_map,node_size=500)


plt.savefig("Session8 Graph c BFS.png")
plt.title("Graph c BFS algorithm" , color='blue', fontweight='bold')
plt.show()

Successors=nx.bfs_successors(c_G,'B')
print("Successors: ",dict(Successors))
Predecessors=nx.bfs_predecessors(c_G,'B')
print("Predecessors: ",dict(Predecessors))

""" Beam seach algorithm  of Graph a with the width=2"""
print("###Grapg info and result of beam search of graph a############################")
print(nx.info(a_G))
eigen_centra=nx.eigenvector_centrality(a_G)
source = 'A'
width = 2
bfs_beam_edges=nx.bfs_beam_edges(a_G, source, eigen_centra.get, width)
beam_graph=nx.DiGraph()
beam_graph.add_edges_from(bfs_beam_edges)
print("\n Beam Search Result: ",list(beam_graph.edges))

color_map=[]
for node in beam_graph:
    if node =='A':
        color_map.append('pink')
    else: 
        color_map.append('blue')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(beam_graph, with_labels=True, node_color=color_map,node_size=500)


plt.savefig("Session8 Graph a BFS_BeamSearch.png")
plt.title("Graph a BFS_BeamSearch" , color='blue', fontweight='bold')
plt.show()
""""""

""" Beam seach algorithm  of Graph b with the width=2"""
print("###Grapg info and result of beam search of graph a############################")
print(nx.info(b_G))
eigen_centra=nx.eigenvector_centrality(b_G)
source = 'C'
width = 2
bfs_beam_edges=nx.bfs_beam_edges(b_G, source, eigen_centra.get, width)
beam_graph=nx.DiGraph()
beam_graph.add_edges_from(bfs_beam_edges)
print("\n Beam Search Result: ",list(beam_graph.edges))

color_map=[]
for node in beam_graph:
    if node =='C':
        color_map.append('pink')
    else: 
        color_map.append('blue')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(beam_graph, with_labels=True, node_color=color_map,node_size=500)


plt.savefig("Session8 Graph b BFS_BeamSearch.png")
plt.title("Graph b BFS_BeamSearch" , color='blue', fontweight='bold')
plt.show()
""""""
""" Beam seach algorithm  of Graph c with the width=2"""
print("###Grapg info and result of beam search of graph a############################")
print(nx.info(c_G))
eigen_centra=nx.eigenvector_centrality(c_G)
source = 'B'
width = 2
bfs_beam_edges=nx.bfs_beam_edges(c_G, source, eigen_centra.get, width)
beam_graph=nx.DiGraph()
beam_graph.add_edges_from(bfs_beam_edges)
print("\n Beam Search Result: ",list(beam_graph.edges))

color_map=[]
for node in beam_graph:
    if node =='B':
        color_map.append('pink')
    else: 
        color_map.append('blue')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(beam_graph, with_labels=True, node_color=color_map,node_size=500)


plt.savefig("Session8 Graph c BFS_BeamSearch.png")
plt.title("Graph c BFS_BeamSearch" , color='blue', fontweight='bold')
plt.show()


"""Exercise 2: Dijktra’s algorithm. For each of the following graphs, compute the sortest
path from the orange node to the green node. Implement these graphs in your own
notebook and apply the algorithms provided by the network library."""

"""adding weights and visualizing graph"""

"""graph a"""
print("###Adding weights and visualizing graphs################")

attrs = {('A', 'B'): {'weight': 1.1},('A', 'C'): {'weight': 0.1}, ('B', 'C'): {'weight': 0.5}, 
('B', 'D'): {'weight': 0.2}, ('C', 'D'): {'weight': 0.8}, ('C', 'E'): {'weight': 1.5}}

nx.set_edge_attributes(a_G, attrs)

color_map=[]
for node in a_G:
    if node =='A':
        color_map.append('orange')
    elif node =='D':
        color_map.append('green')
    else: 
        color_map.append('blue')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)


attributes = nx.get_edge_attributes(a_G,'weight')
pos = nx.layout.spring_layout(a_G)

nx.draw(a_G,pos, with_labels=True ,node_color=color_map,node_size=500)
nx.draw_networkx_edge_labels(a_G,pos,edge_labels=attributes)
edges = nx.draw_networkx_edges(a_G,pos,  width=2)


plt.savefig("Session8 Graph a weighted graph.png")
plt.title("Graph a weighted graph" , color='blue', fontweight='bold')
plt.show()

"""graph b"""
attrs = {('A', 'B'): {'weight': 0.1},('A', 'C'): {'weight': 0.4}, ('B', 'C'): {'weight': 0.3}, 
('C', 'D'): {'weight': 1.5}, ('D', 'E'): {'weight': 1.6}, ('D', 'F'): {'weight': 0.2},('E', 'F'): {'weight': 0.1}}

nx.set_edge_attributes(b_G, attrs)

color_map=[]
for node in b_G:
    if node =='C':
        color_map.append('orange')
    elif node =='F':
        color_map.append('green')
    else: 
        color_map.append('blue')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)


attributes = nx.get_edge_attributes(b_G,'weight')
pos = nx.layout.spring_layout(b_G)

nx.draw(b_G,pos, with_labels=True ,node_color=color_map,node_size=500)
nx.draw_networkx_edge_labels(b_G,pos,edge_labels=attributes)
edges = nx.draw_networkx_edges(b_G,pos,  width=2)


plt.savefig("Session8 Graph b weighted graph.png")
plt.title("Graph b weighted graph" , color='blue', fontweight='bold')
plt.show()

"""graph c"""


c_G.remove_edges_from([('D','E')])
c_G.add_node('E')
attrs = {('A', 'B'): {'weight': 0.4},('B', 'C'): {'weight': 0.1}, ('C', 'D'): {'weight': 1.6}}


nx.set_edge_attributes(c_G, attrs)

color_map=[]
for node in c_G:
    if node =='B':
        color_map.append('orange')
    elif node =='E':
        color_map.append('green')
    else: 
        color_map.append('blue')
figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)


attributes = nx.get_edge_attributes(c_G,'weight')
pos = nx.layout.spring_layout(c_G)

nx.draw(c_G,pos, with_labels=True ,node_color=color_map,node_size=500)
nx.draw_networkx_edge_labels(c_G,pos,edge_labels=attributes)
edges = nx.draw_networkx_edges(c_G,pos,  width=2)


plt.savefig("Session8 Graph c weighted graph.png")
plt.title("Graph c weighted graph" , color='blue', fontweight='bold')
plt.show()

"""Dijktra’s algorithm. For each of the following graphs, compute the sortest path
 from the orange node to the green node.
 Implement these graphs in your own notebook and apply the algorithms provided by the network library"""
 
""""Graph a shortest path colculations"""




print("### colculation of shortest path fram node A to D in Graph a")
print("shortest path excluding edge weights",nx.shortest_path(a_G,'A','D'))
print("shortest  path excluding length ",nx.shortest_path_length(a_G,'A','D'))
print("shortest  path applying edge weights  ",nx.shortest_path(a_G,'A','D',weight='weight'))
print("shortest  path length applying edge weights",nx.shortest_path_length(a_G,'A','D',weight='weight'))
print("All pairs",dict(nx.all_pairs_shortest_path(a_G)))
print(f"Dijkstra algorithm obtained result: {nx.dijkstra_path(a_G,'A','D')}")
print("diamete fo graph a",nx.diameter(a_G))
print("Eccentricity",nx.eccentricity(a_G))


""""Graph b shortest path colculations"""




print("### colculation of shortest path fram node C to F in Graph b")
print("shortest path",nx.shortest_path(b_G,'C','F'))
print("shortest  path length",nx.shortest_path_length(b_G,'C','F'))
print("shortest  path applying edge weights  ",nx.shortest_path(b_G,'C','F',weight='weight'))
print("shortest  path length applying edge weights",nx.shortest_path_length(b_G,'C','F',weight='weight'))
print("All pairs",dict(nx.all_pairs_shortest_path(b_G)))
print(f"Dijkstra algorithm obtained result: {nx.dijkstra_path(b_G,'C','F')}")
print("diameter of graph b",nx.diameter(b_G))
print("Eccentricity of graph b",nx.eccentricity(b_G))


""""Graph c shortest path colculations"""




#print("### colculation of shortest path fram node B to E in Graph c")
#print("shortest path",nx.shortest_path(c_G,'B','E'))
#print("shortest  path lenght",nx.shortest_path_length(c_G,'B','E'))
#print("shortest  path applying edge weights  ",nx.shortest_path(c_G,'B','E',weight='weight'))
#print("shortest  path lenght applying edge weights",nx.shortest_path_length(c_G,'B','E',weight='weight'))
#print("All pairs",dict(nx.all_pairs_shortest_path(c_G)))
#print(f"Dijkstra algorithm obtained result: {nx.dijkstra_path(c_G,'B','E')}")
#print("diameter of graph b",nx.diameter(c_G))
#print("Eccentricity of graph b",nx.eccentricity(c_G))




#print("*********************************EX 2 c********************************")
#
#"c)"
#
#
#color_map = []
#for node in g2c:
#    if node =='b':
#        color_map.append('blue')
#    elif node =='e':
#        color_map.append('red')
#    else: 
#        color_map.append('orange') 
#        
#fig1 = plt.figure()
#ax1 = fig1.add_subplot(111,aspect='equal')
#labels = nx.get_edge_attributes(g2c,'weight')
#pos = nx.layout.spring_layout(g2c)
#nx.draw(g2c,pos, with_labels=True, font_weight='bold', node_color=color_map,node_size=500 )
#nx.draw_networkx_edge_labels(g2c,pos,edge_labels=labels)
#edges = nx.draw_networkx_edges(g2c, pos,  width=2)
#plt.title("Ex2 Graph c")
#plt.show()
#
#
#print("shortest path",nx.shortest_path(g2b,'c','f'))
#print("shortest path lenght",nx.shortest_path_length(g2b,'c','f'))
#
#print("shortest path 2",nx.shortest_path(g2b,'c','f',weight='weight'))
#print("shortest path lenght 2",nx.shortest_path_length(g2b,'c','f',weight='weight'))
#
#print("All Pairs",dict(nx.all_pairs_shortest_path(g2b)))
#
## alternatively: dijkstra_path
#print(f"Dijkstra: {nx.dijkstra_path(g2b,'c','f')}")
#
## Mesures sobre el graf
#print("Diameter",nx.diameter(g2b))
#print("eccentricity",nx.eccentricity(g2b))
























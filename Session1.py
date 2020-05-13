# -*- coding: utf-8 -*-
"""

Created on Sun May 10 16:35:16 2020

@author: Ramin Soleimani
@email:  ramin.soleimani222@gmail.com
"""""""""
#####Importing Libraries
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure







"""a) Based on the provided code, create a new graph with nodes and edges. Use the data 
used to create your Ego network. Visualize the graph in a subplot."""

G=nx.Graph()         ##  creating an empty graph
family=["Abbas","Jawaher","Reza","Ramyar","Shadi","Ramin"]  ## list of family members  
friends=["Mohak", "Albert", "Miki","Rogi", "Sirvan", "Shaho","Arsalan", "Aitor","Roger","Julio","Adele"]

G.add_nodes_from(family)
G.add_nodes_from(friends)
family_edges=[("Ramin", "Abbas"),("Ramin", "Jawaher"),("Ramin","Reza"),("Ramin","Ramyar"),("Ramin","Shadi")]
friends_edge=[("Ramin", "Mohak"),("Ramin", "Albert"),("Ramin","Miki"),("Ramin","Sirvan"),("Ramin","Shaho")
,("Ramin","Arsalan"),("Ramin","Aitor"),("Ramin","Julio"),
("Ramin","Adele"),("Ramin","Rogi"),("Ramin","Arsalan"),("Ramin","Roger"),("Ramin","Loan")]

G.add_edges_from(family_edges)
G.add_edges_from(friends_edge)

"""Visualizing Graph"""
figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold',
        node_color='blue', edge_color='red',title="Ramin Ego Network" )
plt.savefig("Session1 RaminUndirectedEgo.png")
plt.title("Ramin Ego Network", color='blue', fontweight='bold')
plt.show()





"""b) The same as before but create a directed graph (digraph)"""


GD=nx.DiGraph()
GD.add_edges_from(family_edges)
GD.add_edges_from(friends_edge)

"""Visualizing Graph"""
figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(GD, with_labels=True, font_weight='bold', node_color='red',edge_color='blue' )
plt.savefig("Session1 RaminDirectedEgo.png")
plt.title("Ramin Directed Ego Network" , color='blue', fontweight='bold')
plt.show()


"""c) Add attributes at node and edge level. Visualize it."""
"""adding two attributes to edges"""
print("Undirected graph:")
"""Position attribut"""
pos = { "Ramin":[10,0],"Jawaher":[0,-1],"Shadi":[1,20]}
age= {"Ramin":30, "Jawaher":58,"Shadi":26,"Sirvan":32}

nx.set_node_attributes(G, pos, 'position')
nx.set_node_attributes(G, age, 'age')

print("\n ########")
print('Position: ',nx.get_node_attributes(G,'position'))

print("\n ########")
print('Age', nx.get_node_attributes(G,'age'))

""""printing node positions in spring layout visualization"""
print("printing node positions in spring layout visualization")
pos = nx.layout.spring_layout(G)
print(pos)

"""Adding edge attributes and visualizing graph with labels"""

G.add_edge("Ramin","Abbas",relaciones="Dad")
G.add_edge("Ramin","Shadi",relaciones="Partner")
G.add_edge("Ramin","Sirvan",relaciones="friend")
G.add_edge("Ramin","Adele",relaciones="friend")
pos=nx.get_node_attributes(G,'pos')
print('positions: ', pos)
labels = nx.get_edge_attributes(G,'relaciones')
print("labels: ", labels)
pos = nx.layout.spring_layout(G)

figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_color='blue' ,node_size=500)

nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
edges = nx.draw_networkx_edges(G, pos,  width=2)
plt.savefig("Session1 RaminEgoNetworkWithLabels.png")
plt.title("Ramin Ego Network with labels" , color='blue', fontweight='bold')
plt.show()

"""Exercise 2: Adjacency Matrix.
Using the graphs from the previous exercise:
a) Extract the adjacency matrix of the undirected graph. Is it symmetric?
"""
print("#########adjacency matrix of graph G######################")
adj = nx.adjacency_matrix(G, nodelist=None)
print(adj)

print("#########partial adjacency matrix of graph G######################")
adj = nx.adjacency_matrix(G, nodelist=["Ramin","Mohak","Sirvan"])
print(adj)
np.array(adj)

print("#########Converting ajacency matrix to numpy matrix and showing matrix of several modes######################")
adj = nx.to_numpy_matrix(G, nodelist=["Ramin", "Mohak","Sirvan"])
print(adj)

print("###########Extract the adjacency matrix of the directed graph######")
adj = nx.to_numpy_matrix(GD, nodelist=["Ramin", "Mohak","Sirvan"])
print(adj)

print("######Extract node information and create a matrix with all the gathered data#####")
Height= {"Ramin":185, "Jawaher":155,"Shadi":170,"Sirvan":175}

nx.set_node_attributes(G, Height, 'Height')
      
agedic=nx.get_node_attributes(G,'Height')
data = list(dict. items(agedic))
an_array = np. array(data)
print(an_array)

print("######Extract the edges information and create a numpy matrix with all the gathered data#####")
edge_aver_conversation_duration={("Ramin","Shadi"):55,("Ramin","Mikey"):5,("Ramin", "Jawaher"):15,("Ramin","Adele"):25}
nx.set_edge_attributes(G, edge_aver_conversation_duration, 'AveCon')
AveCon=nx.get_edge_attributes(G, 'AveCon')
data = list(dict. items(AveCon))
an_array = np. array(data)
print(an_array)


print("##Compile the ego networks created by your classmates and generate a complete social network. Think about how to define the ties between you##")
Albert_ego=[("Albert", "Mohak"),("Albert", "Ramin"),("Albert","Miki"),("Albert","Andera"),("Albert","Lamia")
,("Albert","Aitor"),("Albert","Julio"),
("Albert","Adele"),("Albert","Rogi"),("Albert","Jordi"),("Albert","Roger"),("Albert","Loan")]
Loan_ego=[("Loan", "Mohak"),("Loan", "Ramin"),("Loan","Miki"),("Loan","Aura"),("Loan","Chau")
,("Loan","Aitor"),("Loan","Julio"),
("Loan","Mikel"),("Loan","Rogi"),("Loan","Javior"),("Loan","Roger"),("Loan","Albert"),("Loan","Sahar")]
Aitor_ego=[("Aitor", "Mohak"),("Aitor", "Ramin"),("Aitor","Miki"),("Aitor","Viktoria"),("Aitor","Alfredo")
,("Aitor","Loan"),("Aitor","Julio"),
("Aitor","Mikel"),("Aitor","Rogi"),("Aitor","Augusto"),("Aitor","Roger"),("Aitor","Albert")]


G_AL=nx.Graph()
G_AL.add_edges_from(Albert_ego)
G_Lo=nx.Graph()
G_Lo.add_edges_from(Loan_ego)

Ai_ego=nx.Graph()
Ai_ego.add_edges_from(Aitor_ego)

G_Ra_Al=nx.compose(G,G_AL)

G_RA_Al_Lo=nx.compose(G_Ra_Al,G_Lo)

G_RA_Al_Lo_Ai=nx.compose(G_RA_Al_Lo,Ai_ego)
G_RA_Al_Lo_Ai.edges()

figure(num=None, figsize=(20, 20), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)
color_map = []
#edge_color=[]
#for node1 in G_RA_Al_Lo_Ai:
#    for node2 in G_RA_Al_Lo_Ai:
#      if node2  in["Ramin","Albert","Aitor","Loan"]:
#          if node1  in["Ramin","Albert","Aitor","Loan"]:
#              G_RA_Al_Lo_Ai.add_edge(node1,node2,color='r',width=8)
#              edge_color.append("blue")
#      else:
#          edge_color.append("blue")
    
for node in G_RA_Al_Lo_Ai:
   if node in ["Ramin","Albert","Aitor","Loan" ] :
     color_map.append('blue')
   else: 
     color_map.append('green')



nx.draw(G_RA_Al_Lo_Ai, node_color=color_map,with_labels=True,font_size=16 ,node_size=500)


plt.savefig("Session1 EgoNetworksAndCompleteGraph.png")
plt.title("Classmate Complete Ego Network" , color='blue', fontweight='bold')
plt.show()

print("####Download the file Xarxa1.txt from the Virtual Campus and copy it to your Python project. Create a Python script able to load a graph from a file###")

f = open('./data/Xarxa1.txt')
#.rstrip("\n")
line = f.readline().rstrip("\n")
Xar_G=nx.Graph()
while line:
  "TODO: Exercise 1a. read each line of the file and parse its contents to create the graph"
  ls =line.split('\t')
  line = f.readline().rstrip("\n")
  if ls[0]!="":
     Xar_G.add_edge(int(ls[0]),int(ls[1]))
##print(Xar_G.edges) 
f.close()
figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(121)


nx.draw(Xar_G, node_color='blue', with_labels=True ,node_size=500)

plt.savefig("Session1 XarxaGraph.png")
plt.title("Xarxa Graph" , color='blue', fontweight='bold')
plt.show()







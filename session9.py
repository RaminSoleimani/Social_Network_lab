import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
from Session1 import G_RA_Al_Lo_Ai


###################Exercise 1: Information retrieval.#################

"""a) Review the features defined for each node and consider adding at least 4
meaningful features/attributes for each of them. These features can be different
from nodes to nodes. Justify a bit the choice done"""
G=G_RA_Al_Lo_Ai
print(G_RA_Al_Lo_Ai.nodes(data=True))
print(len(G.nodes()))
attrs = {'Abbas': {'age': 59, 'gender':'male', 'salary':2000, 'education':'average'},
         'Jawaher': {'age': 54, 'gender':'female', 'salary':0, 'education':'good'},
         'Reza': {'age': 36, 'gender':'male', 'salary':2200, 'education':'good'},
         'Ramyar': {'age': 26, 'gender':'male', 'salary':700, 'education':'good'},
         'Shadi': {'age': 26, 'gender':'female', 'salary':655, 'education':'very good'},
         'Ramin': {'age': 33, 'gender':'male', 'salary':1800, 'education':'very good'},
         'Mohak': {'age': 33, 'gender':'male', 'salary':1900, 'education':'very good'},
         'Albert': {'age': 29, 'gender':'male', 'salary':1900, 'education':'very good'},
         'Miki': {'age': 28, 'gender':'male', 'salary':900, 'education':'very good'},
         'Sirvan': {'age': 32, 'gender':'male', 'salary':2200, 'education':'good'},
         'Shaho': {'age': 35, 'gender':'male', 'salary':10000, 'education':'exellent'},
         'Arsalan': {'age': 33, 'gender':'male', 'salary':3000, 'education':'very good'},
         'Aitor': {'age': 24, 'gender':'male', 'salary':1700, 'education':'very good'},
         'Roger': {'age': 25, 'gender':'male', 'salary':2100, 'education':'very good'},
         'Julio': {'age': 40, 'gender':'male', 'salary':3500, 'education':'good'},
         'Adele': {'age': 25, 'gender':'transgender', 'salary':1500, 'education':'average'},
         'Loan': {'age': 32, 'gender':'female', 'salary':1400, 'education':'very good'},
         'Aura': {'age': 36, 'gender':'female', 'salary':3200, 'education':'exellent'},
         'Chau': {'age': 27, 'gender':'female', 'salary':900, 'education':'low'},
         'Andera': {'age': 27, 'gender':'transgender', 'salary':1100, 'education':'average'},
         'Lamia': {'age': 28, 'gender':'female', 'salary':1400, 'education':'exellent'},
         'Jordi': {'age': 58, 'gender':'male', 'salary':11000, 'education':'exellent'},
         'Mikel': {'age': 42, 'gender':'male', 'salary':2800, 'education':'average'},
         'Sahar': {'age': 35, 'gender':'female', 'salary':800, 'education':'good'},
         'Viktoria': {'age': 23, 'gender':'female', 'salary':2200, 'education':'good'},
         'Alfredo': {'age': 36, 'gender':'male', 'salary':2400, 'education':'good'},
         'Augusto': {'age': 33, 'gender':'male', 'salary':0, 'education':'low'},
         'Javior': {'age': 39, 'gender':'male', 'salary':2200, 'education':'good'},
         'Rogi': {'age': 34, 'gender':'female', 'salary':900, 'education':'good'},
         
         }

nx.set_node_attributes(G, attrs)
print(G.nodes(data=True))
print(len(G))
 


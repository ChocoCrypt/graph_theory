import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.Graph()

tuplas = []
#labels = {}
for i in range(0,11):
    tuplas.append( (i, i+1)  )
#    labels[i] = str(i) + "gonorrea"

tuplas.append((0,10))
tuplas.append(("jaja","jiji"))


G.add_edges_from(tuplas)

chaman_shortest_path = nx.shortest_path( G ,1 ,11 )
print(chaman_shortest_path)


options = {"node_size": 500, "alpha": 1.0}
pos = nx.spring_layout(G)  # positions for all nodes


#nx.draw(G, cmap = plt.get_cmap('jet'), node_color = 'r' ,  font_size = 10)
#nx.draw_networkx_labels(G, pos, labels, font_size=16)
nx.draw_networkx(G, pos , node_color = "r"  )
plt.show()
nx.draw_networkx(G, pos , node_color = "r" , nodelist = chaman_shortest_path)
plt.show()

import networkx as nx
import json
import numpy as np
import matplotlib.pyplot as plt

def get_nombre_banda(id_banda):
    for i in datos['nodes']:
        if(i['id'] == id_banda):
            return(i['nombre'])

path = "/home/r/Semestre2020-2/nod32/relaciones/PielCamaleón_r3.json"
with open (path) as json_file:
    datos = json.load(json_file)


id_artista1 = '3aeY1LxKK63GRg7tmI8UVa'
id_artista2 = '5n4mCk6ZQoWaUHjicvR6vO'
print(get_nombre_banda(id_artista1))


tuplas = []
for i in datos['links']:
    source = i['source']
    target = i['target']
    tuplas.append((source,target))

G = nx.Graph()
G.add_edges_from(tuplas)

try:
    chaman_shortest_path = nx.shortest_path( G ,id_artista1 ,id_artista2)
    #print(chaman_shortest_path)
    lista_nombres = []
    for i in chaman_shortest_path:
        for j in datos['nodes']:
            if(j['id'] == i):
#                print(j['nombre'])
                lista_nombres.append(j['nombre'])
    print(lista_nombres)
except:
    pass



options = {"node_size": 500, "alpha": 1.0}
pos = nx.spring_layout(G)  # positions for all nodes


#nx.draw(G, cmap = plt.get_cmap('jet'), node_color = 'r' ,  font_size = 10)
#nx.draw_networkx_labels(G, pos, labels, font_size=16)






            #Parte grafica:   |mar oct 27 22:20:20 -05 2020|




#nx.draw_networkx(G, pos , node_color = "r"  , font_size = 8)
#plt.savefig("grafo_madonna.png")
#plt.show()

#esto dibuja el path mas corto   |mar oct 27 21:43:34 -05 2020|
#try:
#    nx.draw_networkx(G, pos , node_color = "r" , nodelist = chaman_shortest_path)
#    plt.show()
#except:
#    print("no imprimo nada porque el shortest path no existe")

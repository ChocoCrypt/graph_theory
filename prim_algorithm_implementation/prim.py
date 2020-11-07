#Rodrigo castillo
#para hacer este trabajo me basé en el trabajo de kylekizirian en su github
from queue import PriorityQueue
from random import randint, uniform
import networkx as nx
from matplotlib import animation, rc
import matplotlib.pyplot as plt

rc('animation', html='html5')

#Aca defino el grafo   |vie nov  6 13:05:11 -05 2020|

#el numero de nodos del grafo aleatorio   |vie nov  6 13:33:12 -05 2020|
NUM_NODES = 50

def random_node():
    return randint(0, NUM_NODES-1)

def random_weight():
    return randint(0, 10)



#aca definoe l grafo usando la libreria de networkx(que es una chimba de librería para grafos)   |vie nov  6 13:05:58 -05 2020|
#soy consciente de que el grafo aleatorio se puede definir en esta librería pero pues igual severo   |vie nov  6 13:06:25 -05 2020|
#el grafo también puede definirse como un digrafo   |vie nov  6 13:06:44 -05 2020|
print("creating graph...")
graph = nx.Graph()

#a todos los nodos que creé les pongo un peso aleatorio con eso el algoritmo funciona, sin embargo podría definir otro grafo de otra manera o simplementa llamar un archivo json predefinido   |vie nov  6 13:19:25 -05 2020|
for i in range(1, NUM_NODES):
    graph.add_edge(i-1, i, weight=random_weight())

#genero las aristas aleatorias    |vie nov  6 15:23:24 -05 2020|
for _ in range(NUM_NODES * 5):
    graph.add_edge(
        random_node(), random_node(), weight=random_weight()
    )

pos = nx.random_layout(graph)



#defino las tuplas para insertar en el grafo y para poner en la grafica la cual luego animare   |vie nov  6 13:18:11 -05 2020|
all_edges = set(
    tuple(sorted((n1, n2))) for n1, n2 in graph.edges()
)
edges_in_mst = set()
nodes_on_mst = set()

fig, ax = plt.subplots(figsize=(6,4))





#Tarea: Algoritmo de prim   |vie nov  6 13:08:20 -05 2020|
def prims():
    print("prim...")
    pqueue = PriorityQueue()
    #agarro un nodo aleatorio para empezar   |vie nov  6 13:22:28 -05 2020|
    start_node = random_node()
    for neighbor in graph.neighbors(start_node):
        edge_data = graph.get_edge_data(start_node, neighbor)
        edge_weight = edge_data["weight"]
        pqueue.put((edge_weight, (start_node, neighbor)))

    #bucle hasta que todos los nodos están en el arbol de expansión mínima   |vie nov  6 13:23:16 -05 2020|
    while len(nodes_on_mst) < NUM_NODES:
        #agarro todos los nodos con menor peso del priority queue   |vie nov  6 13:23:46 -05 2020|
        _, edge = pqueue.get(pqueue)

        if edge[0] not in nodes_on_mst:
            new_node = edge[0]
        elif edge[1] not in nodes_on_mst:
            new_node = edge[1]
        else:
            #si la arista conecta dos nodos que ya estan en el arbol de expansion minima pues pailas   |vie nov  6 13:24:09 -05 2020|
            continue

        #cada vez que agrega un nodo al priority queue agrega las aristas en el priority queue   |vie nov  6 13:24:47 -05 2020|
        for neighbor in graph.neighbors(new_node):
            edge_data = graph.get_edge_data(new_node, neighbor)
            edge_weight = edge_data["weight"]
            pqueue.put((edge_weight, (new_node, neighbor)))

        #agrego este nodo al arbol de expansion minima   |vie nov  6 13:25:24 -05 2020|
        edges_in_mst.add(tuple(sorted(edge)))
        nodes_on_mst.add(new_node)

        #retorno los nodos en el arbol de expansion minima que luego voy a usar para imprimirlo(aunque hasta aca melo)   |vie nov  6 13:25:43 -05 2020|
        yield edges_in_mst



#esto es para dibujar el arbol de expansion minima   |vie nov  6 13:16:29 -05 2020|
def update(mst_edges):
    ax.clear()
    nx.draw_networkx_nodes(graph, pos, node_size=25, ax=ax)
    nx.draw_networkx_edges(
        graph, pos, edgelist=all_edges-mst_edges, alpha=0.1,
        edge_color='g', width=1, ax=ax
    )
    nx.draw_networkx_edges(
        graph, pos, edgelist=mst_edges, alpha=1.0,
        edge_color='b', width=1, ax=ax
    )

def do_nothing():
    #esta vuelta es necesaria para la animacion   |vie nov  6 13:13:57 -05 2020|
    pass



#configuracion de la animacion del algoritmo de prim   |vie nov  6 13:11:05 -05 2020|
ani = animation.FuncAnimation(
    fig,
    update,
    init_func=do_nothing,
    frames=prims,
    interval=500,
)

#llamo la animacion   |vie nov  6 13:16:09 -05 2020|
ani

plt.show()
print('Listos, el arbol de expansión mínima del grafo ya está completo')
print("guardando...")
ani.save("ultima_animacion.mp4")

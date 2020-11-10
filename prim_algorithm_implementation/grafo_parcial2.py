from queue import PriorityQueue
from random import randint, uniform
import networkx as nx
from matplotlib import animation, rc
import matplotlib.pyplot as plt




NUM_NODES =28
rc('animation', html='html5')


graph = nx.Graph()
#Lineas horizontales   |mar nov 10 10:53:16 -05 2020|
graph.add_edge('a','b' , weight=1)
graph.add_edge('b','c' , weight=2)
graph.add_edge('c','d' , weight=1)

graph.add_edge('e','f' , weight=2)
graph.add_edge('f','g' , weight=3)
graph.add_edge('g','h' , weight=2)

graph.add_edge('i','j' , weight=3)
graph.add_edge('j','k' , weight=4)
graph.add_edge('k','l' , weight=3)

graph.add_edge('m','n' , weight=2)
graph.add_edge('n','o' , weight=2)
graph.add_edge('o','p' , weight=3)

#lineas verticales   |mar nov 10 10:53:24 -05 2020|
graph.add_edge('a','e' , weight=1)
graph.add_edge('e','i' , weight=2)
graph.add_edge('i','m' , weight=3)

graph.add_edge('b','f' , weight=3)
graph.add_edge('f','j' , weight=3)
graph.add_edge('j','n' , weight=4)

graph.add_edge('c','g' , weight=3)
graph.add_edge('g','k' , weight=4)
graph.add_edge('k','o' , weight=3)


graph.add_edge('d','h' , weight=1)
graph.add_edge('h','l' , weight=3)
graph.add_edge('l','p' , weight=2)

#lineas por fuera   |mar nov 10 10:58:01 -05 2020|
graph.add_edge('a','m' , weight=2)
graph.add_edge('a','d' , weight=2)
graph.add_edge('d','p' , weight=2)
graph.add_edge('m','p' , weight=2)



#imprmo el grafo del parcial   |mar nov 10 11:09:41 -05 2020|
nx.draw(graph)
plt.show()







all_edges = set(
    tuple(sorted((n1, n2))) for n1, n2 in graph.edges()
)
edges_in_mst = set()
nodes_on_mst = set()
pos = nx.random_layout(graph)
#Tarea: Algoritmo de prim   |vie nov  6 13:08:20 -05 2020|
fig, ax = plt.subplots(figsize=(6,4))
def prims():
    print("prim...")
    pqueue = PriorityQueue()
    #agarro un nodo aleatorio para empezar   |vie nov  6 13:22:28 -05 2020|
    start_node = ('a')
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
cont = 10
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

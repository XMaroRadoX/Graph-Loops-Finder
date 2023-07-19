# app/graph_loops_finder.py
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def read_csv_edges(file_path):
    df = pd.read_csv(file_path)
    return df.values.tolist()

def find_loops_in_graph(edges_list):
    graph = nx.DiGraph()
    graph.add_edges_from(edges_list)
    loops = list(nx.simple_cycles(graph))
    return loops

def draw_graph_with_loops(edges_list, loops):
    graph = nx.DiGraph()
    graph.add_edges_from(edges_list)
    pos = nx.spring_layout(graph, seed=42)
    plt.figure(figsize=(10, 8))
    nx.draw(graph, pos, with_labels=True, node_size=1500, node_color='skyblue', arrowsize=20, font_size=12)
    nx.draw_networkx_edges(graph, pos, edgelist=edges_list, edge_color='gray', arrows=True)
    
    # Highlight loops in red
    loop_edges = [edge for loop in loops for edge in zip(loop, loop[1:] + [loop[0]])]
    nx.draw_networkx_edges(graph, pos, edgelist=loop_edges, edge_color='red', arrows=True)

    plt.show()

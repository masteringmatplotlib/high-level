"""
Note that the code for this module was adapted from the NetworkX example
for the a selection of LANL routes to the Internet:

 * https://networkx.github.io/documentation/latest/examples/drawing/lanl_routes.html

"""
import networkx as nx


def parse_routes_data(filename):
    fh = open(filename, 'r')
    G = nx.Graph()
    times = {}
    times[0] = 0
    for line in fh.readlines():
        (head, tail, rtt) = line.split()
        G.add_edge(int(head), int(tail))
        times[int(head)] = float(rtt)
    return (G, times)


def get_routes_graph(debug=False):
    "Return the lanl internet view graph from lanl.edges"
    (time_graph, times) = parse_routes_data('lanl_routes.edgelist')
    G = sorted(
       nx.connected_component_subgraphs(time_graph),
       key=len,
       reverse=True)[0]
    G.rtt = {}
    for n in G:
        G.rtt[n] = times[n]
    if debug:
        print(("graph has %d nodes with %d edges"
              % (nx.number_of_nodes(time_graph),
                 nx.number_of_edges(time_graph))))
        print(nx.number_connected_components(time_graph),
              "connected components")
    return G

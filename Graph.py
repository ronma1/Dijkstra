import networkx as nx

class Graph:
    
    # Construct graph from file using networkx
    def __init__ (self, *args):
        self.graph = nx.Graph()
        # Open the input file and create the graph from the given data
        with open(args[0], 'r') as input:
            # add range of nodes from 0 to the number of required nodes - 1
            self.graph.add_nodes_from(range(0, int(input.readline()) - 1))

    # Parse single line from file            
    def add_edge_from_line(line):
        pass

if __name__ == '__main__': 
    g = Graph('g0.txt')
    print g.graph.nodes()
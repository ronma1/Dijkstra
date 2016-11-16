import networkx as nx

class Graph:
    
    # Construct graph from file using networkx
    def __init__ (self, *args):
        self.graph = nx.Graph()
        # Open the input file and create the graph from the given data
        with open(args[0], 'r') as input:
            # add range of nodes from 0 to the number of required nodes - 1
            self.nodes = int(input.readline())
            self.edges = int(input.readline())
            self.graph.add_nodes_from(range(0, self.nodes - 1))
            for line in input.readlines():
                self.add_edge_from_line(line)

    # Parse single line from file            
    def add_edge_from_line(self, line):
        parms =line.split()
        self.graph.add_edge(int (parms[0]),int(parms[1]),weight=float(parms[2]))

if __name__ == '__main__': 
    g = Graph('g0.txt')
    print " graph: " + str(g)
    print g.graph.nodes()
    print "\n"
    for edge in g.graph.edges():
        print str(edge[0]) + " " + str(edge[1]) + " " + str(g.graph.get_edge_data(edge[0], edge[1]))
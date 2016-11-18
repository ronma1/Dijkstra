import networkx as nx

class Graph:
    
    # initialize graph instance 
    def __init__ (self, *args):
        self.graph = nx.Graph()
        # Opens the input file and create a graph from given data
        with open(args[0], 'r') as input:
            self.nodes = int(input.readline())
            self.edges = int(input.readline())
            # add range of nodes from 0 to the number of required nodes - 1
            self.graph.add_nodes_from(range(0, self.nodes - 1))
            for line in input.readlines():
                self.add_edge_from_line(line)

    # Parse single line from a file with the following format:
    # params[0] = v1 
    # params[1] = v2
    # params[3] = weight of the edge between v1 & v2. 
    def add_edge_from_line(self, line):
        params =line.split()
        self.graph.add_edge(int (params[0]),int(params[1]),weight=float(params[2]))

# main for tests / should delete it. 
if __name__ == '__main__': 
    g = Graph('g0.txt')
    print g.graph.nodes()
    print "\n"
    for edge in g.graph.edges():
        print str(edge[0]) + " " + str(edge[1]) + " " + str(g.graph.get_edge_data(edge[0], edge[1]))
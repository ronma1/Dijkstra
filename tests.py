import networkx as nx
from graph_algo import Graph_algo

class TestGraph:

    def __init__(self, *args):
        self.graph = nx.Graph()
        with open(args[0], 'r') as input:
           self.numOfQueries = int(input.readline())
           for line in input.readlines():
               self.parseTheLine(line)
            


    def parseTheLine(self, line):
        params = line.split()
        self.graph.add_edge(params[0], params[1])
        self.sizeOfBlackList = params[2]
        self.blackList = []
        for i in range(3,len(params)):
            self.blackList.append(int(params[i]))
        self.weigth = Graph_algo.calc_path_with_blacklist(self, int(params[0]), int(params[1]), self.blackList)
        print self.weigth

        
        
if __name__ == '__main__': 
    g = TestGraph('test.txt')

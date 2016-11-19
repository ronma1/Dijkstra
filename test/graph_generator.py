import networkx as nx
from sys import argv
import random

# a short script made in order to generate graphs for testing purpose
# graphs will be generated using this tool via bash.
# How to use:
# python graph_generator.py file_base_name number_of_graphs
# python graph_generator.py G 100 will create G1.txt , .... , G100.txt
#
# for now graph's size will be automaticlly generated between 100-1000
# This can be changed currently manually via the __main__ . 

global base_name, num_of_graphs

# create the number i graph with a given size
def single_graph_generator(i, size):
	# creates a random graph with the following params:
	# n = number of nodes.
	# p = probabilty for edge between two nodes.
	G = nx.fast_gnp_random_graph(n = size, p = random.random())
	with open(base_name + str(i) + '.txt', 'w') as output:
		output.write(str(G.number_of_nodes()) + '\n')
		output.write(str(G.number_of_edges()) + '\n')
		for edge in G.edges():
			output.write(str(edge[0]) + ' ' + str(edge[1]) + ' ' + str(random.uniform(1, 10)) + '\n')

if __name__ == '__main__': 
		
	base_name = argv[1]
	num_of_graphs = argv[2]

	if base_name is None or num_of_graphs is None:
		raise Exception('Arguments error, please read documentation.')

	num_of_graphs = int(num_of_graphs) # convert form str to int

	for i in range(num_of_graphs):
		single_graph_generator(i, random.randint(100, 1000))
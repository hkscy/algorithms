# Chris Hicks 2020
#
# Uses Depth-First Search (DFS) on a graph to efficiently compute the topoligical sort.
from queue import LifoQueue

# Stores graph using adjacency lists, input a list of edge tuples [('u', 'v'),...]
class Graph:
	def __init__(self, edge_tuples=None):
		
		# High-level pass the edges to build a set of vetcies
		self.edges = edge_tuples
		self.vertices_list = list(set([item for sublist in edge_tuples for item in sublist]))
		self.vertices_dict = dict()
		
		# Second pass to build a list of pointers from each vertex to the incident edges
		for vertex in self.vertices_list:
			edges = []
			for edge in edge_tuples:
				u,w = edge
				if u == vertex:
					edges.append(w)
				elif w == vertex:
					edges.append(u)
			self.vertices_dict.update({vertex: edges})	
		
	def to_string(self):	
		return str(self.vertices_dict)
		
	def n_vertices(self):
		return len(self.vertices_list)
		
	def get_vertices_list(self):
		return self.vertices_list
	
	def get_vertices_dict(self):
		return self.vertices_dict
		
# Depth First Search algorithm.
# Inputs: graph and start vertex label
# Output: True (connected) / False (unconnected) and list of vertices connecting 
#         start_vertex to target_vertex
def dfs(graph, start_vertex, target_vertex):
	vertices = graph.get_vertices_dict()
	# Edge case return False if start or target vertex are absent in graph
	if start_vertex not in vertices or target_vertex not in vertices:
		return False, []
	
	explored = dict(zip(graph.get_vertices_list(), [False for null in range(graph.n_vertices())]))
	
	Q = LifoQueue(maxsize = 0)
	Q.put(start_vertex)
	
	while not Q.empty():
		v = Q.get()
		if explored.get(v) == False:
			explored.update({v:True})
			edges = vertices.get(v)
			for w in edges:
				Q.put(w)
				
	return explored.get(target_vertex), explored

# Recursive Depth First Search algorithm.
# Inputs: graph and start vertex label
# Output: True (connected) / False (unconnected) and list of vertices connecting 
#         start_vertex to target_vertex
def dfs_recursive(graph, start_vertex, target_vertex, explored=None):
	vertices = graph.get_vertices_dict()
	if explored == None:
		explored = dict(zip(graph.get_vertices_list(), [False for null in range(graph.n_vertices())]))
	explored.update({start_vertex:True}) # Mark start_vertex as explored
	edges = vertices.get(start_vertex)
	for w in edges:
		if explored.get(w) == False:
			dfs_recursive(graph, w, target_vertex, explored)
	return explored.get(target_vertex), explored
	
def main():
	# Example undircted graph, specify as a list of edge tuples
	example_graph = [('S', 'A'), ('S', 'B'), ('A', 'B'), ('A', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
	graph = Graph(example_graph)
	
	# Test DFS
	start = 'S'
	target = 'E'
	
	print("Testing DFS using non-recursive method:")
	if dfs(graph, start, target)[0]:
		print('\t{} is connected to {} in graph: {}'.format(start, target, graph.to_string()))
	else:
		print('\t{} is NOT connected to {} in graph: {}'.format(start, target, graph.to_string()))
	
	print("Testing DFS using recursive method:")
	# Test recursive DFS
	if dfs_recursive(graph, start, target)[0]:
		print('\t{} is connected to {} in graph: {}'.format(start, target, graph.to_string()))
	else:
		print('\t{} is NOT connected to {} in graph: {}'.format(start, target, graph.to_string()))
	
if __name__ == "__main__":
	main()

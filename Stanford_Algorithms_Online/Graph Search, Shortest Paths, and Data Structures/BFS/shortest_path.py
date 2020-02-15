# Chris Hicks 2020
#
# Uses Breadth-First Search (BFS) on a graph to efficiently compute the shortest path.
from queue import Queue

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
		
# Breadth First Search algorithm.
# Inputs: graph and start vertex label
# Output: True (connected) / False (unconnected) and list of vertices connecting 
#         start_vertex to target_vertex
def bfs(graph, start_vertex, target_vertex):
	vertices = graph.get_vertices_dict()
	# Edge case return False if start or target vertex are absent in graph
	if start_vertex not in vertices or target_vertex not in vertices:
		return False, []
	
	explored = dict(zip(graph.get_vertices_list(), [False for null in range(graph.n_vertices())]))
	explored.update({start_vertex:True})
	
	Q = Queue(maxsize = 0)
	Q.put(start_vertex)
	
	while not Q.empty():
		v = Q.get()
		edges = vertices.get(v)
		for w in edges:
			if explored.get(w) == False:
				explored.update({w:True})
				Q.put(w)
				
	return explored.get(target_vertex), explored
	
# Breadth First Search algorithm for finding the shortest-path of a graph
# Inputs: graph of nodes and vertices, start vertex and target vertex
# Output: Distance (number of edges) from start_vertex to target_vertex. -1 on error
def shortest_path_bfs(graph, start_vertex, target_vertex):
	vertices = graph.get_vertices_dict()
	# Edge case return False if start or target vertex are absent in graph
	if start_vertex not in vertices or target_vertex not in vertices:
		return -1
		
	explored = dict(zip(graph.get_vertices_list(), [False for null in range(graph.n_vertices())]))
	explored.update({start_vertex:True})
	
	dist = dict(zip(graph.get_vertices_list(), [-1 for null in range(graph.n_vertices())]))
	dist.update({start_vertex:0})
	
	Q = Queue(maxsize = 0)
	Q.put(start_vertex)
	
	while not Q.empty():
		v = Q.get()
		edges = vertices.get(v)
		for w in edges:
			if explored.get(w) == False:
				explored.update({w:True})
				dist.update({w:dist.get(v)+1})
				Q.put(w)
				
	return dist.get(target_vertex)
	
def main():
	# Example undircted graph, specify as a list of edge tuples
	example_graph = [('S', 'A'), ('S', 'B'), ('A', 'B'), ('A', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
	graph = Graph(example_graph)
	
	# Test BFS
	start = 'S'
	target = 'E'
	if bfs(graph, start, target)[0]:
		print('{} is connected to {} in graph: {}'.format(start, target, graph.to_string()))
	else:
		print('{} is NOT connected to {} in graph: {}'.format(start, target, graph.to_string()))
	
	# Test BFS shortest path
	target = 'C'
	dist_target = shortest_path_bfs(graph, start, target)
	print('{} is {} edges from {} in graph: {}'.format(start, dist_target, target, graph.to_string()))
	
if __name__ == "__main__":
	main()

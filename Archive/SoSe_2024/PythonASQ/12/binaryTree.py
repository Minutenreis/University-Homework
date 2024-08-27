import math
import random


class Graph:
    class Node:
        def __init__(self, name, value = 0):
            self._name = name
            self._edges: list[Graph.Node] = []
            self.value = value
                    
        @property
        def name(self):
            return self._name
        
        @property
        def edges(self):
            return self._edges
        
        def deg(self):
            return len(self.edges)
        
        def __repr__(self):
            return f"Node<{self.name}>"
        
    def __init__(self, nodes : list[str] = None):
        self.nodes: dict[str,Graph.Node] = {}
        if nodes is not None:
            if len(nodes) != len(set(nodes)):
                raise ValueError('Knoten doppelt vorhanden')
            for node in nodes:
                self.add_node(node)
        self.num_edges = 0
        self.edge_weights = {}
    
    @property
    def num_nodes(self):
        return len(self.nodes)
    
    def add_node(self, name, value = 0):
        if name in self.nodes:
            raise ValueError('Knoten bereits vorhanden')
        self.nodes[name] = Graph.Node(name, value)
        return self.nodes[name]
    
    def change_name(self, oldName, newName):
        if newName in self.nodes:
            raise ValueError('neuer Name bereits vorhanden')
        try:
            node = self.nodes[oldName]
        except:
            raise ValueError('Knoten nicht vorhanden')
        del self.nodes[oldName]
        node._name = newName
        self.nodes[newName] = node
    
    def remove_node(self, name):
        try:
            node = self.nodes[name]
        except KeyError:
            raise ValueError('Knoten nicht vorhanden')
        del self.nodes[name]
        for n in node.edges:
            n._edges.remove(node)
        self.num_edges -= node.deg()
        
    def add_edge(self, name1: str, name2: str, value = 0):
        try:
            node1 = self.nodes[name1]
            node2 = self.nodes[name2]
        except KeyError:
            raise ValueError('ein Knoten nicht vorhanden')
        if node2 in node1.edges:
            raise ValueError('Kante bereits vorhanden')
        node1._edges.append(node2)
        node2._edges.append(node1)
        self.edge_weights[(name1, name2)] = value
        self.edge_weights[(name2, name1)] = value
        self.num_edges += 1
        
    def remove_edge(self, name1: str, name2: str):
        try:
            node1 = self.nodes[name1]
            node2 = self.nodes[name2]
        except KeyError:
            raise ValueError('ein Knoten nicht vorhanden')
        if node2 not in node1.edges:
            raise ValueError('Kante nicht vorhanden')
        node1._edges.remove(node2)
        node2._edges.remove(node1)
        self.edge_weights.pop((name1, name2))
        self.edge_weights.pop((name2, name1))
        self.num_edges -= 1
        
    def get_edge_weight(self, name1: str, name2: str):
        return self.edge_weights.get((name1, name2), None)
    
    def avg_deg(self):
        return self.num_edges * 2 / self.num_nodes
    
    # could be more efficient if we just keep track of the maximums
    def highest_deg(self):
        nodes:list[Graph.Node] = []
        deg = 0
    
        for node in self.nodes.values():
            if node.deg() > deg:
                nodes = [node]
                deg = node.deg()
            elif node.deg() == deg:
                nodes.append(node)
        return nodes
    
    def lowest_deg(self):
        nodes:list[Graph.Node] = []
        deg = self.num_nodes
    
        for node in self.nodes.values():
            if node.deg() < deg:
                nodes = [node]
                deg = node.deg()
            elif node.deg() == deg:
                nodes.append(node)
        return nodes
    
    def get_Adjazenzmatrix(self):
        matrix = []
        for node in self.nodes.values():
            row = [0] * self.num_nodes
            for edge in node.edges:
                row[list(self.nodes.values()).index(edge)] = 1
            matrix.append(row)
        return matrix
    
    def __add__(self, other):
        if not isinstance(other, Graph):
            raise TypeError('Graph kann nur mit Graph addiert werden')
        result = Graph()
        for node in self.nodes.values():
            result.add_node(node.name)
        for node in other.nodes.values():
            try:
                result.add_node(node.name)
            except:
                continue
        edges = 0
        for node in result.nodes.values():
            for edge in node.edges:
                edges += 1
                result.edge_weights[(node.name, edge.name)] = self.edge_weights.get((node.name, edge.name), other.edge_weights.get((node.name, edge.name)))
        result.num_edges = edges // 2
        
        return result
    
    def __str__(self):
        return str(self.nodes)
    
    def __len__(self):
        return self.num_nodes
    
    def __getitem__(self, key):
        return self.nodes[key]
    
    def __contains__(self, key):
        if isinstance(key, Graph.Node):
            key = key.name
        if isinstance(key,str):
            return key in self.nodes
        if isinstance(key, tuple) or isinstance(key, list):
            if len(key) == 2 and isinstance(key[0], str) and isinstance(key[1], str):
                return key[0] in self.nodes and key[1] in self.nodes and self.nodes[key[0]] in self.nodes[key[1]].edges
            
            #expects a tuple or list of edges [(node1name, node2name), (node2name, node3name), ...]
            for edge in key:
                if not isinstance(edge, tuple) and not isinstance(edge, list):
                    return False
                if len(edge) != 2:
                    return False
                if edge[0] not in self.nodes or edge[1] not in self.nodes:
                    return False
                if self.nodes[edge[0]] not in self.nodes[edge[1]].edges:
                    return False
            return True
        raise ValueError('key must be a string, a Graph.Node or a list of edges')
    
    def bfs(self, value: int ,startNode: Node = None) -> Node:
        if startNode is None:
            startNode = self.nodes[next(iter(self.nodes))]
        queue = [startNode]
        visitedNames = set()
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return node
            visitedNames.add(node.name)
            for edge in node.edges:
                if edge.name not in visitedNames:
                    queue.append(edge)
        return None
    
    def dfs(self, value: int ,startNode: Node = None) -> Node:
        if startNode is None:
            startNode = self.nodes[next(iter(self.nodes))]
        queue = [startNode]
        visitedNames = set()
        while queue:
            node = queue.pop()
            if node.value == value:
                return node
            visitedNames.add(node.name)
            for edge in node.edges:
                if edge.name not in visitedNames:
                    queue.append(edge)
        return None

    def isConnected(self):
        visited = set()
        if not self.nodes:
            raise ValueError('Graph is empty')
        queue = [list(self.nodes.values())[0]]
        while queue:
            node = queue.pop()
            visited.add(node)
            for edge in node.edges:
                if edge not in visited:
                    queue.append(edge)
        return len(visited) == len(self.nodes)

# Meckerbemerkung: es wäre viel sinnvoller gewesen einen Bidirektionalen Graphen
# als Spezialfall eines Gerichteten Graphen zu implementieren
class GerichteterGraph(Graph):
    class GerichteterKnoten(Graph.Node):
        def __init__(self, name):
            super().__init__(name, value = 0)
            self.out_edges = []
            self.in_edges = []
        
        @property
        def name(self):
            return self._name
        
        @property
        def out_edges(self):
            return self._out_edges
        
        @property
        def out_deg(self):
            return len(self.out_edges)
        
        
        def add_out_edge(self, node):
            if node not in self.out_edges:
                self.out_edges.append(node)
                if node not in self._edges:
                    self._edges.append(node)
                node.add_in_edge(self)
        
        def remove_out_edge(self, node):
            if node in self.out_edges:
                self.out_edges.remove(node)
                if node not in self._edges:
                    self._edges.remove(node)
                node.in_edges.remove(self)
        
        @property
        def in_edges(self):
            return self._in_edges
        
        @property
        def in_deg(self):
            return len(self.in_edges)
        
        def add_in_edge(self, node):
            if node not in self.in_edges:
                self.in_edges.append(node)
                if node not in self._edges:
                    self._edges.append(node)
                node.add_out_edge(self)
                
        def remove_in_edge(self, node):
            if node in self.in_edges:
                self.in_edges.remove(node)
                if node not in self._edges:
                    self._edges.remove(node)
                node.out_edges.remove(self)
        
        def __repr__(self):
            return self.name
    
    def __init__(self, nodes : list[str] = None):
        self.nodes: dict[str,GerichteterGraph.GerichteterKnoten] = {}
        super().__init__(nodes)
        # Binärbaum:
        # max 2 Nachfolger
        # 1 Vorgänger außer Wurzel
        self.isBinaryTree = True if self.num_nodes == 1 else False
    
    def add_node(self, name):
        if name in self.nodes:
            raise ValueError('Knoten bereits vorhanden')
        self.nodes[name] = GerichteterGraph.GerichteterKnoten(name)
        # new node isn't connected -> no binary tree anymore
        if self.num_nodes > 1:
            self.isBinaryTree = False
            
    def check_binary_tree(self):
        if self.num_edges != self.num_nodes - 1:
            self.isBinaryTree = False
        else:
            numRoots = 0
            for node in self.nodes.values():
                if node.in_deg == 0:
                    numRoots += 1
                if node.in_deg > 1:
                    self.isBinaryTree = False
                    break
                if node.out_deg > 2:
                    self.isBinaryTree = False
                    break
                if numRoots > 1:
                    self.isBinaryTree = False
                    break
            else:
                self.isBinaryTree = numRoots == 1
    
    def remove_node(self, name):
        try:
            node = self.nodes[name]
        except KeyError:
            raise ValueError('Knoten nicht vorhanden')
        del self.nodes[name]
        for n in node.in_edges:
            n.out_edges.remove(node)
        for n in node.out_edges:
            n.in_edges.remove(node)
        for n in node.edges:
            n._edges.remove(node)
        self.num_edges -= node.deg()
        
        self.check_binary_tree()
    
    def add_edge(self, start: str, end: str, value=0):
        try:
            node1 = self.nodes[start]
            node2 = self.nodes[end]
        except KeyError:
            raise ValueError('ein Knoten nicht vorhanden')
        if node2 in node1.out_edges:
            raise ValueError('Kante bereits vorhanden')
        node1.add_out_edge(node2)
        self.num_edges += 1
        self.edge_weights[(start, end)] = value
        
        self.check_binary_tree()

    
    def remove_edge(self, start: str, end: str):
        try:
            node1 = self.nodes[start]
            node2 = self.nodes[end]
        except KeyError:
            raise ValueError('ein Knoten nicht vorhanden')
        if node2 not in node1.out_edges:
            raise ValueError('Kante nicht vorhanden')
        node1.remove_out_edge(node2)
        self.num_edges -= 1
        self.edge_weights.pop((start, end))
        
        self.check_binary_tree()
    
    def toGraph(self):
        graph = Graph()
        for node in self.nodes.values():
            graph.add_node(node.name)
        for node in self.nodes.values():
            for edge in node._edges:
                graph.add_edge(node.name, edge.name)
        return graph
    
    def get_Adjazenzmatrix(self):
        matrix = []
        for node in self.nodes.values():
            row = [0] * self.num_nodes
            for edge in node.out_edges:
                row[list(self.nodes.values()).index(edge)] = 1
            matrix.append(row)
        return matrix
    
    def invert(self):
        for node in self.nodes.values():
            node.in_edges, node.out_edges = node.out_edges, node.in_edges
            
    def __add__(self, other):
        if not isinstance(other, GerichteterGraph):
            raise TypeError('GerichteterGraph kann nur mit GerichteterGraph addiert werden')
        result = GerichteterGraph()
        for node in self.nodes.values():
            result.add_node(node.name)
        for node in other.nodes.values():
            try:
                result.add_node(node.name)
            except:
                continue
        edges = 0
        for node in result.nodes.values():
            for _edge in node.out_edges:
                edges += 1
        result.num_edges = edges // 2
        return result
    
    def __contains__(self, key):
        if isinstance(key, Graph.Node):
            key = key.name
        if isinstance(key,str):
            return key in self.nodes
        if isinstance(key, tuple) or isinstance(key, list):
            if len(key) == 2 and isinstance(key[0], str) and isinstance(key[1], str):
                return key[0] in self.nodes and key[1] in self.nodes and self.nodes[key[0]] in self.nodes[key[1]].edges
            
            #expects a tuple or list of edges [(node1name, node2name), (node2name, node3name), ...]
            for edge in key:
                if not isinstance(edge, tuple) and not isinstance(edge, list):
                    return False
                if len(edge) != 2:
                    return False
                if edge[0] not in self.nodes or edge[1] not in self.nodes:
                    return False
                if self.nodes[edge[0]] not in self.nodes[edge[1]].in_edges:
                    return False
            return True
        raise ValueError('key must be a string, a Graph.Node or a list of edges')

def generateGraph(n: int, i: int, j: int)-> Graph:
    graph = Graph()
    for k in range(n):
        graph.add_node(str(k), random.randint(i,j))
    allNodes = set(graph.nodes)
    for node in graph.nodes.values():
        currentEdges = set(map(lambda n: n.name, node.edges))
        nEdges = len(currentEdges)
        edgesToCreate = math.ceil(n/2)-nEdges
        possibleEdges = sorted(allNodes - currentEdges - {node.name})
        newEdges = random.sample(possibleEdges, edgesToCreate)
        for edge in newEdges:
            graph.add_edge(node.name, edge, random.randint(i,j))
    return graph

def greedySearch(graph: Graph, start: str, end: str):
    if start not in graph or end not in graph:
        raise ValueError('Knoten nicht vorhanden')
    start = graph[start]
    end = graph[end]
    nodeOrder = [start]
    distance = []
    visited = set()
    while nodeOrder[-1] != end:
        node = nodeOrder[-1]
        visited.add(node.name)
        nextNode = None
        minWeight = float('inf')
        for edge in node.edges:
            if edge.name not in visited and graph.get_edge_weight(node.name, edge.name) < minWeight:
                nextNode = edge
                minWeight = graph.get_edge_weight(node.name, edge.name)
        if nextNode is None:
            # go back if no way forward
            nodeOrder.pop()
            distance.pop()
        else:
            nodeOrder.append(nextNode)
            distance.append(minWeight)
    return sum(distance), nodeOrder

def dijkstra(graph: Graph, start: str, end: str):
        if start not in graph.nodes or end not in graph.nodes:
            raise ValueError('Knoten nicht vorhanden')
        start = graph[start]
        end = graph[end]
        if start == end:
            return 0, [start]
        distances = {node: float('inf') for node in graph.nodes.values()}
        distances[start] = 0
        Q = [start] # idealerweise MinHeap
        visited = set()
        previous = {node: None for node in graph.nodes.values()}
        while Q:
            node = min(Q, key=lambda n: distances[n])
            visited.add(node)
            Q.remove(node)
            for edge in node.edges:
                if edge not in visited:
                    newDist = distances[node] + graph.get_edge_weight(node.name, edge.name)
                    if newDist < distances[edge]:
                        if distances[edge] == float('inf'):
                            Q.append(edge)
                        distances[edge] = newDist
                        previous[edge] = node
        path = [end]
        while path[-1] != start:
            path.append(previous[path[-1]])
        path.reverse()
        return distances[end], path
            
class Binärbaum(Graph):
    def __init__(self, nodes : list[str] = None):
        super().__init__()
        self.isBinaryTree = True
        self.root = None
        if nodes is not None:
            self.build(nodes)
        
    def __build_rec(self, sortedList: list[tuple[str,int]], parentName: str):
        if not sortedList:
            return
        mid = len(sortedList) // 2
        node = self.add_node(str(sortedList[mid]), sortedList[mid])
        self.add_edge(parentName, node.name)
        self.__build_rec(sortedList[:mid], node.name)
        self.__build_rec(sortedList[mid+1:], node.name)
    
    # each node has up to 3 edges (1 to parent if not root, 2 to children)
    # builds a balanced search tree
    def build(self, nodes: list[int]):
        nodes.sort()
        mid = len(nodes) // 2
        self.root = self.add_node(str(nodes[mid]), nodes[mid])
        self.__build_rec(nodes[:mid], self.root.name)
        self.__build_rec(nodes[mid+1:], self.root.name)
        return self
    
    # returns a tuple with a boolean indicating if the value was found and the node if it was found and the parent node
    def __search_pos(self, value: int) -> tuple[bool, Graph.Node, Graph.Node]:
        node = self.root
        previous = None
        while node.value != value:
            nextNode = None
            if value > node.value:
                # search right child
                for edge in node.edges:
                    if edge.value > node.value and edge != previous:
                        nextNode = edge
                        break
            else:
                # search left child
                for edge in node.edges:
                    if edge.value < node.value and edge != previous:
                        nextNode = edge
                        break
            # no child in the right direction
            if nextNode is None:
                return False, None, node
            previous = node
            node = nextNode
        return True, node, previous
    
    # looks whether a value is in the tree
    def search(self, value: int) -> bool:
        return self.__search_pos(value)[0]
    
    # inserts a new node into the tree, does not preserve balance
    def insert(self, value: int):
        searchRes = self.__search_pos(value)
        if searchRes[0]:
            raise ValueError('value already exists')
        parent = searchRes[2]
        self.add_node(str(value), value)
        self.add_edge(parent.name, str(value))
    
    # removes a node from the tree, does not preserve balance
    def remove(self, value: int):
        searchRes = self.__search_pos(value)
        if not searchRes[0]:
            raise ValueError('value not found')
        node = searchRes[1]
        parent = searchRes[2]
        # create new connections before removing the node
        if len(node.edges) == 1 and parent is not None:
            # no children
            pass
        elif len(node.edges) == 2 and parent is not None or len(node.edges) == 1 and parent is None:
            # one child
            child = node.edges[0] if node.edges[0] != parent else node.edges[1]
            self.add_edge(parent.name, child.name)
        else:
            # two children, find the smallest node in the right subtree
            nextNode = None
            previous = parent
            # go to right child
            for edge in node.edges:
                if edge.value > node.value and edge is not parent:
                    previous = node
                    nextNode = edge
                    break
            while nextNode is not None:
                current = nextNode
                nextNode = None
                for edge in current.edges:
                    if edge.value < current.value and edge is not previous:
                        previous = current
                        nextNode = edge
                        break
            # cut child loose
            self.remove_edge(previous.name, current.name)
            if current.edges:
                self.add_edge(previous.name, current.edges[0].name)
                self.remove_edge(current.name, current.edges[0].name)
            
            # add child in place of removed node
            for edge in node.edges:
                if edge != current:
                    self.add_edge(current.name, edge.name)
        # remove node
        self.remove_node(node.name)
    
    
# graph = generateGraph(4, 1, 4)
# for node in graph.nodes.values():
#     print(node.name, list(map(lambda n: (n.name, graph.get_edge_weight(node.name,n.name)),node.edges)))
# print(graph.bfs(3))
# print(graph.dfs(3))
# print(greedySearch(graph, '0', '3'))
# print(dijkstra(graph,'0','3'))

# baum = Binärbaum()
# baum.build([0,1,2,3,4,5,6])
# print(baum.search(1))
# for node in baum.nodes.values():
#     print(node.name, node.value, node.edges)
# baum.insert(7)
# print()
# for node in baum.nodes.values():
#     print(node.name, node.value, node.edges)
# baum.remove(2)
# baum.remove(1)
# print()
# for node in baum.nodes.values():
#     print(node.name, node.value, node.edges)


import time

n = 4000

# generate Graph
start = time.perf_counter()
graph = generateGraph(n, 1, n//10)
print("Graph generated in", time.perf_counter() - start, "seconds")

# dijkstra
start = time.perf_counter()
print(dijkstra(graph, '0', str(n-1))[0])
print(time.perf_counter() - start)

# greedySearch
start = time.perf_counter()
print(greedySearch(graph, '0', str(n-1))[0])
print(time.perf_counter() - start)

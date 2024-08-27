class Graph:
    class Node:
        def __init__(self, name):
            self._name = name
            self._edges: list[Graph.Node] = []
        
        @property
        def name(self):
            return self._name
        
        @property
        def edges(self):
            return self._edges
        
        def deg(self):
            return len(self.edges)
        
        def __repr__(self):
            return self.name
        
    def __init__(self, nodes : list[str] = None):
        self.nodes: dict[str,Graph.Node] = {}
        if nodes is not None:
            if len(nodes) != len(set(nodes)):
                raise ValueError('Knoten doppelt vorhanden')
            for node in nodes:
                self.add_node(node)
        self.num_edges = 0
    
    @property
    def num_nodes(self):
        return len(self.nodes)
    
    def add_node(self, name):
        if name in self.nodes:
            raise ValueError('Knoten bereits vorhanden')
        self.nodes[name] = Graph.Node(name)
    
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
        
    def add_edge(self, name1: str, name2: str):
        try:
            node1 = self.nodes[name1]
            node2 = self.nodes[name2]
        except KeyError:
            raise ValueError('ein Knoten nicht vorhanden')
        if node2 in node1.edges:
            raise ValueError('Kante bereits vorhanden')
        node1._edges.append(node2)
        node2._edges.append(node1)
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
        self.num_edges -= 1
    
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
            for _edge in node.edges:
                edges += 1
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

# Meckerbemerkung: es wäre viel sinnvoller gewesen einen Bidirektionalen Graphen
# als Spezialfall eines Gerichteten Graphen zu implementieren
class GerichteterGraph(Graph):
    class GerichteterKnoten(Graph.Node):
        def __init__(self, name):
            super().__init__(name)
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
    
    def add_edge(self, start: str, end: str):
        try:
            node1 = self.nodes[start]
            node2 = self.nodes[end]
        except KeyError:
            raise ValueError('ein Knoten nicht vorhanden')
        if node2 in node1.out_edges:
            raise ValueError('Kante bereits vorhanden')
        node1.add_out_edge(node2)
        self.num_edges += 1
        
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
    
graph = Graph(['A', 'B', 'C', 'D', 'E'])
print(str(graph))
print(len(graph))
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('D', 'E')

print(graph['A'].deg())
print('A' in graph)
print(graph['A'] in graph)
print(['A','E'] in graph)
print(graph.highest_deg())
print(graph.lowest_deg())
class Graph:
    class Node:
        def __init__(self, name):
            self._name = name
            self._edges = []
        
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
        self.nodes = []
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
        if name in [node.name for node in self.nodes]:
            raise ValueError('Knoten bereits vorhanden')
        self.nodes.append(Graph.Node(name))
    
    def change_name(self, oldName, newName):
        if newName in [node.name for node in self.nodes]:
            raise ValueError('neuer Name bereits vorhanden')
        for node in self.nodes:
            if node.name == oldName:
                node._name = newName
                break
        else:
            raise ValueError('Knoten nicht vorhanden')
    
    def remove_node(self, name):
        node = None
        for n in self.nodes:
            if n.name == name:
                node = n
                break
        if node is None:
            raise ValueError('Knoten nicht vorhanden')
        self.nodes.remove(node)
        for n in node.edges:
            n._edges.remove(node)
        self.num_edges -= node.deg()
        
    def add_edge(self, name1: str, name2: str):
        node1 = None
        node2 = None
        for n in self.nodes:
            if n.name == name1:
                node1 = n
                if node2 is not None:
                    break
            if n.name == name2:
                node2 = n
                if node1 is not None:
                    break
        if node1 is None:
            raise ValueError(f'Knoten {node1} nicht vorhanden')
        if node2 is None:
            raise ValueError(f'Knoten {node2} nicht vorhanden')
        if node2 in node1.edges:
            raise ValueError('Kante bereits vorhanden')
        node1._edges.append(node2)
        node2._edges.append(node1)
        self.num_edges += 1
        
    def remove_edge(self, name1: str, name2: str):
        node1 = None
        node2 = None
        for n in self.nodes:
            if n.name == name1:
                node1 = n
                if node2 is not None:
                    break
            if n.name == name2:
                node2 = n
                if node1 is not None:
                    break
        if node1 is None:
            raise ValueError(f'Knoten {node1} nicht vorhanden')
        if node2 is None:
            raise ValueError(f'Knoten {node2} nicht vorhanden')
        if node2 not in node1.edges:
            raise ValueError('Kante nicht vorhanden')
        node1._edges.remove(node2)
        node2._edges.remove(node1)
        self.num_edges -= 1
    
    def avg_deg(self):
        return self.num_edges * 2 / self.num_nodes
    
    def highest_deg(self):
        nodes:list[Graph.Node] = []
        deg = 0
    
        for node in self.nodes:
            if node.deg() > deg:
                nodes = [node]
                deg = node.deg()
            elif node.deg() == deg:
                nodes.append(node)
        return nodes
    
    def lowest_deg(self):
        nodes:list[Graph.Node] = []
        deg = self.num_nodes
    
        for node in self.nodes:
            if node.deg() < deg:
                nodes = [node]
                deg = node.deg()
            elif node.deg() == deg:
                nodes.append(node)
        return nodes
    
graph = Graph(['A', 'B', 'C', 'D', 'E'])
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('D', 'E')

print(graph.highest_deg())
print(graph.lowest_deg())
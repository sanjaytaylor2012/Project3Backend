class temp_graph:
    def __init__(self):
        # structure: key: name+brand val:[[name],[adj nodes (name+brand)]]
        self.graph = {}

    # _from and _to are keys (name_brand)
    def addEdge(self, _from, _to):
        self.graph[_from][1].append(_to)
        self.graph[_to][1].append(_from)

    # Peanut ButterTrader Joe's: [[1, 2, 3], [PeanutButterWalmart, ...]]
    def addVertex(self, name_brand, name_as_vector):
        self.graph[name_brand] = []
        self.graph[name_brand].append(name_as_vector)
        self.graph[name_brand].append([])

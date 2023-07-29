import Food


class AdjList:
    def __init__(self):
        # key: food + brand
        # value: food obj, adj nodes
        self.graph = {}

    # def addEdge(self, _from, _to):
    #     if self.graph.get((_from.name + _from.brand)) == None:
    #         self.graph[(_from.name + _from.brand)][1] = []
    #     self.graph[(_from.name + _from.brand)][0] = _from
    #     self.graph[(_from.name + _from.brand)][1].append((_to.name + _to.brand))
    #     if self.graph.get((_to.name + _to.brand)) == None:
    #         self.graph[(_to.name + _to.brand)][0] = _to
    #         self.graph[(_to.name + _to.brand)][1] = []

    # def addVertex(self, food):
    #     if self.graph.get((food.name + food.brand)) == None:
    #         self.graph[(food.name + food.brand)][0] = food
    #         self.graph[(food.name + food.brand)][1] = []

    def addEdge(self, _from, _to):
        self.graph[_from][1].append(_to)
        self.graph[_to][1].append(_from)

    # {peanuts butter: [Food(Peanut Butter), [Salted Peanuts, Peanut Spread]]}
    def addVertex(self, food):
        if (food.name) not in self.graph:
            self.graph[(food.name)] = []
            self.graph[(food.name)].append(food)
            self.graph[(food.name)].append([])

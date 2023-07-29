class Food:
    def __init__(
        self,
        name,
        brand,  # url, servingSize, energy, fat, sugar, protein, fiber, sodium
    ):
        self.name = name
        self.brand = brand
        # self.url = url
        # self.servingSize = servingSize
        # self.energy = energy
        # self.fat = fat
        # self.sugar = sugar
        # self.protein = protein
        # self.fiber = fiber
        # self.sodium = sodium

    def getName(self):
        return self.name

    def getBrand(self):
        return self.brand

    # def getURL(self):
    #     return self.url

    # def getServingSize(self):
    #     return self.servingSize

    # def getEnergy(self):
    #     return self.energy

    # def getFat(self):
    #     return self.fat

    # def getSugar(self):
    #     return self.sugar

    # def getProtein(self):
    #     return self.protein

    # def getFiber(self):
    #     return self.fiber

    # def getSodium(self):
    #     return self.sodium

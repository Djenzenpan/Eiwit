class Protein(object):
    def __init__(self, protein):
        self.sequence = protein
        self.length = len(protein)
        self.dimension = (self.length * 2) - 1
        self.field = [["_"] * self.dimension for i in range(self.dimension)]

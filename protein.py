class Protein(object):
    def __init__(self, protein):
        self.sequence = protein
        self.length = len(protein)
        self.dimension = (self.length * 2) - 1
        self.field = [["_"] * self.dimension for i in range(self.dimension)]
        self.current_option = ["right" for i in range(self.length - 2)]
        self.field[self.length - 1][self.length - 1] = self.sequence[0]
        self.field[self.length][self.length - 1] = self.sequence[1]
        self.number = 0
        self.best_fold_points = 0
        self.best_fold = None

    """ createss field based on the current_option"""
    def create_field(self, x, y):
        for aminoacid, option in zip(self.sequence[2:], range(len(self.current_option))):
           if self.current_option[option] == "right":
               if self.field[y][x+1] == "_":
                   self.field[y][x+1] = aminoacid
                   x = x + 1
               else:
                   self.current_option[option] = "up"
           if self.current_option[option] == "up":
               if self.field[y-1][x+1] == "_":
                   self.field[y-1][x] = aminoacid
                   y = y - 1
               else:
                   self.current_option[option] = "left"
           if self.current_option[option] == "left":
               if self.field[y][x-1] == "_":
                   self.field[y][x-1] = aminoacid
                   x = x - 1
               else:
                   self.current_option[option] = "down"
           if self.current_option[option] == "down":
               if self.field[y+1][x] == "_":
                   self.field[y+1][x] = aminoacid
                   y = y + 1
               else:
                   self.current_option[option] = "right"

    """ calculates current_option fields total points"""
    def fold_points(self):
        points = 0
        for i in range(self.dimension):
           for j in range(self.dimension):
               if self.field[j][i] == "H":
                   if self.field[j+1][i] == "H":
                       points += 1
                   if self.field[j-1][i] == "H":
                       points += 1
                   if self.field[j][i-1] == "H":
                       points += 1
                   if self.field[j][i+1] == "H":
                       points += 1
        for i in range(self.length - 1):
                if self.sequence[i] == self.sequence[i + 1] == "H":
                    points -= 1
        for i in range(self.length):
            if i != 0 and self.sequence[i] == self.sequence[i - 1] == "H":
                    points -= 1
        return(int(points / 2))

    """checks whether current option is the best option yet"""
    def check_option(self):
        self.create_field((self.length - 1), self.length)
        if self.fold_points() > self.best_fold_points:
            self.best_fold_points = self.fold_points()
            self.best_fold = self.current_option

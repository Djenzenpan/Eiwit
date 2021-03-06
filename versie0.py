from sys import argv
from protein import Protein
from option import Option
from field import Field

def main():
    # checks whether program is used correctly
    check()
    best_fold_points = 0
    # makes user input into the protein class
    protein = Protein(argv[1])
    # checks whether current option is better than all previous ones
    options = Option(protein.length)
    field = Field(protein.length, protein.sequence)
    best_fold = options.options[0]
    #
    ### while(not_all_options):
    #
    # creates field and fold based on the protein and the current option
    for option in options.options:
        if(field.fill_field(protein.sequence, option)):
            # check wether current fold is the best and remembers it if it is
            if int(fold_points(field, protein.errorpoint)) > int(best_fold_points):
                best_fold_points = fold_points(field, protein.errorpoint)
                best_fold = option
        field.clear_field(protein.length)
        field.x_cdn = protein.length - 1
        field.y_cdn = protein.length
    # prints best_fold_points and best_fold and current field
    print(best_fold_points)
    print(best_fold)
    field.fill_field(protein.sequence, best_fold)
    for line in field.field:
        print(line)


# checks user input
def check():
    if len(argv) != 2:
        exit("Usage: python protein.py proteinsequence")
    for aminoacid in argv[1]:
        if aminoacid != 'H' and aminoacid != 'P':
            exit("Protein sequence can only contain P and H")

# checks the points scored by the current fold
def fold_points(field, reduction):
    points = 0
    for i in range(field.dimension):
       for j in range(field.dimension):
           if field.field[j][i] == "H":
               if field.field[j+1][i] == "H":
                   points += 1
               if field.field[j-1][i] == "H":
                   points += 1
               if field.field[j][i-1] == "H":
                   points += 1
               if field.field[j][i+1] == "H":
                   points += 1
    points = points - reduction
    return(int(points / 2))


if __name__ == '__main__':
    main()

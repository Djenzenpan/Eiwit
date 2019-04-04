from sys import argv
from protein import Protein

def main():
    # checks whether program is used correctly
    check()
    # makes user input into the protein class
    protein = Protein(argv[1])
    # initialises first aminoacid directly above the middle of the field and
    # the second aminoacid in the middle of the field
    protein.field[protein.length - 1][protein.length - 1] = protein.sequence[0]
    protein.field[protein.length][protein.length - 1] = protein.sequence[1]
    #
    # TODO
    # protein.check_best
    #
    # remembers x and y coordinates of current aminoacid
    x = protein.length - 1
    y = protein.length

    ### configures protein to go down in a straight line
#    for aminoacid in protein.sequence[2:]:
#        if protein.field[y+1][x] == "_":
#            protein.field[y+1][x] = aminoacid
#            y = y+1
#        elif protein.field[y][x+1] == "_":
#            protein.field[y][x+1] = aminoacid
#            x = x+1

    # prints field
    for line in protein.field:
        print(line)


def check():
    if len(argv) != 2:
        exit("Usage: python protein.py proteinsequence")
    for aminoacid in argv[1]:
        if aminoacid != 'H' and aminoacid != 'P':
            exit("Protein sequence can only contain P and H")


if __name__ == '__main__':
    main()

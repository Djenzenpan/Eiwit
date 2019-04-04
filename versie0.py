from sys import argv
from protein import Protein

def main():
    # checks whether program is used correctly
    check()
    # makes user input into the protein class
    protein = Protein(argv[1])
    # folds protein for testing
    if len(protein.current_option) > 7:
        protein.current_option[1] = "up"
        protein.current_option[2] = "up"
        protein.current_option[3] = "left"
        protein.current_option[4] = "left"
        protein.current_option[5] = "down"
        protein.current_option[6] = "down"
    # checks whether current option is better than all previous ones
    protein.check_option()
    # prints best_fold_points and best_fold and best field
    print(protein.best_fold_points)
    print(protein.best_fold)
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

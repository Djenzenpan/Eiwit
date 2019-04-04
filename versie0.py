from sys import argv

def main():
    # checks whether program is used correctly
    check()
    # creates field for protein to fold in
    field = createfield()
    # prints field
    for line in field:
        print(line)
    # print(check_all_options(field))
    #



def check():
    if len(argv) != 2:
        exit("Usage: python protein.py proteinsequence")
    for aminoacid in argv[1]:
        if aminoacid != 'H' and aminoacid != 'P':
            exit("Protein sequence can only contain P and H")

def createfield():
    proteinsequence = argv[1]
    dimension = len(proteinsequence) * 2 - 1
    field = [[0] * dimension for i in range(dimension)]
    return field


if __name__ == '__main__':
    main()

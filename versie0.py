from sys import argv

def main():
    # checks whether program is used correctly
    check()
    proteinsequence = argv[1]
    # creates field for protein to fold in and remembers middle of field
    field, middle = createfield(proteinsequence)
    # prints field
    field[middle][middle] = proteinsequence[0]
    field[middle + 1][middle] = proteinsequence[1]
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

def createfield(proteinsequence):
    dimension = len(proteinsequence) * 2 - 1
    print(dimension)
    field = [["O"] * dimension for i in range(dimension)]
    return field, (int((dimension-1)/2))


if __name__ == '__main__':
    main()

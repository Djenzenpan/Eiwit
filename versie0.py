from sys import argv

def main():
    # checks whether program is used correctly
    check()
    # creates field for protein to fold in and remembers middle of field
    proteinsequence = argv[1]
    field, middle = createfield(proteinsequence)
    # initialises first aminoacid in the middle of field and the second
    # aminoacid directly below the middle
    field[middle][middle] = proteinsequence[0]
    field[middle + 1][middle] = proteinsequence[1]
    # remembers x and y coordinates of current aminoacid
    x = middle
    y = middle + 1
    for aminoacid in proteinsequence[2:]:
        if field[y+1][x] == "O":
            field[y+1][x] = aminoacid
            y = y+1
        elif field[y][x+1] == "O":
            field[y][x+1] = aminoacid
            x = x+1
    # TODO
    # check_all_options(field)
    # prints field
    for line in field:
        print(line)


def check():
    if len(argv) != 2:
        exit("Usage: python protein.py proteinsequence")
    for aminoacid in argv[1]:
        if aminoacid != 'H' and aminoacid != 'P':
            exit("Protein sequence can only contain P and H")

def createfield(proteinsequence):
    dimension = len(proteinsequence) * 2 - 1
    field = [["O"] * dimension for i in range(dimension)]
    return field, (int((dimension-1)/2))


if __name__ == '__main__':
    main()

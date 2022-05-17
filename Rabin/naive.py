import time
def naive_pattern(source):
    with open(source) as matrix:
        lines = matrix.read().splitlines()
    count = 0
    # print("Found patterns at:")

    for x in range(len(lines) -3 + 1):
        for y in range(len(lines) -3 + 1):
            if(lines[x][y]) == 'A' and lines[x][y + 1] == 'B' and lines[x][y + 2] == 'C':
                if lines[x + 1][y] == 'B' and lines[x + 2][y] == 'C':
                    # print(str(x) + ', ' + str(y))
                    count += 1

    # print(str(count) + ' patterns found')


# naive_pattern('patterns/1000_pattern.txt')
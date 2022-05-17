#rabin karp but with addition and some ifs
import time

def whole(source):
    with open(source) as file:
        lines = file.read().splitlines()
        matrix = []
        for i in range(len(lines)):
            matrix.append(list(lines[i]))
            for j in range(len(lines)):
                matrix[i][j] = int(matrix[i][j], 16) #numbers in hexadecimal
    pattern = [10, 11, 12] #A, B, C in hexadecimal

    return rabin(pattern, matrix)

def rabin(pat, txt):
    d = 16 #number of letters

    count = 0
    M = len(pat)
    N = len(txt)
    i = 0
    p_hash = 0
    t_hash = 0
    for i in range(M): #pattern value
        p_hash += pat[i]

    for y in range(N - M + 1): #range(N - M + 1)
        t_hash = 0
        for i in range(M): #single line
            t_hash += txt[y][i] #index 0 - text value
        
        for x in range(N - M + 1):
            if p_hash == t_hash:
                if pat[0] == txt[y][x] and pat[1] == txt[y + 1][x] and pat[2] == txt[y + 2][x]:

                    t_hash_vert = txt[y][x] + txt[y + 1][x] + txt[y + 2][x]
                    if p_hash == t_hash_vert:
                        if pat[1] == txt[y][x + 1] and pat[2] == txt[y][x + 2]:
                            # print(str(y) + ', ' + str(x))
                            count += 1

            if x < N - M: #new hash creation
                t_hash += txt[y][x + M] - txt[y][x] #single line
    return count


# print(str(whole('patterns/1000_pattern.txt')) + ' patterns found')
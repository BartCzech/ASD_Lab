from texttable import Texttable
import time
import rabin_karp
import naive

data = []

def calculate(n):
    naive_start = time.time()
    naive.naive_pattern('patterns/' + str(n) + '_pattern.txt')
    naive_end = time.time() - naive_start

    rk_start = time.time()
    rabin_karp.whole('patterns/' + str(n) + '_pattern.txt')
    rk_end = time.time() - rk_start
    data.append([
        n,
        (naive_end),
        (rk_end)
        ])

def draw():
    t = Texttable()
    t.add_rows([
        ['N', 'naive time', 'Rabin-Karp time'],
        *data
    ])
    print(t.draw())

calculate(1000)
calculate(2000)
calculate(3000)
calculate(4000)
calculate(5000)
calculate(8000)
draw()
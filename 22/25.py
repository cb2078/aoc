import math
p=open('25.txt').read().strip().split('\n')

dig =  {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
dig_r =  {v: k for k, v in dig.items()}
dec = lambda x: sum(dig[c] * 5 ** (len(x) - i - 1) for i, c in enumerate(x))
b5 = lambda x: [x // 5 ** i % 5 for i in range(math.ceil(math.log(x, 5)))]

def snafu(x):
    x = b5(x) + [0]
    for i in range(len(x)):
        if x[i] <= 2:
            continue
        x[i] -= 5
        x[i + 1] += 1
    if x[-1] == 0:
        del x[-1]
    return ''.join(dig_r[y] for y in x[::-1])

print(snafu(sum(map(dec, p)))) # 1

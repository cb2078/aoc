f=open('06.txt').read().strip()
# n = 4 # 1
n = 14 # 2

for i in range(len(f) - n + 1):
    p = f[i: i + n]
    if len(p) == len(set(p)):
        print(i + n)
        break

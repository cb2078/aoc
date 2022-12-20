f=open('17.txt').read().strip()
s='''####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##'''.split('\n\n')
w=7
s=[x.split('\n') for x in s]
s=[sum((x[i][j]=='#')<<w-1-j<<(len(x)-i-1)*w for i in range(len(x)) for j in range(len(x[i]))) for x in s]

def t(x):
    n = 0
    while x:
        x >>= w
        n += 1
    return n

g0 = (1 << w) - 1
p=lambda x:'\n'.join(''.join('.#'[0!=x&1<<(t(x)-i-1)*w<<w-j-1] for j in range(w)) for i in range(t(x)))+'\n'
b = lambda x,o: max((i + 1) * (0 != 1 << i * w + o & x) for i in range(t(x)))
l = lambda g: max((i + 1) * (g0 == g0 & g >> i * w) for i in range(t(g)))

def solve(i, j, k):
    g = g0
    i0, j0 = i, j
    x = s[i] << (3 + t(g)) * w >> 2
    n = dn = 0
    r = dr = 0
    dp = {} # (i,j,dr,dn)
    while n + dn < k:
        if g == g0 and (i,j) in dp:
            c = []
            while (i,j) not in c:
                c += [(i,j)]
                i, j = dp[i,j][:2]
            rep = (k - n) // sum(dp[i,j][3] for i,j in c)
            dr, dn = (sum(dp[i,j][o] * rep for i,j in c) for o in (2, 3))
            return r + dr + solve(i, j, k - n - dn)
        if f[j] == '<' and b(x, w - 1) == 0 and 0 == g & x << 1:
            x <<= 1
        if f[j] == '>' and b(x, 0) == 0 and 0 == g & x >> 1:
            x >>= 1
        if x >> w & g:
            g |= x
            d = l(g) - 1
            dr += d
            g >>= w * d
            i = (i + 1) % 5
            x = s[i] << (3 + t(g)) * w >> 2
            dn += 1
            if g == g0:
                dp[i0, j0] = i, (j + 1) % len(f), dr, dn
                i0, j0 = i, (j + 1) % len(f)
                r, dr = r + dr, 0
                n, dn = n + dn, 0
        else:
            x >>= w
        j = (j + 1) % len(f)
    return r + dr + t(g) - 1

print(solve(0, 0, 2022)) # 1
print(solve(0, 0, 1000000000000)) # 2

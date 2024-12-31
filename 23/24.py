h = [[tuple(map(int, y.split(', '))) for y in x.split(' @ ')] for x in open('24.txt').read().strip().split('\n')]
n = len(h)

def GE(m):
    w, h = len(m[0]), len(m)
    for k in range(h):
        if m[k][k] == 0:
            for i in range(k + 1, h):
                if m[i][k]:
                    m[k], m[i] = m[i], m[k]
                    break
            else:
                continue
        for i in range(k + 1, h):
            r = -m[i][k] / m[k][k]
            for j in range(w):
                m[i][j] += r * m[k][j]
    for k in range(h - 1, 0, -1):
        if m[k][k] == 0:
            continue
        for i in range(k - 1, -1, -1):
            r = -m[i][k] / m[k][k]
            for j in range(w):
                m[i][j] += r * m[k][j]
    return m

def p1(p, v, P, V):
    mn, mx=200000000000000, 400000000000000
    # p+tv=P+sV=>tv-sV=P-p
    m =[[v[i], -V[i], P[i]-p[i]] for i in range(2)]
    m = GE(m)
    if any(m[k][k] == 0 for k in range(2)):
        return False
    t= m[0][2] / m[0][0]
    T= m[1][2] / m[1][1]
    return t >= 0 and T >= 0 and all(mn <= p[i] + t * v[i] <= mx for i in range(2))
print(sum(p1(*h[i], *h[j]) for i in range(n) for j in range(i)))

def LI(v0, v1, v2):
    m = GE([list(v0), list(v1), list(v2)])
    return any(m[-1])

def dot(u, v):
    return sum(u[i] * v[i] for i in range(3))

def cross(u, v):
    return [u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0]]

def sub(u, v):
    return [u[i] - v[i] for i in range(3)]

def p2(p0, v0, p1, v1, p2, v2):
    V1 = sub(v1, v0)
    V2 = sub(v2, v0)
    P1 = sub(p1, p0)
    P2 = sub(p2, p0)
    t1 = -dot(V2, cross(P1, P2)) / dot(V2, cross(V1, P2))
    t2 = -dot(V1, cross(P1, P2)) / dot(V1, cross(P1, V2))
    v = [((t2 * v2[i] + p2[i]) - (t1 * v1[i] + p1[i])) / (t2 - t1) for i in range(3)]
    p = [p1[i] + t1 * v1[i] - t1 *v[i] for i in range(3)]
    return sum(p)

i, j, k = next((i, j, k) for i in range(n) for j in range(i) for k in range(j) if LI(h[i][1], h[j][1], h[k][1]))
print('%.0f'%p2(*h[i], *h[j], *h[k]))

'''
if the rock starts at positio p with velocity v

p0+t0v0=p+t0v
p1+t1v1=p+t1v
...
pi+(ti)vi=p+(ti)v

since the intersections lie on a line

((p+t1v)-(p+t0v))x((p+t2v)-(p+t0v))=(0,0,0)
((p1+t1v1)-(p0+t0v0))x((p2+t2v2)-(p0+t0v0))=(0,0,0)

let Vi=vi-v0

((p1+t1V1)-p0)x((p2+t2V2)-p0)=(0,0,0)
(t1V1+(p1-p0))x(t2V2+(p2-p0))=(0,0,0)
(t1V1)x(t2V2)+(t1V1)x(p2-p0)+(p1-p0)x(t2V2)+(p1-p0)x(p2-p0)=(0,0,0)
t1t2(V1xV2)+t1(V1x(p2-p0))+t2((p1-p0)xV2)+(p1-p0)x(p2-p0)=(0,0,0)

let Pi=pi-p0

t1t2(V1xV2)+t1(V1xP2)+t2(P1xV2)+P1xP2=(0,0,0)    (eq.0)

solve for t1

t1t2V2.(V1xV2)+t1V2.(V1xP2)+t2V2.(P1xV2)+V2.(P1xP2)=V2.(0,0,0)    (eq.0).V2
t1V2.(V1xP2)+V2.(P1xP2)=0
t1=-(V2.(P1xP2))/(V2.(V1xP2))

solve for t2

t1t2V1.(V1xV2)+t1V1.(V1xP2)+t2V1.(P1xV2)+V1.(P1xP2)=V1.(0,0,0)    (eq.0).V1
t2V1.(P1xV2)+V1.(P1xP2)=0
t2=-(V1.(P1xP2))/(V1.(P1xV2))

therefore

v=(t2v2+p2-t1v1-p1)/(t2-t1)
p=(P1+t1v1)-t1v

'''

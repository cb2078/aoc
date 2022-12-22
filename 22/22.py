g,p=open('22.txt').read().rstrip().split('\n\n')
g0=g=g.split("\n")
g, w = ({j + i * 1j for i in range(len(g)) for j in range(len(g[i])) if g[i][j] == c} for c in '.#')
import re
p=re.findall(r'\d+|[RL]', p)

def c(z):
    if z in v:
        return {1: '>', -1j: '^', -1: '<', 1j: 'v'}[v[z]]
    if z in w:
        return '#'
    if z in g:
        return '.'
    return ' '

sz = 50
faces = {}
dirs = (1, -1, 1j, -1j)
s = [g0[0].index('.')]
while s:
    z, *s = s
    if z in faces:
        continue
    neighbors = {dz: (z + dz * sz, 1) for dz in dirs if z + dz * sz in g | w}
    faces[z] = neighbors
    s += [v[0] for v in neighbors.values()]
while any(len(v) < 4 for v in faces.values()):
    for k in faces:
        for dz in dirs:
            if dz in faces[k]:
                continue
            for dr in (1j, -1j):
                if dz * dr not in faces[k]:
                    continue
                neighbor_pos, neighbor_rot = faces[k][dz * dr]
                if dz * neighbor_rot not in faces[neighbor_pos]:
                    continue
                target_pos, target_rot = faces[neighbor_pos][dz * neighbor_rot]
                assert dz not in faces[k]
                faces[k][dz] = (target_pos, target_rot * neighbor_rot * dr)
                break

orientations = {1: 0, 1j: 1, -1: 2, -1j: 3}
def rot(z, o):
    for _ in range(orientations[o]):
        z = (sz - 1 - z.imag) + z.real * 1j
    return z

def solve(part):
    v = {}
    z = g0[0].index('.')
    o = 1
    for i in p:
        if i in 'LR':
            o *= {'L': -1j, 'R': 1j}[i]
            v |= {z: o}
            continue
        for _ in range(int(i)):
            if z + o in g:
                z += o
            elif z + o in w:
                break
            else:
                if part == 1:
                    z0 = z
                    o0 = o
                else:
                    region = (z.real // sz * sz) + 1j * (z.imag // sz * sz)
                    assert region in faces
                    neighbor_pos, neighbor_rot = faces[region][o]
                    z0 = neighbor_pos + rot(z - region, neighbor_rot)
                    o0 = o * neighbor_rot
                    assert z0 in g | w
                while z0 in g or z0 in w:
                    z0 -= o0
                z0 += o0
                if z0 in w:
                    break
                z = z0
                o = o0
            v |= {z: o}
    return int((1 + z.imag) * 1000 + 4 * (1 + z.real) + orientations[o])

# print('\n'.join(''.join(c(j + 1j * i) for j in range(len(g0[i]))) for i in range(len(g0))))
print(solve(1)) # 1
print(solve(2)) # 2

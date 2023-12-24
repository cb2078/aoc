p = open('16.txt').read().strip().split('\n')
w, h = len(p[0]), len(p)
assert w == h

def search(light):
    lights = [light]
    visited = set()
    while lights:
        (di, dj), (i, j) = light = lights.pop()

        if light in visited:
            continue
        else:
            visited.add(light)

        match p[i][j]:
            case '.':
                dirs = [(di, dj)]
            case '|' :
                if dj:
                    dirs = [(1, 0), (-1, 0)]
                else:
                    dirs = [(di, dj)]
            case '-' :
                if di:
                    dirs = [(0,  1), (0, -1)]
                else:
                    dirs = [(di, dj)]
            case '/':
                dirs = [(-dj, -di)]
            case '\\':
                dirs = [(dj, di)]
            case _:
                raise Error()

        for di, dj in dirs:
            if i + di not in range(w) or j + dj not in range(w):
                continue
            else:
                lights.append(((di, dj), (i + di, j + dj)))

    return len(set(v[1] for v in visited))

# for i in range(w):
#     print(''.join('.#'[any(v[1] == (i, j) for v in visited)] for j in range(w)))

print(search(((0, 1), (0, 0)))) # p1

lights = ([((0, 1), (i, 0)) for i in range(w)] +
          [((1, 0), (0, j)) for j in range(w)] +
          [((0, -1), (i, w - 1)) for i in range(w)] +
          [((-1, 0), (w - 1, j)) for j in range(w)])
print(max(map(search, lights))) # p2

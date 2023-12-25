p = [list(map(int, l)) for l in open('17.txt').read().strip().split('\n')]
w, h = len(p[0]), len(p)
assert w == h

import heapq
def solve(part):
    visited = set()
    queue = [(0, 0, (di, dj), (0, 0)) for di, dj in [(1, 0), (0, 1)]] # (dst, count, (di, dj), (i, j))
    while queue:
        dst, count, dr, (i, j) = node = heapq.heappop(queue)
        if (i, j, *dr, count) in visited:
            continue
        else:
            visited.add((i, j, *dr, count))
        if (i, j) == (w - 1, w - 1):
            return dst
        drs = [dr] if count < 4 and part == 2 else [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for di, dj in drs:
            # out of bounds
            if i + di not in range(w) or j + dj not in range(w):
                continue
            # travelled too far in one direction
            next_count = count + 1 if (di, dj) == dr else 1
            if part == 1 and next_count > 3 or part == 2 and next_count > 10:
                continue
            if di and -di == dr[0] or dj and -dj == dr[1]:
                continue
            heapq.heappush(queue, (dst + p[i + di][j + dj],
                                   next_count,
                                   (di, dj),
                                   (i + di, j + dj)))
    raise AssertionError()

print(solve(1)) # 986 1000 too high
print(solve(2))

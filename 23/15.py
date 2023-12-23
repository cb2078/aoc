p = open('15.txt').read().strip().split(',')

def f(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h

print(sum(map(f, p))) # p1

boxes = [[] for _ in range(256)]
for s in p:
    t = s[-1] if s[-1] == '-' else s[-2]
    l = s[:-1] if t == '-' else s[:-2]
    h = f(l)
    if t == '-':
        for i in range(len(boxes[h]))[::-1]:
            if boxes[h][i][0] == l:
                del boxes[h][i]
    else:
        lens = (lambda x: (x[0], int(x[1])))(s.split('='))
        for i in range(len(boxes[h])):
            if boxes[h][i][0] == l:
                boxes[h][i] = lens
                break
        else:
            boxes[h].append(lens)
    # print(s)
    # for i in range(256):
    #     if boxes[i]:
    #         print(i, boxes[i])
    # print()

print(sum((i + 1) * (j + 1) * lens[1]
          for i, b in enumerate(boxes) for j, lens in enumerate(b)))

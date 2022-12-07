cmds = [cmd.split() for cmd in open('07.txt').read().strip().split('\n')]
from collections import defaultdict
tree=defaultdict(int)
path=('/',)

for cmd in cmds:
    match cmd:
        case ['$', 'cd', name]:
            match name:
                case '/':
                    path = path[:1]
                case '..':
                    path = path[:-1]
                case _:
                    path += (name,)
        case ['$', 'ls']:
            pass
        case ['dir', name]:
            pass
        case [size, name]:
            for i in range(len(path)):
                tree[path[:i + 1]] += int(size)

# print({k[-1]: v for k, v in tree.items()})
print(sum(v for v in tree.values() if v <= 100000)) # 1

used = tree[('/',)]
tot = 70000000
needed = 30000000
print(min(v for v in tree.values() if tot - used + v >= needed)) # 2

s:str
from math import prod

def p():
    global s
    
    def r(n):
        global s
        v = int(s[:n], 2)
        s = s[n:]
        return v

    if len(s) <= 3 + 4:
        return 0
    V = r(3)
    T = r(3)
    if T == 4:
        x = 0
        while r(1) == 1:
            x += r(4)
        x += r(4)
        return x
    else:
        I = r(1)
        if I == 0:
            L = r(15)
            S = s
            a = []
            while len(S) < len(s) + L:
                a.append(p())
        else:
            L = r(11)
            a = [p() for _ in range(L)]
        return  +{0: sum,
                  1: prod,
                  2: min,
                  3: max,
                  5: lambda a: a[0] > a[1],
                  6: lambda a: a[0] < a[1],
                  7: lambda a: a[0] == a[1]}[T](a)

for t in (
    # "38006F45291200", # 0
    
    # "EE00D40C823060", # 1
    
    # "8A004A801A8002F478",
    # "620080001611562C8802118E34",
    # "C0015000016115A2E0802F182340", 
    # "A0016C880162017C3686B18A3D4780",

    # "C200B40A82",
    # "04005AC33890",
    # "880086C3E88112",
    # "CE00C43D881120",
    # "D8005AC2A8F0",
    # "F600BC2D8F",
    # "9C005AC2F8F0",
    # "9C0141080250320F1802104A08",

    open('16.txt').read()[:-1],
):
    s = format(int(t, 16), '0' + str(len(t) * 4) + 'b')
    res = p()
    print(t, res)
    print()

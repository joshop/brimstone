f = open("brimstone.mlb").read().split("\n")
n = []
for l in f:
    if l[0] != 'G' and l[0] != 'R':
        n.append(l)
        continue
    else:
        a1 = l[2:6]
        a2 = l[7:11]
        if a1[0] == '0':
            a1 = (hex(int(a1,16)+16)[2:]).zfill(4)
            l = l[:2] + a1 + l[6:]
        if a2[0] == '0':
            a2 = (hex(int(a2,16)+16)[2:]).zfill(4)
            l = l[:7] + a2 + l[11:]
        n.append(l)
        print(l)
open("brimstone.mlb","w").write('\n'.join(n))
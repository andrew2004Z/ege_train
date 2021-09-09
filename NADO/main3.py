data = open('24-s1.txt').readlines()
sp = []
for i in data:
    sp.append(i.count('A'))
temp = data[sp.index(min(sp))]
sp12 = []
slov = {}
for i in temp:
    if i not in slov:
        slov[i] = 1
    else:
        slov[i] += 1
print(sorted(slov))
con = 0
for i in data:
    con += i.count('V')
print(con)
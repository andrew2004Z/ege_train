data = open('k7c-4.txt').readline()
s1 = ['A', 'D', 'F']
s2 = ['C', 'D', 'F']
s3 = ['C', 'D', 'F']
s4 = []
for i in s1:
    for j in s2:
        for x in s3:
            s4.append([i, j, x])
s5 = []
sp = []
for i in s4:
    if i[0] != i[2] and i[1] != i[2]:
        s5.append(f'{i[0]}{i[1]}{i[2]}')
for i in s5:
    data3 = data.replace(i, '1')
    maxx = 0
    m = 0
    for i in data3:
        if i == '1':
            m +=1
        else:
            if m > maxx:
                maxx = m
            m = 0
    sp.append(maxx)
print(sum(sp))
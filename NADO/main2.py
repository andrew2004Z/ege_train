data = open('k7a-3.txt').readline()
maxx = 0
m = 0
for i in data:
    if i in ['A', 'B', 'E', 'F']:
        m += 1
    else:
        if m > maxx:
            maxx = m
        m = 0
print(maxx)
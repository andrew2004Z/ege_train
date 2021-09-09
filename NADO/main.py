data = open('k7c-4.txt').readline()
maxx = 0
c = 0
m = 10
for i in data:
    if i.isdigit() and int(i) < m:
        m = int(i)
        c += 1
    elif i.isdigit():
        print(i)
    else:
        if c > maxx:
            maxx = c
        m = 10
        c = 0
print(maxx)
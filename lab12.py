import numpy as np

stroka = input()
x = int(input())
con=0
y = len(stroka)
newstr = ""
for i in range(y-x+1):
    for j in range(x):
        newstr+=stroka[j+i]
    if i != y-x:
        newstr+=','
fq = newstr.split(',')
c=np.zeros(len(fq))


for i in range(len(fq)):
    c[i] = (fq.count(fq[i]))

for i in range(len(fq)):
    for j in range(len(fq)-1):
        if c[j] < c[j+1]:
            c[j], c[j+1] = c[j+1], c[j]
            fq[j], fq[j+1] = fq[j+1], fq[j]

for i in range(len(fq)):
    if c[i] == c[0]:
        con+=1

popa = con/c[0]
p = np.empty(int(popa), dtype='S'+str(x))
ch = 0
for i in range(int(popa)):
    for j in range (len(fq)):
        if fq[j] != p[0]:
            p[i] = fq[j]
            ch+=1
        if ch>=popa:
            break
oppa=""
for i in range(int(popa)):
    for j in range(x):
        oppa+=chr(p[i][j])
    print(oppa, end = ' ')
    oppa=""

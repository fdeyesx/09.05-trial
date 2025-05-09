def d(x1,y1,x2,y2):
    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def centre(k):
    mn = 10**10
    for i in range(len(k)):
        tx,ty = k[i][0], k[i][1]
        s = 0
        for j in range(len(k)):
            cx,cy = k[j][0], k[j][1]
            s += d(tx,ty,cx,cy)
        if s < mn:
            mn = s
            cntx = tx
            cnty = ty
    return [cntx,cnty]

print('第一：')
k1a = []
k2a = []
odd = []
s = open('27.21.A.txt').readlines()
for r in s:
    r = r.split()
    x,y = float(r[0]),float(r[1])
    if y > - 1 and x < 11.5:
        k1a.append([x,y])
    elif 14 < x < 27:
        if (14.8 < x < 15) and (3.72 < y < 3.8):
            odd.append([x,y])
        else: k2a.append([x,y])

x1,y1 = centre(k1a)
x2,y2 = centre(k2a)

print(abs( ((x1+x2)/2) * 10_000 ))
print(abs( ((y1+y2)/2) * 10_000 ))

print('第二：')
k1b = []
k2b = []
k3b = []
k4b = []
odd = []
s = open('27.21.B.txt').readlines()
for r in s:
    r = r.split()
    x,y = float(r[0]),float(r[1])
    if y > - 10 and x < -10: k1b.append([x,y])
    elif y < -30 and x < 0: k2b.append([x, y])
    elif 0 < x < 94:
        if y > 0: k3b.append([x, y])
        else: k4b.append([x, y])

x1,y1 = centre(k1b)
x2,y2 = centre(k2b)
x3,y3 = centre(k3b)
x4,y4 = centre(k4b)

print(abs( ((x1+x2+x3+x4)/4) * 10_000 ))
print(abs( ((y1+y2+y3+y4)/4) * 10_000 ))

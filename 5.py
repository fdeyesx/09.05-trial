def f(n):
    s = ''
    while n!=0:
        s = str(n%6) + s
        n//=6
    return s

def main(n):
    s1 = f(n)
    s1 = s1 + s1[-1]
    s2 = bin(int(s1,6))[2:]
    s2 = s2 + s2[-1]
    return int(s2,2)

a = []
for n in range(1,1000):
    r = main(n)
    if r < 344:
        a.append(r)
print(max(a))

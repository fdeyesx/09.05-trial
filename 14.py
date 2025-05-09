def f(n):
    s1 = ''
    while n!=0:
        s1 = str(n%5) + s1
        n //= 5
    return s1

a = []
mx = 0
for x in range(2,2025+1):
    sm = 5**2025 + 5**200 - x
    s = f(sm)
    r = s.count('4')
    if r > mx:
        a = []
        mx = r
        a.append(x)
    elif r == mx:
        a.append(x)
print(max(a))

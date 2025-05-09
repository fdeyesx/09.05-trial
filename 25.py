df = set()
for n in range(1, 1_000_000+1):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    if len(d) == 0:
        df.add(n)
k=0
for n in range(401_219 + 1, 1_000_000):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    if len(d) > 2:
        M = 0
        for j in d:
            if j in df:
                M += int(j)
        if M%17 == 0:
            if M%10 == 4:
                k+=1
                print(n,M)
                if k == 7:
                    break


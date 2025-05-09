from functools import lru_cache

@lru_cache()
def f(n):
    if n < 2: return n
    if n%2 == 0: return f(n/2) + 1
    return f(3*n + 1) + 1

k=0
for i in range(1,100_000 + 1):
    if f(i) == 16:
        k+=1
print(k)

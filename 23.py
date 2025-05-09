def f(n,e):
    if n == e: return 1
    if n > e: return 0
    if n == 6: return f(n+2,e)+f(n+5,e)
    return f(n+2,e)+f(n+5,e)+f(n**2,e)

print(f(4,36))

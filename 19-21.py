#for the 19th - in function you need to change 'all' to 'any'. for the others it stays the same as at 1st.

def f(s1,s2,m):
    if s1+s2 >= 52 : return m%2 == 0
    if m == 0: return 0
    h = [f(s1+2,s2,m-1),f(s1*3,s2,m-1),f(s1,s2+2,m-1),f(s1,s2*3,m-1)]
    return any(h) if m%2 != 0 else all(h)

print('19:',[s for s in range(1,46) if not f(5, s,1) and f(5, s,2)])
print('20:',[s for s in range(1,46) if not f(5, s,1) and f(5, s,3)])
print('21:',[s for s in range(1,46) if not f(5, s,2) and f(5,s,4)])


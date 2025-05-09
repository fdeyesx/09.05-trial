from itertools import product
k = 0

for i in product('012345678',repeat = 7):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('2') == 0:
            if len(s) == len(set(s)):
                for j in '0468':
                    s = s.replace(j,'+')
                for r in '1357':
                    s = s.replace(r,'-')
                if '++' not in s and '--' not in s:
                    k+=1
print(k)

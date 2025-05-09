s = open('24.txt').readline()
#s = 'ABSDGARHETBABDAHDTAB'
p = ''
mn = '1'*10000000
for j in 'AEIOUY':
    s = s.replace(j,'+')
for l in 'BCDFGHJKLMNPQRSTVWXZ':
    s = s.replace(l,'-')

for i in s:
    p += i
    if p.count('--+') >= 500:
        if len(p) < len(mn):
            mn = p
            p = ''
print(len(mn))

for a in range(1,2000):
    d = set()
    for x in range(1,4000):
        f = (x&1097 == 0) <= ((x&2047 != 0) <= (x&a !=0))
        d.add(f)
    if False not in d:
        print(a)
        break

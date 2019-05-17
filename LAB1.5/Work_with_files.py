import glob
l = glob.glob("C:\\PY_WORK\\*.txt")
L = []
for x in l:

    f = open (x)
    for a in f:
        if "ip address" in a:
            s = a.strip()
            L.append(s)



            for d in L:
                j = list(set(list(L)))


                for k in j:
                    r = k.replace('ip address', '')
                    g = r.replace('dhcp', '')
                    p = g.replace('no', '')

                    print(p)

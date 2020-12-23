x = [5,3,8,7]
e = []
for a in x:
    for b in x:
        for c in x:
            if a!=b!=c:
                k = 24 - a - b - c
                print(f"{a}+{b}+{c}+k=24\nk={k}\n")
                if k not in e:
                    e.append(k)
print(len(e))
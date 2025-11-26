input= {"a": 1, "b": 2, "c": 1}
inv={}

for k in input:
    v = input[k]
    if v not in inv:
        inv[v] = [k]
    else:
        inv[v].append(k)
print(inv)
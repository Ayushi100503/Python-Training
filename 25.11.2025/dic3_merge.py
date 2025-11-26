x = {"a": 1, "b": 2} 
y = {"b": 3, "c": 4}
merge = {}
for k in x:
    merge[k] = x[k]

for k in y:
    if k in merge:
        merge[k] = [merge[k],y[k]]
    else:
        merge[k] = y[k]
print(merge)
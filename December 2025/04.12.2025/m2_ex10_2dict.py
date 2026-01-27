d1 = {"a":10, "b":20, "c":30}
d2 = {"b":5, "c":15, "d":40}
combined = d1.copy()
for k, v in d2.items():
    combined[k] = combined.get(k, 0) + v
print(combined)
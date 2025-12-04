pairs = [("a",1), ("b",2), ("a",3), ("b",4)]
result = {}
unique = True
keys = [k for k, _ in pairs]
if len(keys) == len(set(keys)):
    result = dict(pairs)
else:
    unique = False
print(result if unique else "Error: Duplicate keys found")

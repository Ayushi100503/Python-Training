prices = [100, 200, 300, 400,300, 500, 100, 800, 200]
print(prices)
seen = set()
result = []
for p in prices:
    if p not in seen:
        seen.add(p)
        result.append(p)
print(result)
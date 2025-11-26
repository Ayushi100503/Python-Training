items = {"pen":200, "bag":550, "book":100, "shoes":120, "bottle":80}
new_items = {}
for k in items:
    if items[k]>=100:
        new_items[k] = items[k]
print(new_items)
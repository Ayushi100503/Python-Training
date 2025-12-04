marks = {"A":98, "B":89, "C":88, "D":87, "E":86}
top3 = sorted(marks.items(), key=lambda x: x[1], reverse=True)[:3]
print(top3)
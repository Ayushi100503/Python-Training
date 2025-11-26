marks = {"A": 85, "B": 92, "C": 78, "D": 92}

max_value = -1
for v in marks.values():
    if v>max_value:
        max_value = v
    
for k in marks:
    if marks[k] == max_value:
        print(k)
    
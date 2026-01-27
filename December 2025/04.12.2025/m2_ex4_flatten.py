nested = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for sub in nested for x in sub]
print(flat)
t = (10, (20, 30), (40, (50, 60)))
def print_tuple(x):
    for i in x:
        if isinstance(i, tuple):
            print_tuple(i)
        else:
            print(i)
print_tuple(t)
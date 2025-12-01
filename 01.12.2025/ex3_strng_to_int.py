def int_convert(s):
    try:
        return int(s)
    except ValueError:
        return "invalid integer"
print(int_convert("012"))
print(int_convert("abc"))
try:
    value = int("50")
except ValueError:
    PRINT("invalid conversion")
else:
    print("conversion successful", value)
    
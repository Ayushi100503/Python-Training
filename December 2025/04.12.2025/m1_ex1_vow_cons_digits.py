s = input("Enter a string: ")
vowels = "aeiouAEIOU"
v_count = c_count = d_count = 0
for ch in s:
    if ch.isdigit():
        d_count += 1
    elif ch in vowels:
        v_count += 1
    else:
        c_count += 1

print("vowels: ", v_count)
print("consonant: ", c_count)
print("digits: ", d_count)
s = input("Enter a sentence: ").split()
for i in range(len(s)):
    if i%2 == 1:
        s[i] = s[i][::-1]
print("".join(s))
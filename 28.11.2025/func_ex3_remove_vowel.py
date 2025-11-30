def remove_vowel(text):
    vowel = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowel:
            result += ch
    return result
print(remove_vowel("Have a nice day"))
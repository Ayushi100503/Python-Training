def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for w in words:
        if len(w)>len(longest):
            longest = w
    return longest
print(longest_word("Python programming is interesting."))
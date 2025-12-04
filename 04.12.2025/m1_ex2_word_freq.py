def word_freq(sentence):
    words = sentence.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
s = input("Enter a sentence: ")
freq = word_freq(s)
print(freq)
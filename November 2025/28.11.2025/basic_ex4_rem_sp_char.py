import re

text = "hello@world! welcome to python 123"
clean_text = re.sub(r"[^a-zA-Z0-9]+", " ", text)
print("original_text", text)
print("clean_text", clean_text)
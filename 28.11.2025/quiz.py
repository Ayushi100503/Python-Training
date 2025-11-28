make_question = lambda i, q: f"Q{i}, {q}\nAnswer:             \n"
def generate_quiz(questions, filename="quiz.txt"):
    with open(filename, "w") as f:
        for i, q in enumerate(questions,1):
            f.write(make_question(i, q))
    print(f"{filename} created")

questions = [
    "What is the capital of China?",
    "What is the capital of India?",
    "What is the capital of USA?",
    "What is the capital of Japan?"
]
generate_quiz(questions)
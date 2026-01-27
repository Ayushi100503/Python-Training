class book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def is_big(self):
        return self.pages > 300
    
b = book("Python Guide","A.C", 650)
print(b.is_big()) 
class Book():
    
    def __init__(self,name,author,pages):
        
        self.name = name
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.name} is written by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("book object is deleted ")
        
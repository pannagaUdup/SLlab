class student:
    def __init__(self):
        self.name=input("enter your name")
        self.age=int(input("enter your age"))
        self.marks=[]
    def accept(self):
        for i in range(3):
            self.marks.append(input("Enter subject "+str(i+1)+" marks")) #',' comma separation wont work only use'+'
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
s=student()
s.accept()
s.display()

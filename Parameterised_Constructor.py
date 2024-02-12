# Parameterised constructor- Constructor with parameter

class Course:
    def __init__(self,name,ratings,duration):   # This is parameterised constructor. parameters and variable after = must be same
        self.n=name
        self.r=ratings
        self.d=duration

c1=Course('Java',[1,2,3,4,5],50)
print("Course name is:",c1.n)
print("Course Ratings are:",c1.r)
print("Course duration is:",c1.d,"days")
print()

c2=Course('Python',[1,2,3,4,5],60)
print("Course name is:",c2.n)
print("Course Ratings are:",c2.r)
print("Course duration is:",c2.d,"days")

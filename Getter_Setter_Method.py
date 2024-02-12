# Getter and Setter methods
# getter method:-> used to get or return value also known as Accessor method
# setter method:-> used to set or modify values also known as Mutator method

# create a class Programmer having 3 fields-name,salary,technologies

class Programmer:
    def SetName(self,n):
        self.name=n

    def GetName(self):
        return self.name

    def SetSalary(self,sal):
        self.salary=sal

    def GetSalary(self):
        return self.salary

    def SetTechnologies(self,tech):
        self.technologies=tech

    def GetTechnologies(self):
        print(self.technologies)

p1=Programmer()
p1.SetName('Sayali')
p1.SetSalary(35000)
p1.SetTechnologies(['Python','Sql','Java'])

print("Name is:",p1.GetName())      # There is no print stat inside get method so, we write print here
print("Salary is:",p1.GetSalary())  # There is no print stat inside get method so, we write print here
p1.GetTechnologies()    # Here print stat is inside get method so no need to write print

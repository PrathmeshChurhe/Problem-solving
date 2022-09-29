class salary: # base class or parent class
     def __init__(self,name,batch,education):  # properties of class salary
          self.name=name
          self.batch=batch
          self.education=education

     def names(self): # methods of class salary
          print('name is '+self.name)     

class employee(salary): #inherited class or child class of salary
     def __init__(self, name, batch, education,year): #init property of class employee
          super().__init__(name, batch, education) # init property of super class i.e salary 
          self.year=2022
     
     def welcome(self):
          print("Name is :",self.name,"Year :",self.year)
"""s1=salary(name='Sam',batch='morning',education='degree')

print('Name of employee :',s1.name,'\nBatch :',s1.batch,'\nEducation :',s1.education)"""

p1=employee('sam',2,'degree',2022)  # object of class employee
p1.names()    # names method called using object p1
print(p1.year)
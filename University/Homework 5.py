class Employee:
   'Common base class for all employees'
   empCount = 0
   __compID = 10 # data hiding, only visible if explicitly called

   def __init__(self, name, salary):  # constructor / initializer
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "destroyed"

   def displayName (self):
        print "Name : ", self.name,
        
   def displaySalary(self):
        print ", Salary: ", self.salary,
      

#creating objects by instantiation
emp1 = Employee('e1', 2000)
emp2 = Employee('e2', 4000)

#accessing attributes of object
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayName()
emp1.displaySalary()
print "Total Employees %d" % Employee.empCount
print "Company ID %d" % emp1._Employee__compID
print emp1.name
print  emp1.salary
#print "Company ID %d" % emp1.__compID
#print Employee.__compID



#add remove or modify attributes
emp1.age = 7  # Add an attribute.
emp1.age = 8  # Modify attribute.
#del emp1.salary  # Delete attribute.


print hasattr(emp1, 'age')    # Returns true if attribute exists
print getattr(emp1, 'age')    # Returns value of attribute
setattr(emp1, 'age', 9) # Set attribute at 8
#delattr(empl, 'age')    # Delete attribute

del emp2   #destroyes the object and also calls the distructor


#built in class attributes
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__





#class inheritance and overiding methods

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def orMethod(self):
      print 'Calling or method from parent'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

   def orMethod(self):
      print 'Calling or method from CHILD'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
c.orMethod()         # child calls overriden method


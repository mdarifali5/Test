
class Employee_Salary:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def __mul__(self,other):
    return self.salary*other.days

class Employee_Days:
  def __init__(self,name,days):
    self.name=name
    self.days=days

es=Employee_Salary("Arif Ali",700)
ed=Employee_Days("Arif Ali",30)
print(es*ed)

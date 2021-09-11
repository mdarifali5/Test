
''' ----------------------------   POLYMORPHISM   ----------------------------


 Poly         means --> Many
 Morph        means --> Forms
 Polymorphism means --> Many Forms

 Example-1 :  Yourself is the best example of Polymorphism. In front of your parents you will have one-type of behaviour and with friends you will have another type of behaviour. Same person but different behaviour at different places.
 Example-2 :  The  +  operator acts as concatenation as well as arithmetic operation.
 Example-3 :  The  *  operator acts as multiplication as well as repetition operator.
 Example-3 :  The same method with different implementations in Parent-Class and Child-Classes. (overriding).


 ***** Related to  Poymorphism  the following 4 topics are important:

 (1). Duck Typing

 (2). Overloading:
          (a) Operator Overloading
          (b) Method Overloading
          (c) Constructor Overloading

 (3). Overriding:
          (a) Method Overriding
          (b) Constructor Overriding




 --(1)--------------------------  DUCK  TYPING  ------------------------------

 In Python we cannot specify the type explicitly (in a clear and detailed manner). Based on provided value at runtime, the type will be considered automatically. Hence Python is considered as
 Dynamically Typed Programming Language.

 def f1(obj):
   obj.talk()


 *** Question:  What is the Type of  obj? We cannot decide at the Beginning.
                At Runtime we can  Pass  any Type.
                Then how we decide the Type?

     Ans: At Runtime --- if it walks like a duck and talks like a duck, it must be a duck.
          Python follows this principle.
          This is called  Duck Typing  Philosophy of Python.                         '''


# class Duck:
#   def talk(self):
#     print("Quack Quack....")
# class Dog:
#   def talk(self):
#     print("Bow Bow...")
# class Cat:
#   def talk(self):
#     print("Meow Meow...")
# def f1(obj):
#   obj.talk()
# x = Duck(), Dog(), Cat()
# for obj in x:
#   f1(obj)
#   # obj.talk()





'''      The problem with this approach is that if  obj  doesn't contain  talk() method  then we will get
 Attribute Error.        '''


# class Duck:
#    def talk(self):
#      print("Quack Quack....")
# class Dog:
#    def bark(self):
#      print("Bow Bow...")
# def f1(obj):
#      obj.talk()
# d=Duck()
# f1(d)
# d=Dog()
# f1(d)


'''    AttributeError: 'Dog' object has no attribute 'talk'


--> But we can solve this by using  hasattr()  function.
--> hasattr(obj,"attributename")        
--> attributename can be  "Method Name" or "Variable Name".



*** Demo Program with hasattr() function :                                '''


class Duck:
  def quack(self):
    print("Quack Quack....")
class Human:
  def talk(self):
    print("Hello hi....")
class Dog:
  def bark(self):
    print("Bow Bow...")
def combine(obj):

    

















def f1(obj):
  if hasattr(obj,"quack"):
    obj.quack()
  elif hasattr(obj,"talk"):
    obj.talk()
  elif hasattr(obj,"bark"):
    obj.bark()
d=Duck()
d.quack()
h=Human()
h.talk()
g=Dog()
g.bark()





'''   (2) ------------------------  OVERLOADING  ----------------------------


 We can use same operator or methods for different purposes.

 Example-1:   + operator can be used for Arithmetic addition and String Concatenation.
              print(10+20)          --> output is: 30
              print("Arif"+"Ali")   --> output is: Arif Ali

 Example-2:   * operator can be used multiplication and string repetition purposes.
              print(10*20)          --> output is: 300
              print("Arif"*3)       --> output is: ArifArifArif

 Example-3:   We can use deposit() method to deposit cash or cheque or dd
              deposit(cash)
              deposit(cheque)
              deposit(dd)

 There are 3 types of Overloading:
       1. Operator Overloading
       2. Method Overloading
       3. Cnstructor Overloading



 --------------- (1). Operator Overloading ----------------

 --> We can use the same operator for multiple purposes, which is nothing but Operator Overloading.
 --> Python supports Operator Overloading. 
 --> Example: + operator can be used for Aritmetic addition and also Sring concatenation.
 --> * operator can be used in multiplication and string repetition purposes.


 Demo Program to use + operator in Class Objects:

 class Book:
   def __init__(self,pages):
     self.pages=pages
 b1=Book(100)
 b2=Book(200)
 print(b1+b2)

 TypeError: unsupported operand type(s) for + : 'Book' and 'Book'

 --> We can Overload + operator for our Book Class Objects.
 --> For every operator Magic Methods are available. To have to overload we have to override that Method in our Class  
 --> Internally the + operator is implemented by using __add__() method. This method is called  Magic Method  for + operator.                                                       '''



# class Book:
#   def __init__(self,pages):
#     self.pages=pages
#   def __add__(self,other):
#     return self.pages + other.pages
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)


''' The following are the list of operators and corresponding magic methods.

 1)    +   --> object.__add__(self,other)
 2)    -   --> object.__sub__(self,other)
 3)    *   --> object.__mul__(self,other)
 4)    /   --> object.__div__(self,other)
 5)   //   --> object.__floordiv__(self,other)
 6)    %   --> object.__mod__(self,other)
 7)   **   --> object.__pow__(self,other)
 8)   +=   --> object.__iadd__(self,other)
 9)   -=   --> object.__isub__(self,other)
 10)  *=   --> object.__imul__(self,other)
 11)  /=   --> object.__idiv__(self,other)
 12) //=   --> object.__ifloordiv__(self,other)
 13)  %=   --> object.__imod__(self,other)
 14) **=   --> object.__ipow__(self,other)
 15)   <   --> object.__lt__(self,other)
 16)  <=   --> object.__le__(self,other)
 17)   >   --> object.__gt__(self,other)
 18)  >=   --> object.__lt__(self,other)
 19)  ==   --> object.__eq__(self,other)
 20)  !=   --> object.__ne__(self,other)                                 '''


# class Student:
#   def __init__(self,marks):
#     # self.name=name
#     self.marks=marks
#   def __gt__(self,other):
#     return self.marks > other.marks
#   def __le__(self,other2):
#     return self.marks <= other2.marks

# s1=Student(100)
# s2=Student(200)
# print(s1 > s2)
# print(s1 <= s2)
# print(s1 < s2)
# print(s1 == s2)



# class Employee:
#   def __init__(self,name,salary):
#     self.name=name
#     self.salary=salary
#   def __mul__(self,other):
#     return self.salary*other.days

# class TimeSheet:
#   def __init__(self,name,days):
#     self.name=name
#     self.days=days

# e = Employee("Arif", 500)
# t = TimeSheet("Arif", 25)
# print(e*t)

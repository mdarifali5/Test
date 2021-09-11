''' -------------------- Types of Inheritance  ---------------------

1. Single Inheritance
2. Multil Level Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance
6. Cyclic Inheritance



1. Single Inheritance:
   The concept of inheriting the properties from one-class to the another-class is called as  "Single Inheritance".
             A <--- B                                      '''
#
# class A:
#   def m1(self):
#     print("This is Parent Method")
# class B(A):
#   def m2(self):
#     print("This is Child Method")
# c=B()
# c.m1()
# c.m2()



'''   --------     2. Multil Level Inheritance:    ---------
   The concept of inheriting the properties from multiple classes to a single class is called as  "Multil Level Inheritance"
         A <----- B <---- C                                                          '''



# class A:
#   def m1(self):
#     print("This is Parent Method")
# class B(A):
#   def m2(self):
#     print("This is Child Method")
# class C(B):
#   def m3(self):
#     print("This is Sub-Child Method")
# b=B()
# b.m1()
# b.m2()
# c=C()
# c.m1()
# c.m2()
# c.m3()




''' 3. Hierarchical Inheritance:
       The concept of inheriting properties from  one-class  into  multiple-classes which are present at same level is known as
       "Hierarchical Inheritance".
              B ----> A <---- C                           '''


# class A:
#   def m1(self):
#     print("This is Parent Method")
# class B(A):
#   def m2(self):
#     print("This is Child-1 Method")
# class C(A):
#   def m3(self):
#     print("This is Child-2 Method")
# c1=B()
# c1.m1()
# c1.m2()
# c2=C()
# c2.m1()
# c2.m3()



'''
4. Multiple Inheritance:
   The concept of inheriting properties from  multiple-classes  into  single-class  at a time is known as
   "Multiple Inheritance".
        B <---- A ----> C                                          '''


# class A:
#   def m1(self):
#     print("This is Parent-1 Method")
# class B:
#   def m2(self):
#     print("This is Parent-2 Method")
# class C(A,B):                           # Here we can also use C(B,A)
#   def m3(self):
#     print("This is Child Method")
# c=C()
# c.m1()
# c.m2()
# c.m3()


# class A:
#   def m1(self):
#     print("This is Parent-1 Method")
# class B:
#   def m2(self):
#     print("This is Parent-2 Method")
# class C:
#   def m3(self):
#     print("This is Parent-3 Method")
# class D(A,B,C):                         # Here we can also use C(C,B,A) or D(C,A,B)
#   def m4(self):
#     print("This is Child Method")
# c=D()
# c.m1()
# c.m2()
# c.m3()
# c.m4()



'''  --> Note: If the same method is inherited from both Parent-Classes, then Python will always consider the order 
               of  Parent-Class in the declaration of the the child classes.                                 '''

# class A:
#   def m1(self):
#     print("This is Parent-1 Method")
# class B:
#   def m1(self):
#     print("This is Parent-2 Method")
# class C(A,B):                           # When we use here C(B,A) it will consider  class B
#   def m3(self):
#     print("This is Child Method")
# c=C()
# c.m1()




# 5. Hybrid Inheritance:
#    The combination of Single, Muliti-Level, Hierarchical and Multiple iheritance is known as  "Hybrid Inheritance".
#    A,B,C  <----  D  <----  E  <----  F  <----  G,H





# 6. Cyclic Inheritance:
   # -- The process of inheriting properties from  one-class  to  another-class  in a cyclic way is called as  "Cyclic Inheritance".
   # -- Since, Python won't support  "Cyclic Inheritance"  hence it is not required.
   # -- Example:

# class A(A): pass
# NameError: name 'A' is not defined





# *** Method Resolution Order (MRO):
#
#     --> In  "Hybrid Inheritance"  the  "Method Resolution Order"  is decided based on  MRO alogorithm.
#     --> This algorithm is also known as  C3  algorithm.
#     --> "Samuele Pedroni"  proposed this algorithm.
#     --> It follows  DLR (Depth First Left to Right)  i.e Child will get more priority than Parent.
#     --> Left Parent will get more priority than Right Parent.
#     --> MRO(X) = X + (MRO(P1),MRO(P2),.....(ParentList))
#
#
#
# *** Head Element  vs  Tail :
#     --> Assume  C1,C2,C3,.....  are classes.
#     --> In the list  C1,C2,C3,C4,C5,.....   C1 is considered as Head Element adn the remaining is conisdered as Tail.
#
#
#
# *** How to Merge:
#     --> Take the Head of the first list.
#     --> If the  Head  is not present in the  Tail  of any other list, then add this head to the result and remove it from the lists in the merge.
#     --> If the  Head  is present in the tail part of any other list, then consider the Head element of the the next list
#         and continue the same process.
#
# Note:  We can find  MRO  of any classes by using  mro()  function.





# --> Demo Program-1 for MRO:                  # reference - page no. 47 (Durga)

#     A  <---  B,C  <---  D
# mro(A) = A, object
# mro(B) = B,A object
# mro(C) = C,A object
# mro(D) = D,C,B,A object


# class A:pass
# class B(A): pass
# class C(A): pass
# class D(B,C): pass
# print(A.mro())
# print(B.mro())
# print(C.mro())
# print(D.mro())





# --> Demo Program-2 for MRO:            Page 48


# mro(A): A,object
# mro(B): B,object
# mro(C): C,object
# mro(X): X,A,B,object
# mro(Y): Y,B,C,object
# mro(P): P,X,A,Y,B,C,object
#
#
#
# *** Finding  mro(P) by using C3 Algorithm:
#
# Formula:    MRO(X) = X + Merge(MRO(P1),MRO(P2),.....ParentList)
#             mro(P) = P + Merge(mro(X), mro(Y), mro(C),XYC)
#                    = P + Merge(XABO,YBCO,CO,XYC)
#                    = P + X + Merge(ABO,YBCO,CO,YC)
#                    = P + X + A + Merge(BO,YBCO,YC)
#                    = P + X + A + Y + Merge(BO,BCO,C)
#                    = P + X + A + Y + B + Merge(O,CO,C)
#                    = P + X + A + Y + B + C + Merge(O,O,O)
#                    = P + X + A + Y + B + C + O
#
#
# Test1.py

# class A: pass
# class B: pass
# class C: pass
# class X(A,B): pass
# class Y(B,C): pass
# class P(X,Y,C): pass

# print(A.mro())
# print(B.mro())
# print(C.mro())
# print(X.mro())
# print(Y.mro())
# print(P.mro())



# Test2.py


# class A:
#     def m1(self):
#         print("This is A class method")
# class B:
#     def m1(self):
#         print("This is B class method")
# class C:
#     def m1(self):pass
#         # print("This is C class method")
# class X(A,B):
#     def m1(self):
#         print("This is X class method")
# class Y(B,C):
#     def m1(self):
#         print("This is Y class method")
# class P(X,Y,C):
#     def m1(self):
#         print("This is P class method")
# p = C()
# p.m1()


# In the above example P class m1 method will be considered.
# If P class does not contain m1 method then as per MRO,  X class will be considered.




# --> Demo Program-3 for MRO:            Page 50


# mro(o) = object
# mro(D) = D,object
# mro(E) = E,object
# mro(F) = F,object
# mro(B) = B,D,E,object
# mro(C) = C,D,F,object
# mro(A) = A + Merge(mro(B),mro(C),BC)
#        = A + Merge(BDEO,CDFO,BC)
#        = A + B + Merge(DEO,CDFO,C)
#        = A + B + C + Merge(DEO,DFO,O)
#        = A + B + C + D + Merge(EO,FO,O)
#        = A + B + C + D + E + Merge(O,FO,O)
#        = A + B + C + D + E + F + Merge(O,O,O)
#        = A + B + C + D + E + F + O


# Test.Py

# class D: pass
# class E: pass
# class F: pass
# class B(D,E): pass
# class C(D,F): pass
# class A(B,C): pass
# print(D.mro())
# print(E.mro())
# print(F.mro())
# print(B.mro())
# print(C.mro())
# print(A.mro())





# ---> super()  Method:
#
#      super() is a bulit-in method which is useful to call the superclass constructors, variables and methods from the child class.



# Demo Program-1 for super():


# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def m1(self):
#         print("a: ", self.a)
#         print("b: ", self.b)
#
# class B(A):
#     def __init__(self,a,b,c,d):
#         super().__init__(a,b)
#         self.c=c
#         self.d=d
#     def m1(self):                       # Here we can also write m1 as m2 or anyo other name
#         super().m1()
#         print("c: ", self.c)
#         print("d: ", self.d)
#
# b = B(10,20,30,40)
# b.m1()



# Demo Program-2 for super():


# class A:
#     def __init__(self):
#         self.a=5
#         self.b=15
#     def m1(self):
#         print("a: ", self.a)
#         print("b: ", self.b)
#
# class B(A):
#     def __init__(self,a,b,c,d):
#         super().__init__()
#         self.c=c
#         self.d=d
#     def m1(self):
#         super().m1()
#         print("c: ", self.c)
#         print("d: ", self.d)
#
# b = B(10,20,30,40)
# b.m1()


# Note: In the above program we are using the  super()  method to call the parent-class and the  m1  method.




# Demo Program-3 for super():

#
# class A:
#     a=10
#     def __init__(self):
#         self.b=20
#     def m1(self):
#         print("Parent Insatnce Method")
#     @classmethod
#     def m2(cls):
#         print("Parent Class Method")
#     @staticmethod
#     def m3():
#         print("Parent Class Method")
# class B(A):
#     c=30
#     def __init__(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
#         super().a            # calling the static variable  a  from the Parent Class
#         print(self.a)
#         print(self.b)
# b=B()

# In this example we are using super() to call various members of Parent Class which are static variable, @classmethod and @staticmethod.





# *** How to Call Method of a Particular Super Class:


# --> We can use the following approaches:
#     1.    A.m1(self)           --> It will call  A class  m1()  method
#     2.    super(D,self).m1     --> It will call m1() method of super class D


# class A:
#     def m1(self):
#         print("A class Method")
# class B(A):
#     def m1(self):
#         print("B class Method")
# class C(B):
#     def m1(self):
#         print("C class method")
# class D(C):
#     def m1(self):
#         print("D class method")
# class E(D):
#     def m1(self):
#         A.m1(self)
#         B.m1(self)
#         C.m1(self)
#         D.m1(self)
#         # E.m1(self)
#         # print("E class method")
# e=E()
# e.m1()



# class A:
#     def m1(self):
#         print("A class Method")
# class B(A):
#     def m2(self):
#         print("B class Method")
# class C(B):
#     def m3(self):
#         print("C class method")
# class D(C):
#     def m4(self):
#         print("D class method")
# class E(D):
#     def m1(self):
#         super(E,self).m2()
#         super(E,self).m3()
#         print("E class method")
# e=E()
# e.m1()




# *** Various Important Points about  super():



# Case-(1):   --> From child class we are not allowed to access parent class instance variables by using  super(). Compulsory we
#               should be use  self  only.
#             --> But we can access parent class static variables by using super()


# class P:
#     a=10
#     def __init__(self):
#         self.b=20
# class C(P):
#     def m1(self):
#         print(super().a)           # we can access parent class static variables by using super()
#         print(self.b)              # Here we should be use  self  only.
#         # print(super().b)         # This is invalid.
# c=C()
# c.m1()




# Case-(2):   --> From child class constructor and instance method, we can access parent class instance method,
#                 static method and class method by using  super()


# class P:
#     def __init__(self):
#         print("Parent Constructor")
#     def m1(self):
#         print("Parent Instance Method")
#     @classmethod
#     def m2(cls):
#         print("Parent Class Method")
#     @staticmethod
#     def m3():
#         print("Parent Static Method")
#
# class C(P):
#     def __init__(self):
#         super().__init__()
#         # super().m1()
#         # super().m2()
#         # super().m3()
#     def m1(self):
#         # super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
# c=C()
# c.m1()




# Case-(3):   --> From child-class, class-method we cannot access parent-class instance method and constructors by using  super()
#                 directly. But indirectly it is possible.
#             --> But we can access parent-class  ---  class-methods and static-methods.

#
# class P:
#     def __init__(self):
#         print("Parent Constructor")
#     def m1(self):
#         print("Parent Instance Method")
#     @classmethod
#     def m2(cls):
#         print("Parent Class Method")
#     @staticmethod
#     def m3():
#         print("Parent Static Method")
#
# class C(P):
#     @classmethod
#     def m1(cls):
#         # super().__init__()           # invalid
#         # super().m1()                 # invalid
#         super().m2()
#         super().m3()
#
# # c=C()                                # invalid
# C.m1()
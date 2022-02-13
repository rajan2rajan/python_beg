
# #if you need help then help('name')

# # if we have to use  ' inside of ' then it wont work to make that work we have to use outer and inner column different.
# # print('this is rajan's laptop)    this is an error.
# print("this is nabins's laptop and this is rajan's laptop")

# # if we have to make square of some digit then we have to use 2*2*2*2= ... for that 2**3
# #  / refers to the new line
# print("home/ sdf/asdf")
# # this shows in new line so for that we need to write inside 
# print(r'sdfagadasdfsa') # this make dont convert the python code

# #-----------------------------------variable------------------------------------------------------------------------

# name= "youtube"
# s= name +"rocks"
# print(s)   # youtuberocks

# name = "rajan" + "5"  #two different type of data cannot add if have to add then it should be of same type
# print(name) 

# name= "youtube" #  here they are present in an array so start from 0 and ends with 6
# # if we want to print single value present in an array 
# name[5]         # it represent +ve value. starts from 0 and ends with e as 6.
# name[-1]        # here we can represent that also in the form on (-) e start with  -1 and y be (-7)

# # if we want to print multiple value then we can use
# print(name [1:5]) # it will print only the value that are present inside the number.
# print(name[-5:])
# # if waant to press backward then we use [::-1]



# #----------------------------------list/tuple/set------------------------------------------------------------------


#  #list []  => it can be of different type int, string .... they are mutable we can add, update, repeate,pop and so on
# #tuple ()=> it is same as list but they are immutable
# #set {} => they are mutable and arrange the data in accending order and doesnot repeate the value if they are repeated.
# if we are passing single tuple then we use (10,) like this
# values=["rajan","navin","sunny", "leon"]
# marks=[1,3,4,2,4,1,5,4]
# same=[values,marks]  # here we have tuples inside the tuples
# print(same)

# values.append(13)  #here we are adding  13 in the end 
# print(same)

# values.insert(5,13)   # here we are using two argument first means address and second means the value we want to put..
# print(same)

# values.remove("leon")   # it will remove the values
# print(values)

# values.pop()
# print(values) # if we use this then the last values means "sunny" wull be remove, we can remove certain number by using certain index too.

# values.pop(1)   # this is how we remove by giving certain index.
# print(values)

# values.extend([10,20,30,40])        # this is how we can insert elements inside the tuples.
# print(values)

# a=min(marks)    # min value inside the array
# print(a)

# a=marks.sort()    # sorting the data in an accending array
# print(a)


# # this all values are mutable(which can be change) they are written insidet  []  
# #  there are also those data that are immutable data cannot be change and those data are represented as inside {}

# a = {9,8,7,6,5,4,3,3,2,1,45,34,345} # we get the same value but we donot get the value in same order as given we can get the value in arrange order and delete the repeating number.
# print(a)


# #zip function(what if we have to combine two different data in single tuples or dict)
# user_id=["user1 ",'user 2 ', 'user 3']
# names =['rajan ', ' bhandari ', 'america ']
# print(list(zip(user_id , names)))  # zip is iterable only so we need to define which part we want to convert
# print(dict(zip(user_id, names )))

# #-------------------------------------------data type------------------------------------------------------------------

# #  Numeric type:- int , float bool(true as 1 and false as 0) , complex( a+bj    : we have to use j in python where as in formula there is i)
# #         we can convert the value float and integer into vice versa   for that 
# a=5.0
# int(a)   # if want to convet any data then change as want
# print(type(a))   # if you want to know the type then use  type to represent


# #sequence:- list , tuple , set , string , Range;
# a=range(0,10)
# print(type(a))
# print(list(a))

# #dictionary:-   they are just used to access the value present indside the disctionary
# s= {'kiran':'samsung','buba':'redimi','rahul':'oneplus'}
# a=s.keys()
# b=s.values()
# print(a)   
# print(b)
# c=s['kiran']   # if we want to access the value of certain key then follow this method
# print(c)
# d=s.get('buba')  # another method is using get function
# print(d)


# #-------------------------------------------operators------------------------------------------------------------------
# #  Relation operator:- comparing two numbers
# #a>b,a<b,a==b,a<=b,a>=b , a!=b, and the data are shown in true and false statement.
# #a<3 and b>5 , a<3 or b>5

# #-------------------------------------------binary and decimal formate------------------------------------------------------------------
#   #converting number to binary, octal , hexadecimal  and decimal is easy 

# a=25
# d=bin(25)  # converting to binary
# print(d)

# c= 0b111111 # converting binary to decimal
# print(c)

# a=oct(45245275)  # converting in octa
# print(a)

# a=hex(3534345453)  # converting in hexa
# print(a)

# #-------------------------------------------bit wise operator------------------------------------------------------------------
# #complement ~  :- when we use this suppose 5 then we convert that number into bit and if there is 1 change it into 0 viceversa
#         #  after converting that number change that number into decimal again then the number is shown as result .
#         #   we use 2's complement to change number into decimal  2's = 1's comp +1;

# # And and OR:-  change number into bit in And (&) operation if both 1 then 1 other wise 0
#    #           : In OR(|) if anything in two number is 1 then result is 1.

# # XOR(^) :- watch youtube
# # left shift and Right shift

# #-------------------------------------------math function-----------------------------------------

# x=sqrt(25) # if we use like this then it will show the error in the form of complex number so we have to import the math function
# print(x)  #5+0j  

# import math
# from traceback import print_tb  # here we import all the function of math so if we want to import certain part then  
# x=math.sqrt(25) 
# print(x)


# import math as m
# x=m.sqrt(25)
# print(x)

# from math import sqrt, pow
# x=pow(4,5)
# print(x)


# #-------------------------------------------if else condtion-----------------------------------------------------
# # we use for if and else condtion when we need true or false for certain condtion
# # we can use if condtion inside if condtion and if we have to  use elseif then we use elif for that 

# x=2
# if x==1:
#     print("it is equal to 1")
# elif x==2:
#     print("it is equal to 2")
# elif x==3:
#     print("this is equal to 3")

# # we can use if condtion inside if condtion

# x=11
# a=x%5
# if a>=1:
#     print("this is not divible by 5, it is only div by")
#     if a==1:
#         print("reminder is 1")
#     elif a==2:
#         print("reminder is 2")
#     elif a==3:
#         print("the reminder is 3")
#     elif a==4:
#         print("reminder is 4")
# else:
#     print("this is divisible")

# #-------------------------------------------while loop condtion---------------------------------------------------------------
# # we use while loop when we dont know the fix number
# #while doing operation with while just remember week where 1'st day is sunday and clock starts with 1,2,3,.. 
# #tomorrow 2nd day where again it start with fresh time 1 same things happen in while condtion

# i=1    
# while i<=20:
#     print(i)
#     i=i+2



# i=1
# while i<=5:
#     print("rajan",end=" ") # end =" "  it makes start with same line 
#     j=1
#     while j<=5:
#         print("rocks",end=" ")
#         j=j+1
#     i=i+1 
#     print()



# i=0
# while i<=10:
#     print(i)
#     i=i+1
#     if i==8:
#         break
# print("program is terminated")

# #-------------------------------------------for loop---------------------------------------------------------------
# #if we know exactly how many times you want to test a condition (e.g. 10), then you'd use a for loop instead 
# #suppose there is an array and we want to print one by one for that we use for loop

# x=["rajan", "ss",23.4,23.24234,234]
# #       0   1      2    3       4
# for i in x:     # here i refers to that array preesnt in list and that array is present inside the list
#     print(i)



# x="rajan"
# for i in x:     # here i refers to that array that is represented as string
#     print(i)

# for i in range(10 , 20 , 2):  # if want to print inside the range() with the difference between then we use
#     print(i)



# for i in range(1, 50):
#     if i%5!=0 :   # dont use == it is not valid
#       print(i)




# #-------------------------------------------using break and continue---------------------------------------------------------------

# x= int(input("how many candy you want"))
# print("you want ",x)

# i=1
# while i<=x:
#     print("candy")
#     i=i+1
#     if i>=10:
#         print("toomuch amount")
#         break

# print("finish")


# # ------------------making simple vanding machine
# a=5
# x=int(input("how many candies you want"))
# if x<=a:
#     i=1
#     while i<=x:
#         print("candy")
#         i=i+1
# else:
#     i=1
#     while i<=a:
#         print("candy")
#         i=i+1

#     print("sorry no sufficent candny")
#     m=x-a
#     print("your money", m)


# # ------------------making simple vanding machine another method using break
# av=5
# x=int(input("how many candies you want "))
# i=1
# while i <=x:
#     if  i>av:
#         break
#     print("candy")
#     i=i+1
# print("bye")

# for i in range(1,101):
#     if i%3 and i%5 !=0:
#         print(i)


# #-------------------------------------------pattern solving---------------------------------------------------------------

# for j in range(5):
#     for i in range(5):
#         print("#", end=" ")
#     print()
#     print()



# n=10
# for i in range(n):
    
#     for j in range(i+1):
#         print("#",end=" ")
#     print()



# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("#", end=" ")
#     print()




# #-------------------------------------------function--------------------------------------------------------------
# #here to make a certain function we use def (whice means defining a function)

# #syntax:

# def my_function(child1 ,child2 , child3):
#     print("the first name  of the child is  "+ child1)

# my_function("ding","dong","dang")



# # if we dont know how many argument will be pass in the parimeter the we use ** before the parameter name
# def my_function(**kids):
#     print("his last name is "+ kids["lname"]) # here we dont know  how many parameter there may be use so we use like this 

# my_function(fname="rajan", lname="bhandari")


# def recursion(n):
#     if n>0:
#         result= n*(n-1)
#         return result
#     else:
#         print("the fact is 1")
# x=int(input("what number you want to find the recursion"))
# print(recursion(x))


# # define a function take any no of list contaning number [1,2,3] , [4,5,6]   return average (1+4+7)/3,(2,5,8)/3  , (3,6,9)/3
# def average_number(l1 , l2 ):
#     for pair in zip(l1,l2):
#         average=[sum(pair)/len(pair)]
#         print(average)

# average_number([1,2,3] , [4,5,6])
# # if we have only two numbers then we can use like this but if we have multiple then

# def average_number(*args):
#     for pair in zip(*args): # here we are unziping the list for that print zip then you will understand..
#         average=[sum(pair)/len(pair)]   # print(pair)
#         print(average)

# average_number([1,2,3] , [4,5,6] , [7,8,9])
# # if want to perform same process using lameda( this is anpnymous function where we define all the things in same line)

# average_finder=lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
# print(average_finder([1,2,3] , [4,5,6] , [7,8,9]))


# #---------------------------------------lambda / Nested function--------------------------------------------------------------
# # lamda function with filter
# # we can define a whole function in singel line using lambda which are also called anonymous function
# nums=[43,65,32,5,56,34,45]
# def is_even(n):
#     return n%2==0
# x=list(filter(is_even,nums))
# print(x) 

# if this function we have to convert using lamda then (lambda  variable_name(parameter) : operation)

# nums=[43,65,32,5,56,34,45]
# x=list(filter(lambda n : n%2==0 , nums))
# print(x) 

# # lamda function with map
# #map:-take some value do some operation on that and return the values

# nums=[43,65,32,5,56,34,45]
# def mapping(n):
#     return n+2

# x=list(map(mapping,nums))
# print(x)

# # using lambda
# nums=[43,65,32,5,56,34,45]
# x=list(filter(lambda n : n%2==0 , nums))
# print(x)


# # when we call fucntion inside the function the we use nested function
# # it doesnot enter inside the another function until it is called by another.it means at first it run disp() function then print the function and only it run show() when it is  called 
# #syntax:-
# def disp():
#     def show():
#         print("show function")
#     print("this is show function")
#     show()

# disp()


# #-----------------------------------------------------------------Modules(files)-----------------------------------------------------------------------

# # there are different ways to get the modules ..generally we use module when we have to import function from another folder for that we use 

# # import module_name ( just name of the module of given name)
# # import mddule_name as k( sometimes we have large name of module so we change that long name mmodule in to k )
# # form module_name import * ( it means we are goint to import all the things that are presernt inside that another folder) 

# # suppose this is another module build by me. and have funciton data, time
# # to use certain function we use . operator  
# calendar.time()  # this is how we access the function of certain folder.

#  c.time()#  if we donot want to type type calander again again we can we can use c also

# from calendar import *  # this means import all the function ,variable , class that are present insdie that module (files)
 


# #---------------------------------------------------------------------------object/ class--------------------------------------------------------

# # everything is an object human is an object, he is using laptop that all are bbject ....object have two things they are  Atributes and behaviour
# # Attrubutes :- age ,height ,data ,name ....... if we have to define it we use variables
# # Behaviour :- talking , walking if we have to  define methods( function in object oriented programming are called methods)

# # class :- where object has  been designed those are called class

# class Rajan:
#     def __init__(self,name,classes,Roll):
#         self.name=name,
#         self.classes=classes   # when we run the program run then automatic this constructor part runs
#         self.Roll=Roll

#     def detail(self):
#         print("my name is ",self.name)
#         print("i read in ",self.classes)
#         print("my roll number is ",self.Roll)

# r=Rajan("rajan",14,14)
# r.detail()


## another method


# class Item:
#     def calculate_total_price(self):
#         print("this is my mobile ", self.name)
#         print("this is my mobile'price ", self.price)
#         print("this is my mobile data ", self.data)

# item1=Item()
# item1.name="iphone"
# item1.data=25
# item1.price=50
# item1.calculate_total_price()


## another method 

# class Item:
#     def __init__(self , name ):

#         print(f"this is an {name}") # f refers to from where { element } came from
#         #print("this is an ",name)

#     def calculate_total_price(self ,x ,y):
#         return x * y
#   ## here we have to define each time all the attributes so for that we can define all the function inside init
# item1=Item("Iphone")
# item1.price =100
# item1.quantity = 5
# x=item1.calculate_total_price(item1.price , item1.quantity)

# item2=Item("laptop")
# item2.price =10
# item2.quantity = 46
# y=item2.calculate_total_price(item2.price , item2.quantity)
# print(x)
# print(y)


# # removing defining the attributes each time we define attributes so to remove that we can define in insidet the class


# class Item:
#     def __init__ (self,name,price=0 ): # if price is not given then it will print 0
#         self.name=name
#         self.price = price

# item1 = Item("Iphone", 100)
# print(item1.name,item1.price)


# class Item: 
#     def __init__(self , name:str , price:int, qunt=0): # here we are defining the data must be of certain type and in qunt we dont need to define because =0 means it is integer and automatic define
#         self.name= name
#         self.price = price
#         self.qunt = qunt

# #       assert condtion , message
#         assert price>=0 , "amount cannot be -ve."  # just to remove bugs
        
#     def calculate_total_price(self): # here we dont need to define parameters
#         return self.qunt * self.price
    
# item1=Item("iphone", -100,10)
# x=item1.calculate_total_price()
# print(x)

## we can also creat class attribute that is valid inside the whole class


# class Item:
#     pay_rate = 0.8 # pay rate after 20% discount
#     def __init__(self , name , price , quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
        
#     def calculation_after(self):
#         print("the name is ",self.name)
#         print("the price is ",self.price)
#         print("the amount is ",self.quantity)
#         return self.price * self.quantity 
    
#     def discount(self):
#         self.price = self.price * item1.pay_rate
#         print(self.price)
        
        
# item1= Item("iphone", 100 ,  45)
# print(item1.pay_rate)       # if there is class attribute(class variable ) then it can also used by attributes of an class
# print(item1.calculation_after())
# item1.discount()
        
        
        
##creat a program for mobile and phone where give discount of 20% for other product and give 30% discount to laptop.
# #  and  also show the list of data  and print the name of the list


# class Item:
#     discount_d = 0.8
#     all = []
#     def __init__(self , name, quantity, price):
#         # Assign to self object
#         self.name =name
#         self.quantity= quantity
#         self.price = price
        
#         # running wether input is correct or not
        
#         assert price>=0 , "invalid data"    # if given price and quantity is less than 0 then print this message
#         assert quantity >=0 , "invalid data"
        
#         #to show the list of all items input to make simple the price and product of the list
        
#         Item.all.append(self) # here all the data are append inside the Item.all
        
        
#     def component(self):
#         print("the name of product is ", self.name)
#         print("the price of the quantity is ", self.quantity)
#         print("the price of the quantity is ", self.price) 
        
#     def discount_amount(self):    # what if we use Item here it means that discount_d is taken for class variable we cannot use another but if we ise self then we can use from personal applicable
#         return self.quantity * self.price * self.discount_d  

#      # this make show all the data inside the list
#     def __repr__(self): 
#         return f"Item({self.name }, {self.quantity }, {self.price})"   

# print("hellow dear")

# item1= Item("iphone" , 50  ,5000)
# item1.component()
# print("the discount amount is " , item1.discount_amount())


# item2=Item("laptop" , 20 ,8000)
# item2.discount_d = 0.7
# item2.component()
# print("the discount amount is " , item2.discount_amount())



# item3 = Item ("mazic", 5 , 25)
# item3.component()
# print("the discount amount is " , item3.discount_amount())


# print(Item.all)
# # from this data present inside Item.all only name is shown
# for instance in Item.all:  
#     print(instance.name)



#  # take the data from the user and give 30% discount if the product cost is more than 10000 with the list of product



# class lib:
#     def __int__(self, name  ,amount , quantity):
#         self.name = name
#         self.amount = amount
#         self.quantity = quantity
#         print("your calculation ")
    
#     def total_amt(self):
#         total = self.y * self.z
#         return total
#     def confirm(self,s):
#         if self.s>=10000:
#             return
            
            

# product_name=input("what is the product you take :-")
# product_amount=input("the amount of product :- ")
# product_quantity=input("the amount of price :- ") 


# item1 = lib(product_name,product_amount,product_quantity)
# a=item1.total_amt()
# print(a)


# class lib:
#     def __init__(self , booktype ,bookname , bookarthur , bookedition):
#         self.book = bookname
#         self.type = booktype
#         self.aurthur = bookarthur
#         self.edition = bookedition
        
#     def show_book(self):
#         print(f"book name {self.book} {self.type}  {self.aurthur}  {self.edition} ")
        

# book = input("aksjfd")
# booktype = input("afsdd")
# arthur = input(" sf sfs")
# edition = input("sfsa")

# item1=lib(booktype , book , arthur , edition)
# item1.show_book()



# #comparing two different persons age
# class sam:
#     def __init__(self,age):
#         self.age =age
        
#     def compare(self,other):
#         if self.age>other.age:
#             print("greater age")
            
#         else:
#             print("smaller age")       
    
# c1 = sam(20)
# c2 = sam(30)

# c1.compare(c2)
# print(type(c1))


# # ---------------------------------------------------------types of method in oops---------------------------------------
# # there  are 2 different types of variable they are 
# the value that are changed if the object change those are called instance variable

# item2=Item("laptop")
# item2.price =10           this value change according to objects
# item2.quantity = 46
# the value that are not change if the object are changed then those variable are called statice variable 

# class Item:
#     discount_d = 0.8   this value doesnot change until we change it manually



# # there  are 3 different types of method they are 
# instance method:-
#           if we are using instance variable then we called them as instance method .. mostly we create and use instance method 
# 
# class car:
#     def __init__(self, color , name):
#         self.color = color
#         self.name = name
        
    
#     def prop(self):
#         print("the color of car is ", self.color)
#         print("the name of car is ",self.name)
        

# car1 = car("black" , "bmw")
# car2 = car("white" , "bugatti")
# car1.prop()
# car2.prop()


# class method :- if we are working with class variabel then we called them as class method for example
# class car:
#     whell = 4
#     def __init__(self, color , name):
#         self.color = color
#         self.name = name
        
    
#     def prop(self):                #----------------------
#         print("the color of car is ", self.color)        #|  instance method
#         print("the name of car is ",self.name) #----------
        
#     @classmethod    # we have to call method before working with class method  
#     def number(cls):   # if we have to work with class then we have to use cls as argument
#         return cls.whell

# car1 = car("black" , "bmw")
# car2 = car("white" , "bugatti")
# car1.prop()
# print(car1.number())
# car2.prop()
# print(car2.number())


# static method :- if we have nothing to do with class and inherit variable then this method is called static method 
# @staticmethod       #  other example factorial , integer or not
# class printing:   
#     def define(self):
#         print("this is my name ")
# c=printing()
# c.define()
## when we use this method is we have to do somethings with the class and we take data from outside the class



# # ---------------------------------------------------------------------inheritance------------------------------------------------------------



# # if class b can inherit the property of class A then this types of property is called inheritance

# class sending:
#     def __init__(self, device , money  , weight):
#         self.device = device
#         self.money = money
#         self.weight1 = weight
        
#     def get_info(self):
#         print(f"product name is {self.device}")
#         print(f"product price is {self.money}")
#         print(f"product weight is {self.weight1}")
        
        
# class defect(sending):
#     def __init__(self , product , price , weight ,device , money , weight1): # if we want to take the init function of parent class then we have to define that with assigning parameter 
#         # we have to pass the parmeter the of both class not only here also in the object part . if we  dont have to take the value then we dont have to define this
        
#         self.product = product
#         self.price= price
#         self.weight = weight
        
#         super().__init__(device , money  , weight1)
        
        
#     def take (self):
#         print(f"product defect is {self.product}")
#         print(f"price to repair is {self.price}")
#         print(f"days to repair {self.weight}")
         
        
        
        
# item = sending("phone", 200 , 50)
# item.get_info()
# print("---------------------")
# waste = defect("microchip" , 5000 , 50 , "phone", 200 , 50)
# waste.take()
# waste.get_info()



# # ---------------------------------------------------------------------polymorphism------------------------------------------------------------

#  #if method or function have same name but different characterstics then this properties are called polymorphism there are 3 different  type of polymorphism 
#duck typing :- if any animals walk and talk like a duck then it is a duck
# class Duck:
#     def walk(self):
#         print("run duck run")
        
# class Horse:
#     def walk(self):
#         print("run horse run")
        
# def my_function(obj):  # remember we donot use self in external program    .. here it's manin concer is that is data passed form the function contain that
#     # function inside class or not.
#     obj.walk()
    
# d=Duck()
# my_function(d)

# h=Horse()
# my_function(h)



# # ---------------------------------------------------------------------Encapsulation ------------------------------------------------------------
## by default all the method are pulic inside the class and there for there may be confusion between created variable. so to protect form that we use public and protected 
# # private:- we can make any method privete usoing (__) before any method then those method are privete..

# class army:
#     def __init__(self , name , batch):
#         self.name = name
#         self.batch = batch

#     def __batch(self): # this method is private method
#         print(f"the name is {self.name} and batch is {self.batch}")
        
# class police:
#     def __init__(self , name , batch):
#         self.name = name
#         self.batch = batch
        
#     def batch(self):
#         print(f"the name is {self.name} and batch is {self.batch}")
# a1 = army("nabin " , 2012)
# a1._batch()
# p1 = police("ram ", 2018)
# a1.batch()

## protected:- in private we cannot take data outside the class but in protected we can access the data outside the  class if the data is inherited form parent class... it 
## if data is protected in parent then that data can be taken by only child class.

















# -------------------------------------------------------------operator overloading-----------------------------------------
# a+b , where a and b are operand and  + - * are operator


# a=4
# b=5
# print(a+b)
# when we are using + between two integer  a and b then in background  int.__add(self, other) is running wher self takes value of a and other takes the value of b same thing happen with mul, sub/////

# integer, string  knows what is + because they are define in class but .. when we define class and they dont know what is student so we use operator overloading

# # adding s1 and s2 x number
# class student:
#     def __init__(self ,m1,m2):
#         self.m1=m1
#         self.m2 =m2
        
#     def __add__(self,other):
#         return self.m1 + self.m2 , other.m1 + other.m2
          
# s1 =student(58 , 69)
# s2 =student(60 , 65)

# s3 = s1+s2    # => student().__add__(s1,s2)
# print(s3)



## adding s1's x and s1'y numbers



# class point:
#     def __init__(self , x , y):
#         self.x = x
#         self.y= y
        
#     def __add__(self ,other):
#         return self.x + self.y , other.x + other.y
    
    
# c1= point(10,20)
# c2 = point(30,40)
# c= c1 + c2
# print(c)

# if c[0]>c[1]:
#     print("wins")
# else:
#     print("loose")

# -------------------------------------------------------------method  overloading and method overridding-----------------------------------------




















# --------------------------------------------------------error handling-----------------------------------------
# # there are 3 different type of error runtime error , logical error , compile time error

# a=5
# b=3
# print(a/b)
# # what if we divide by 0 then it shows error so we use try and catch where try run first until it found error it run if found error then from that run to catch block
 
# a=5
# b=0
# try:
#     print(a/b)
# except:
#     print("error found invalid data")
    
# finally:  # whatever happen this block run
#     print("bye")


# #we can show the exception error also which is given by the complier
 
# class divisible():
#     def __init__(self,x ,y):
#         self.x =x 
#         self.y = y
        
#     def result (self):
#         try:
#             print(self.x/self.y)
#         # except Exception as e:     # if want to show same error for all then use this 
#     #     print(e)
    
#         except ZeroDivisionError as e:  # if want to show individual error then use by giving error type
#             print(e)
    
#         except ValueError as e:
#             print(e)
    
#         finally:  # whatever happen this block run
#             print("bye")


# bad = divisible(5,1)
# bad.result()


# # --------------------------------------------------------importing-----------------------------------------
# # exporting this data in testing.py 
# def importing():
#     print("this we are sending in testing.py folder")
    

# class adding:
#     def __init__(self, x, y):
#         self.x =x 
#         self.y =y
        
#     def sum(self):
#         print(f"the sum of {self.x} and {self.y} is ",self.x + self.y)
        
        
# a=adding(20,30)
# a.sum()


# # ------------------------------------------------------thread and multithreading----------------------------------------
# # there are multiple thread in our device those program are run by main thread automatically...for example if there is an program 
# # and it is run by 3 user if we donot use multithread concept then we have to stop for execution of 1 program and other will 
## be waiting to get the data for that we need to use multithreading

# from time import sleep
# from threading import *
# class hello(Thread):  # from this we creat two thread for hello and hi to run that we need to type statrt insted of run 
#     def run(self):
#         for i in range(500): # can be seen only large number
#             print("hello")
#             sleep(1)  # time interval for each result
            
# class hi(Thread):
#     def run(self): # we have to use run as method if we use another it wont run
#         for i in range(500):
#             print("hi")
#             sleep(1)
            
# # # with simple for and loop inside class they are running inside inside single thread 
# t1 = hello()
# t1.start() # should use start not run function
# sleep(0.3) # this start is given in the begining time of the program if choose 1 get error because there is not differecne
# # when t1 start then sleep for 0.3 sec and then only start t2 .. there are  2 thread so t1 is runung in another  and t2 on another

# t2 = hi()
# t2.start()

# t1.join()  #first join t1 and then join t2 simultaneously
# t2.join()

# print("bye")
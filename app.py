# Returns list of reserved words
import keyword
print(keyword.kwlist)

print('\n')
# Binary number  --> Allowed values are 0,1
print(0b0111)
# Octal number   --> Allowed values are 0 to 7 (8 --> octal)
print(0o0111)
# Hex Decimal number  -->  Allowed values are 0 to 9, 10 - A, 11 - B, 12 - C, 13 - D, 14 - E, 15 - F (16 --> hex)
print(0b0111)
print('\n')
# Convertion
print(bin(15))
print(bin(0o123))
print('\n')
print(oct(100))
print(oct(0b1111))
print(oct(0xFace))
print('\n')
print(hex(100))
print(hex(0b111))
print(hex(0o777))



# Data Types
# int, float, complex, str, bool


# int
a =100
print(type(a))

# float
b =100.1
print(type(b))
print(1.2e3)

# complex --> binary, octal, hex decimal allowed in real part (10 is real part and 20j is imaginary part)
c= 10 + 20j
print(c)
print(type(c))

# str
print('vamsi krishna')
print('\n')
print("vamsi krishna")
print(""" My name is 'vamsi krishna' and from "tanuku" """)


# bool
v = True
print(v)
print(type(v))


# Index --> index starts from 0 and -1 values return reverse order of string
#Index error while print outside the index ex: s[100]

s = 'vamsi krishna'
print(s[0])
print(s[len(s)-1])
print(s[-1])


# Slice operator s[starting: ending-1]
print(s[0:5]) # returns vamsi
print(s[:4]) #start from 0 at position.
print(s[1:]) # start from position 1 'a' and till end
print(s[:]) # returns empty string


#Programs :
q = 'vamsi' # start v to upper case
print(q[0].upper()+q[1:])

w = 'vamsi' # last i to upper case
print(w[:len(w)-1]+w[-1].upper())

##########################################################################
''' '+' Operator '''
# + operator applicable to two strings but not with string and integer

w = 'durga' + 'soft'
print(w)


# to overcome this problem
h = 'vamsi\n' +str('10')
print(h)

#g = 'durga' + 10
#print(g)  # --> returns type error


##########################################################################
''' '*' Operator '''
# * operator not applicable b/w string but applicable b/w integer and string

r = 'vamsi' * 2
print(r)

#t = 'vamsi' * 'vamsi'
# print(t) --> returns error

##########################################################
#TypeConvertion

# int     -> complex not applicable
print(int(101.5))
print(int(True))
print(int("200"))

#float    -> complex not applicable
print(float(10))
print(float(True))
print(float("100"))
print(float("1055.6"))

#complex
###Form : 1
print(complex(10))
print(complex(10.56))
print(complex(True))
print(complex("103.66"))
print(complex("200"))

###Form : 2
print(complex(10,20))
print(complex(10.56,100.2))
print(complex(True,True))
# print(complex("103",10)) // type error
# print(complex("200",190)) //type error

# bool convertion --> value is 0 and ''(emplty string) means false
print(bool(1))
print(bool(0)) # false
print(bool(18.5))
print(bool(0.0)) # false
print(bool(1+0j))
print(bool(0+0j)) #false
print((bool("vamsi")))
print((bool("True")))
print((bool("False")))
print(bool(' '))  # false only single couts
print(bool(" ")) # True

# str convertion

print(str(10))
print(str(0b1111)) #binary
print(str(10.3))
print(str(True))

##############################################################################################
#Fundamental Data types
''' fundamental data types are in Immutable in nature
    @ Once we creates an object, we cannot change in that object. 
    If we are trying to performaning any change, with those changes, a new object will be created. '''

ex = 10
print(id(ex))
ex = ex+1
print(id(ex)) # new object will created with those changes.

##Why Immutable ?
''' Main Advantage is 1. Memory Utilization
                      2. Performance wise increase '''
a1 = 10
b1 = 10
c1 = 10

print(id(a1)) # all three variable are directing to single object. So, sigle memory useage and performance wise increase.
print(id(b1))
print(id(c1))

#to check it
print(a1 is b1 )  # retruns true refernce to same object
print( a1 == b1)  #content is also same.

##-------------------------------------------------------
#Object Reusability Concept Available
# int, float, bool, str are available but complex can't used as object reusability

#Advan : 1. memory utilization 2. performance improved.

a1 = 10
b1 = 10
print(a1 is b1 )  # retruns true refernce to same object
print( a1 == b1)  #content is also same.

#--------------------------------------------------------------
''' Collection : is a group of values in single entity and all fundamental data type can holds only single variable. '''
# types : list, tuple, set, frozenSet, dict, byteArray, bytes, range, none

#List
''' 1. ordered important 
    2. duplicates are allowed 
    3. index and slice are  allowed
    4. heterogeneous 
    5. growable  
    6. mutable in nature (overides the existing object)
    7. Represent with []
    8. append() and remove()
'''
l =[2,"vamsi",2,39.4,28]
print(l[0])
print(l[-1])
l[0] = "y"
print(l)
l.append(90)
print(l)

#Tuple : similar to list but readable only can't write
''' 1. ordered important 
    2. duplicates are allowed 
    3. index and slice are  not allowed
    4. heterogeneous 
    5. immutable in nature (overides the existing object)
    6. Represent with ()
'''
t =(290,"vamsi krishna y ",2.99,39.4,28)
print(t[0])
print(t[-1])
print(t)

#Note : if t = (10) it tried as int but not as tuple comma is compulsory for single values
t1 = (190,)

#-----------------------------------------------------------------------------------
#Differences b/w  list and tuple
'''
List:
    1. mutable in nature
    2. [] respresented
    3. growable in nature
    4. content can be change
    5 .preformance wise less
    6. append() and remove()
Tuple:
    1. immutable in nature
    2. () respresented
    3. content can't be change
    4 .preformance wise Faster
'''
#--------------------------------------------------
#Set :
''' 1. ordered not important 
    2. duplicates are not allowed 
    3. index and slice are not allowed
    4. heterogeneous 
    5. growable  
    6. mutable in nature (overides the existing object)
    7. Represent with { }
    8. add() and remove()

Can be  build in two ways
    1. set()
    2. set(<iter>)
'''

s = {111,2, 90, "m", 12.5,"o"}
s.add(True)
s.remove(111)
print(s)

s1 = set(("A1", "A2", "A3", "A4", "A5"))
print(s1)
#Or

s1 = set(["A1", "A2", "A3", "A4", "A5"])
print("Square braket : ", s1)

#note : Empty set represent as s = Set{} if we declare as s = {} it tired as dict
s1 = set()
print(type(s1))


#example
w2 = "vamsi"
print(list(w2))
print(set(w2))

#-----------------------------------------------
#dist -> key : value pair like map in java
'''
1. Ordered not important
2. key can"t not be duplicate but value can be duplicate. 
3. Heterogenous 
4. mutable in nature 
5. Index and slice not allowed
6. {} represent
7. Empty dict ->  d ={} '''

d = {1: "v",2: "a", 3: "m", 4: "s", 5: "i"}
print(d[5])
d[6] = " y" # adding
print(d)

#-------------------------------------------------------------------------------
#Range :

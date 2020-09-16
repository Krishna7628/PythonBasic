'''
Array : is a collection of similar type of elements which has contigous memory location

- array are mutable. can be  changed

Creation of array  :
1 import array - without alias
2 import array as arr - using alias
3 from array import * - using *

ex  : array('data type',. [values])
'''

import array

a = array.array('i', [2, 1, 3, 45, 53, 5])
print(a)

import array as arr

b = arr.array('i', [2, 1, 3, 45, 53, 5])
print(b)

from array import *

c = array('i', [21, 12, 32, 45, 53, 56])
print(c)

# Accessing array element : start from 0

print(a[3])

# find length of an array
print(len(a))  # length - 6

'''Adding element to array
#using 
    append() - added att last
    extend() - add more than one element at end 
    insert() - add element at specific position
'''

a.append(9)
print(a)  # array('i', [2, 1, 3, 45, 53, 5, 9])

a.extend([2, 3, 4, 5, 67, 7])
print(a)  # array('i', [2, 1, 3, 45, 53, 5, 9, 2, 3, 4, 5, 67, 7])

a.insert(0, -12)
print(a)  # array('i', [-12, 2, 1, 3, 45, 53, 5, 9, 2, 3, 4, 5, 67, 7])

'''Removing element to array
#using 
    pop() - removes element and return it
    remove() - remove an element with a specific value without returning it 
'''
print(a.pop())  # removes last element
print(a)
print(a.pop(-1))
print(a)
print(a.remove(5))  # if two elements of 5 then it removes first element
print(a)

# ----------------------------------------------------------------------
# Array Concatentaion
a1 = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
a2 = array('i', [3, 4, 5, 67, 8, 9, 10])
a3 = array('i')  # array('i', [1, 2, 3, 4, 5, 6, 7, 8, 3, 4, 5, 67, 8, 9, 10])
a3 = a1 + a2
print(a3)
# ---------------------------------------------------------------------------
# Slice an array
print(a3[::-1])
print(a3[1::])

# -------------------------------------------------------------------------
# looping through an array--
# for and while

for i in a3:
    print(i)

for i in a3[0:3]:
    print('\n', i)

temp = 0
while temp < a3[4]:
    print(a3[temp])
    temp = temp + 1


#-----------------------------------------------------------------------------------------------


#Hashable or #HashMap : is a type of data structure that maps keys to its value pairs
#How to create dictionary ?> 1 declare curly braces 2 dict() function

#Ex :1 using  curly braces
b = {'01': 'vamsi', '02': 'krishna'}
print(b)
print(type(b))
#Ex :2 using dict()


#----------------------------Nested Dictionary: contant dictionary inside a dictonary
c = {"Employee": {"vamsi": {"ID": "01", "Salary": "2000", "Designation": "Manager"},
                  "krishna": {"ID": "03", "Salary": "6000", "Designation": " team Manager"}}}
print(c)

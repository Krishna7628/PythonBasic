"""
1.Python Basics
2 Variable, Data types, Operators
3 arrays
4 flow controls
5 methods
6 file handling
7 oops
8 practice programming
"""

import keyword

print(keyword.kwlist)
# -----------------------------------------------------------------------------
# Comments
# Single comment - # start
# Multiple line - #
# DocString - """ Documentation representation"""
# -----------------------------------------------------------------------------
# Variable : is memory location were we stored

a = 100
b = 'vamsi'

# -----------------------------------------------------------
# Data Type converstion
# int(), float(), tuple(), list(), set(), dict()
print(str("10") + "vamsi")
# ------------------------------------------------------------------------
'''
Collection list, tuple, set, frozenSet, dict, range, bytes, byteArray

Special Collections Data type : is specialized collection data structures (Collection module)
        namedtuple() - returns a tuple with a named value for each element in tuple
        chainmap, 
'''

from collections import namedtuple
a = namedtuple('course', 'name, technology')
s = a('data science', 'python')
print(s)
#or
b = namedtuple('CustomerName', 'FirstName, SecondName, LastName')
d = b('vamsi', 'krishna', 'yandrapragada')
#or using list
#f = b dot _make(['c', 'python'])

'''
deque : pronounced as 'deck' is an optimised list to perform insertion and deletion easily
'''
from collections import deque
a = ['e', 'c', 'y', 'r', 't', 'w', 'q']
d = deque(a)
d.append('python') # appends at ent
d.appendleft('c++') # appends at sarting
print(d)
d.pop() # remove last element
print(d)
d.popleft()
print(d)

'''
Chainmap : is a dictionary l.ike class for creating a single view of multiple mappings(simple combine two dictionary)
'''
from collections import ChainMap

a = {1: "vamsi", 2: "krishna"}
b = {3: "DL", 4: "AL"}
c = ChainMap(a,b)
print(c)

'''
Counter : is a dictionary subclass class for counting hashable objects
'''
from collections import Counter

a= [1, 2, 3, 4, 1, 4, 4, 5, 6, 7, 6, 5, 4, 3, 2, 4]
c = Counter(a)
print(c) # Counter({4: 5, 1: 2, 2: 2, 3: 2, 5: 2, 6: 2, 7: 1}) return count of each element

#element function
print(list(c.elements())) #[1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 6, 7]
#Most common function
print(c.most_common())# sorting [(4, 5), (1, 2), (2, 2), (3, 2), (5, 2), (6, 2), (7, 1)]
#subtract
sub ={2: 2, 6: 1} # removing 2,6 were remove 2 two time and 6 one time
print(c.subtract(sub))#[(4, 5), (1, 2), (2, 2), (3, 2), (5, 2), (6, 2), (7, 1)]
print(c.most_common())# after subtracting [(4, 5), (1, 2), (3, 2), (5, 2), (6, 1), (7, 1), (2, 0)]

'''
orderedDict : is a dictionary subclass which remembers the order in which the entries were done
'''
from collections import OrderedDict

d = OrderedDict()
d[1] = 'a'
d[2] = 'b'
d[3] = 'c'
d[4] = 'd'
d[5] = 'e'
d[6] = 'f'
print(d)#OrderedDict([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f')])
print(d.keys())#odict_keys([1, 2, 3, 4, 5, 6])
print(d.items())
d[1] = 'h'
print(d)#OrderedDict([(1, 'h'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f')])

'''
defaultDict : is a dictionary subclass which calls factory function to supply missing value 
'''
from collections import defaultdict

d = defaultdict(int)
d[1] = 'python'
d[2] = 'C'
print(d[3]) # if value not available returns 0 but dict throws error


'''
UserDict : is a wrapper around dictionary objects for easier dictionary sub classing
UserList : is a wrapper around list objects for easier list sub classing
UserString :  is a wrapper around string objects for easier string sub classing
'''
from collections import OrderedDict



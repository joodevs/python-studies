# LIST BASICS

# We initiate a list by containing elements within '[]' and distinguish elements with ','.
# When accessing an element, we put the index value within the bracket.
# Index starts at 0.
# When declaring an empty list, we input 'list()' or, simply, '[]'

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# Access the fifth element
print(a[4])

# Declare an empty list
a = list()
print(a)

a = []
print(a)

# Reset a one-dimensional list of size N and containing 0
n = 10
a = [0] * n
print(a)

# LIST INDEXING

# We can use both positive and negative numbers to index elements.
# With negative index numbers, we reverse the order of search.
# For instance, inputting '-1' yields the last element in the list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print the last element
print(a[-1])

# Print the third last element
print(a[-3])

# Change the value of the fourth element
a[3] = 7
print(a)

# LIST SLICING
# We can use list slicing to print a certain range of elements within the list
# The first index is the literal index (e.g. 0 for the 1st element)
# The second index is (literal index + 1)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print the second, third, and fourth elements
print(a[1 : 4])

# LIST COMPREHENSION

# A list containing odd numbers within the range 0-19
array = [i for i in range(20) if i % 2 == 1]

print(array)

# This is equivalent to:
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)

# A list containing 1-9 squared
array = [i**2 for i in range(1,10)]

print(array)

# Reset a 2-dimensional list of N x M
n = 3
m = 4
array = [[0] * m for _ in range(n)]

# The role of "_" in list comprehension:
# In python data structure and algorithms, we often use the underscore to
# perform a repeated action without recognizing the value of the variable needed for repetition

# For instance, we write as below to add up integers from 1 to 9:
sum = 0
for i in range(1, 10):
    sum += i
print(sum)

# However, to perform a repeated 'action' not affected by variable value, we do the following:
for _ in range(5):
    print("Hello World")

# LISTS OF STRINGS IN PYTHON

# When initiating a LoS, we use ' or "
# We can contain ' in " or " in '
# We can also attach \ in front of ' or ", we can use them freely

data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# COMPUTING LoS

# LoS computation can be convenient when processing LoS

a = 'Hello'
b = 'World'

print(a + " " + b)

a = "String"

print(a * 3)

a = 'ABCDEF'

print(a[2 : 4])

# TUPLES

# Tuples in Python are very similar to lists, except that:
# Values within tuples cannot be changed once declared.
# Tuples use '()' while lists use '[]'.

# For instance,

a = (1, 2, 3, 4)
print(a)

# yields (1, 2, 3, 4)

# However, 'a[2] = 7' yields an error.

# As can be seen here, item reassignment using '=' is impossible with tuples

# Then why use tuples?

# We use tuples usually when simulating graph algorithms, where values once inputted
# within queues do not need to be changed. Furthermore, tuples are more efficient in memory
# and usually used when we need to contain different types of values (e.g., cost & node in Dijkstra)

# DICTIONARIES IN PYTHON

# Dictionaries consist of a pair of KEY and VALUE.
# While lists and tuples store values sequentially, dictionaries store values as a pair
# We can store an unmodifiable value like a tuple as the key value

fruits = dict()
fruits['사과'] = 'Apple'
fruits['바나나'] = 'Banana'
fruits['코코넛'] = 'Coconut'

print(fruits)

if '사과' in fruits:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")
else:
    print("'사과'를 키로 가지는 데이터가 존재하지 않습니다.")

# Key data only
key_list = fruits.keys()

# Value data only
value_list = fruits.values()

print(key_list)
print(value_list)

# Print each value corresponding to a key value
for key in key_list:
    print(fruits[key])

# SETS IN PYTHON

# In Python, a set is made of a list or LoS & has the following traits:
# It does not allow for repetition.
# Order is not significant.

# Since order of elements held meaning for lists and tuples, it was possible
# to use iteration to access specific elements.

# Initiate set - Method #1
# set() acts as an operator that turns a list into a set
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# Initiate set - Method #2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# Using a set is especially convenient when checking whether a specific element
# has emerged within a series of elements.

# SET COMPUTATION

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

# SET FUNCTIONS

data = set([1, 2, 3])
print(data)

# Add new element
data.add(4)
print(data)

# Add multiple elements
data.update([5, 6])
print(data)

# Remove element of specific value
data.remove(3)
print(data)

# CONDITIONALS

x = 15

if x >= 10:
    print(x)

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

score = 85

if score >= 70:
    print("Your score is above 70.")
    if score >= 90:
        print("Your score is exceptional.")
else:
    print('Your score is below 70.')
    print('Be better.')

# COMPARISON OPERATORS

# X == Y : True if X and Y are equal
# X != Y : True if X and Y aren't equal
# X > Y  : True if Y is smaller than X
# X < Y  : True if X is smaller than Y
# X >= Y : True if X is greater than or equal to Y
# X <= Y : True if X is smaller than or equal to Y

# LOGICAL OPERATORS

# X and Y : True if both X and Y are True
# X or Y  : True even if only one of X and Y are True
# not X   : True if X is not True

# OTHER OPERATORS

# X in LIST : True if X is in LIST
# X not in LoS : True if X is not in LoS X

# 'pass' can be used to not invoke any action even when True

score = 85

if score >= 80:
    pass # code to be added
else:
    print('Your score is below 80.')

print('Closing the program.')

# Can be simplified

score = 85

if score >= 80: result = "Success"
else: result = "Fail"

# Further simplify

score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

# Removing elements of specific values

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

# This is equivalent to:

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

result = [i for i in a if i not in remove_set]

print(result)
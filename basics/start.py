from functools import total_ordering

print('Hello, World') ## the most famous code line

## Create variable
print("#Create variable")
greeting = "Hello"
happy_thought = "Happy"
x = 10
X = 11
print(greeting + "Mario")
print(happy_thought + "Luigi")
print(x) ## is different from X
print(X)

##Constants
print("#Constants")
PI = 3.1415
API_KEY = "kgibsfdhgvnozsbdgvnzsmdgjven"

##Data Types
print("#Data Types")
text = "text" #string
number = 100  # integer
number_second = -100 #integer too
decimal = 0.5 #flaot
complexe = 8j #complexe number

people = ["Mario","Luigi"] # list , can be change
lotto_numbers = (1,2,3,4,5,6) # tuple , cannot be change
numbers = range(1,1000) # generate number from 1 to 999

users = {'user1':'mario123', 'user2':'luigi2022'} #dictionnary key value

unique_numbers = {1,2,2,3,3,4} # set list , if print we've got only 1,2,3,4 , but doesn't keep the order
unique_number_frozen = frozenset({1,2,2,3,3,4}) # set list cannot change
print(unique_number_frozen)
print(unique_numbers)


is_connected = False #boolean
is_empty = None # no value

### Adding type hints
print("#Adding type hints")
name = 'Mario' # python knows my var is a
name_with_type_adding : str = 'Luigi' # safier and save lots of time

##Type conversion
print("#Type convertion")
name_conv = 'Toto'
number_conv = 10

## print(name+number) --> can't work error : can only concatenate str (not "int")
##solution
print(name_conv+str(number_conv))

#i can print type of var
print(type(name_conv))

#sounds logic but not obvious
number_hundred = '100'
classic_number = 10

result_one = str(number) + number_hundred
result_two = number + int(number_hundred)

#integer
print("#Integer")
a = 1
b = 100
c= 10000000000
d = -100
e = 100_000_000
f = 2

print(a + d)
print(e) # underscore gonna be ignore when printing


# basics operator
print("#basics operators")
print(1+2)
print(1-2)
print(2*2)
print(2/4) # the result is a float
print(10%3) # 3 goes 3 times in 10 and stay 1 ( 3*3 = 9 + 1 = 10) % give us the reminder
print(10**3) # it's 10 power 3
print(10//3) # strict division = 3
print(10/3) #  give us 3.3333333
print(f)
f +=3 # works with all operators
print(f)
f **=4
print(f)

print(10==10) # true
print(10!=10) # false
print(10 < 10) #
print(10 > 10)
print(10 >= 10)


g = 2
h = 5

print(a<b or 4 > 6)
print(not(a<b or 4 > 6)) # opposite of example above


i= 100.0
j= 1.0 * i

print(id(i)) # 4303499440
print(id(j)) # 4303500752
print(i is j) # false cause not the same address in memory ( Cpython ) or id if you are in Pypy
print(i == j) # value is the same but not the adress

numeros = [1,2,3,4,5]

print(1 in numeros) #true
print(10 in numeros) #false
print(10 not in numeros) #true

#Strings
print("#Strings")
# using " is better when you want to use ' inside
print("hello 'Luigi' !")
texte = "text "


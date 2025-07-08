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
texte = 'text "toto" \n hi toto'
textee = "text \"toto\" "
texte_multiligne = """this is a story
the middle
the end"""

print(texte)
print(textee)
print(texte_multiligne)
#F-String
print("F-string")
## put var into a string
var = "Text"
print("1 "+var+" 2")
new_string = f"1 {var} 2 , or {1+4}"
print(new_string)

#Boleans
print("Booleans")
print(False == 0)
print(True == 1)
print(True+True) ## equal 2 ...
print(True+False) ## equal 1
wtf = True + True
print(wtf == True) ## true + false == true but true + true don't ...
## to work with logic use and/ or , cause bool inherite from int

##List
# modifiable = oui / ordre conservé = oui / elements dupliqués = oui / def = liste d'élements
print("List")

peoples: list[str] = ['Mario','Luigi','Peach','Peach','Toad']
print(peoples) # print ==> ['Mario', 'Luigi', 'Peach', 'Peach', 'Toad']
print(len(peoples)) # print 5
print(peoples[3]) # Peach
print(peoples[-1]) #Toad
print(peoples[0:2])# ['Mario', 'Luigi']
print('Luigi' in peoples) #True
print('luigi' in peoples) #false !! case sensitive
peoples[0] = 'Bowser'
print(peoples) #['Bowser', 'Luigi', 'Peach', 'Peach', 'Toad']
peoples[2:4] = ['Sonic',"Knuckles"]
print(peoples) #['Bowser', 'Luigi', 'Sonic', 'Knuckles', 'Toad']
peoples.insert(2,"index2")
print(peoples) #['Bowser', 'Luigi', 'index2', 'Sonic', 'Knuckles', 'Toad']
peoples.append('Shadow')
print(peoples)#['Bowser', 'Luigi', 'index2', 'Sonic', 'Knuckles', 'Toad', 'Shadow']
## insert add in a specific position
## append insert at the end of the list
peoples2: list[str]= ['Fox','Frog']
peoples.extend(peoples2)
print(peoples) # ['Bowser', 'Luigi', 'index2', 'Sonic', 'Knuckles', 'Toad', 'Shadow', 'Fox', 'Frog']
new_lists = peoples + peoples2
print(new_lists)
peoples+=peoples2
print(peoples)## ['Bowser', 'Luigi', 'index2', 'Sonic', 'Knuckles', 'Toad', 'Shadow', 'Fox', 'Frog', 'Fox', 'Frog']
peoples.remove('index2')
print(peoples) # ['Bowser', 'Luigi', 'Sonic', 'Knuckles', 'Toad', 'Shadow', 'Fox', 'Frog', 'Fox', 'Frog']
peoples.reverse()
print(peoples) #['Frog', 'Fox', 'Frog', 'Fox', 'Shadow', 'Toad', 'Knuckles', 'Sonic', 'Luigi', 'Bowser']
peoples.sort()
print(peoples)#['Bowser', 'Fox', 'Fox', 'Frog', 'Frog', 'Knuckles', 'Luigi', 'Shadow', 'Sonic', 'Toad']
peoples.clear()
print(peoples)#[]

#Tuples
# modifiable = non / ordre conservé = oui / elements dupliqués = oui / def = liste immuable
print('Tuples')
people_tuples : tuple = ('Mario','Luigi','Toad','Bowser','Toad')# () is not mandatory , tuple is made by ,
print(type(people_tuples))
print(len(people_tuples))

people_list : list[str] = list(people_tuples)
print(people_list)
people_list.append('TOTO')
print(people_list)
people_l_to_tuple: tuple = tuple(people_list)
print(people_l_to_tuple)
print(people_tuples[0]) #Mario
print(people_tuples[:2]) #print from begining tuple to index 2
print(people_tuples[2:]) #print from index 2  to end of tuple
print('Mario' in people_tuples) # true cause Mario is in tuple
print(people_tuples.count('Mario'))#1
print(people_tuples.index('Toad'))#2 but if we lokk a the tuple , we've got 2 Toad index 2 and index 4 , method index only return the first they found
people_tuple_example: tuple = ('Mario','Peach','Toto','Bob')
k,l,*m = people_tuple_example
print(k)#Mario
print(l)#Peach
print(m)#['Toto', 'Bob'] , if we forgot the * , we've got an error


#Set
# modifiable = oui / ordre conservé = Non / elements dupliqués = Non / def = ensemble sans doublons


#Dict
# modifiable = oui / ordre conservé = oui / elements dupliqués = clé unique / def = Paire: Clé /valeur


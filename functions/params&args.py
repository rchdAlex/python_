def greet(name: str, greeting: str = 'Hello'):
    print(f'{greeting}, {name}')


greet('Legolas')  # use default params
greet('Thorn', 'Ciao')

#careful use the default params at the end however the next params should be default too
def greet_two(name:str,greeting:str = 'Hello', age:int = 0):
    print(f'{greeting}, {name} ! you have {age} years old')

greet_two('Maximus')
greet_two('Marc',age=4)
greet_two('Paul',age=4,greeting='Hi')

#usse correct wording , name is a parameters of function greet and 'Maximus' is an argument of the function

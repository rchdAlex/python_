def great_people(*people: str,age:int):
    print(people)
    print(type(people))
    for name in people:
        print(f'Hello {name}')


great_people('Pierre', 'Paul', 'toto',age=3)

def do_something(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs['name'])

do_something(name='Amario' , age = 4)

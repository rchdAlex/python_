people = ['Mario', 'Luigi', 'Peach', 'Toad']
print(type(people))  # list

for person in people:
    print(f'Hello, {person}')

numbers = range(0, 10)

for number in numbers:
    print(number)

# same result if i do

for numero in range(10):
    print(numero)

for char in "marko":
    print(char)

for char in "marko":
    print(char)
    for x in range(1):
        print('-')

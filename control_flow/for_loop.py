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


### add break and continue

for i in range(10):
    print(i)
    if i==5:
        break

print('Done! break')


for j in range(5):
    if j == 3:
        continue
    print(f'value of j after conitnue is {j}')
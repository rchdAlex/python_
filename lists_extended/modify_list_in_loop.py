people: list[str] = ['Mario','Luigi','Peach','Toad']

for person in people:
    if person == 'Luigi':
        people.remove('Luigi')

    if person == 'Peach':
        print('Hi from Peach')

    print(f'{person} --> {people}')

"""
Mario --> ['Mario', 'Luigi', 'Peach', 'Toad']
Luigi --> ['Mario', 'Peach', 'Toad']
Toad --> ['Mario', 'Peach', 'Toad']
!!! why peach is not here ? cause index change during loop
"""
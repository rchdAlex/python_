sample_list = []

for i in range(10):
    sample_list.append(i)

print(sample_list)

# [result for element in list]
sample_list2 = [i for i in range(10)]  # comprehension list
sample_list3 = [i for i in range(10) if i % 2 == 0]

print(sample_list2)
print(sample_list3)

people: list[str] = ['Mario','Luigi','Peach']

cap_people = [person.upper() for person in people]

print(people)
print(cap_people)
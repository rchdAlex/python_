a = 0

while a < 5:
    print(a)
    a += 1

print('Done! classic')

## adding break and continue
i = 0

while i < 3:
    print(i)
    if i == 1:
        break
    i += 1

print('Done! break')

j = 10

while j > 5:
    print(j)

    if j == 3:
        continue
    print(f'value of j after continue {j}')
    j -= 1

print('Done! continue')

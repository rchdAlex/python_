a = 10

if a > 5:
    print('yes a is more than 5')
    print('on the same bloc cause works with indentation')
else:
    print('Failed!')
print('Done')

text = 'Hello'

if text == 'Hello':
    print('Bot: Hello')
elif text == "bye":
    print('Bot:Goodbye')
else:
    print('i did not understand')

### shorter way to do if else

print('Succes') if 1 > 2 else print('Failed')
print('Succes') if 10 > 2 else print('Failed')
# do this if TRUE else do this

a, b = 10, 20
print('a is greater') if a > b else print('b is greater')  # b is greater

x, y = 34, 53
result = x if x > y else y
print(result)  # 53

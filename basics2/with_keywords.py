"""file = open('avocado.text')
text = file.read()
file.close()
print(text)"""

## with automatically open and close the stream

with open('avocado.text') as file :
    text = file.read()
    print(text)
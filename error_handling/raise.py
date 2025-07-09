user_input: str = input('You: ')

if user_input == '0':
    raise Exception('Please never use 0')

is_connected: bool = False

def connect_to_internet():
    if not is_connected:
        raise Exception('No internet')
    else:
        print('Connected to the internet')
## careful beacuse raise , raise a classic exception
try:
    connect_to_internet()
except Exception as e :
    print(e)
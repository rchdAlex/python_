from enum import Enum


class State(Enum):
    OFF = 0
    ON = 1


state = State.ON

if state == State.ON:
    print('The lamp is turn on !')
    print(State.ON.value)
elif state == State.OFF :
    print('The lamp is turn off')

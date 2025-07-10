x = 10

def func():
    x=20
    print('Inner func =',x)

func()
print('Outter func =',x)
"""
Inner func = 20
Outter func = 10
"""

def func_with_global():
    global x
    x=25
    print('Inner func with global=',x)

func_with_global()
print('Outter func after global =',x)

def func_inner_local():
    x=32

    def inner_func_with_nonlocal():
        nonlocal x # not la global , global is for everyone , non local is just for the scope of the function
        x = 10
        print('Inner x=',x)

    inner_func_with_nonlocal()
    print('Outer x',x)

func_inner_local()
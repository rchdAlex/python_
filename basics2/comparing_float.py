a = 0.3
b = 0.1 + 0.2

print(a)
print(b)
print(a == b)


def compare_float(x: float, y: float, tol: float) -> bool:
    absolute = abs(x - y)
    print(f'{x} - {y} = {x - y}')
    return absolute < tol


first = 0.8
second = 0.1 + 0.7
print(compare_float(first, second, tol=1e-10))  # 0.0000000001

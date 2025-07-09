def sum_numbers(a: int, b: int):
    return a + b


s = sum_numbers(10, 30)

print(sum_numbers(10, 20))
print(s)


def sum_number(a: int, b: int) -> float:
    result = float(a + b)
    return result

print(sum_number(3,4))

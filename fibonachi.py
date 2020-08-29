def fibonacci(x):
    a = b = 1
    arr = [0, 1]
    for i in range(x - 2):
        a, b = b, a + b
        arr.append(a)
    return arr


print(fibonacci(10))

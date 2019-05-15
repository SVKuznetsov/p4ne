def fib(n):
    a, b = 1, 1
    step = 0
    while step < n:
        yield b
        b, a = a + b, b
        step += 1

for i in fib(100):
        print(i)
fib(5)
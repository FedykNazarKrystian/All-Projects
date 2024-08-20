
def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

n = int(input('Please Enter Number for Fibonacci: '))
print(fibonacci(n))
fibonacci_list = []
for i in range(1, n+1):
    fibonacci_list.append(fibonacci(i))
print(fibonacci_list)

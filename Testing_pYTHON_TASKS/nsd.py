def nsd(a, b):
    min_num = min(a, b)
    dilnyk = []

    for i in range(2, min_num+1):
        if a % i == 0 and b % i == 0:
            dilnyk.append(i)
    return dilnyk

num1 = int(input('Please Enter First Number: '))
num2 = int(input('Please Enter Second Number: '))

result = min(nsd(num1, num2))
print(nsd(num1, num2))
print(result)


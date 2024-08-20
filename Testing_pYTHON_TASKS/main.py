def roman_to_integer(num):
    roman_num = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
    }

    result = 0
    digit = 0

    for i in num:
        sep_digit = roman_num[i]
        if sep_digit < digit:
            result -= sep_digit
        else:
            result += sep_digit
        digit = sep_digit
    return result


def integer_to_roman(num):
    roman_num = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }

    result = ''
    for dig, rom in roman_num.items():
        while num >= dig:
            result += rom
            num -= dig
    return result


nums = input("Введіть два римські числа у форматі 'I + IV': ")
num1, num2 = nums.split(' + ')

sum_result = roman_to_integer(num1) + roman_to_integer(num2)
print(integer_to_roman(sum_result))

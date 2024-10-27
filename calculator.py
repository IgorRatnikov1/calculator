# calculator
number1 = int(input("введите первое число"))
sign = input("введите символ")
number2 = int(input("введите второе число"))
if sign == "+":
    print(number1 + number2)
elif sing == "-":
    if number1 > number2:
        print(number1 - number2)
    else:
        print(number2 - number1)
elif sing == "/" and number2 != 0:
    print(number2 / number1)
elif sing == "*":
    print(number2 * number1)
else:
    print("я не знаю такого знака")
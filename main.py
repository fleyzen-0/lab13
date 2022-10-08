try:
    number1 = int(input("Введіть два числа: "))
    number2 = int(input())
    while number1 <= number2:
        c = (number1 + number1)
        number1 += 1
    print("Cума чисел у вказаному діапазоні: ", c)
    print("Середнє арифметичне: ", c / 2)

except Exception as ex:
    print("Erorr: ", ex);
finally:
    print("Завдання виконано.")



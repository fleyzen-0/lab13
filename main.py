try:
    line = int(input("Введіть довжину лінії: "))
    simvol = input("Введіть символ для заповнення")
    for item in range(0, line):
        print(simvol, end="")



except Exception as ex:
    print("Erorr: ", ex)
finally:
    print(" Завдання виконано.")

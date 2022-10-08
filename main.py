try:
    line = int(input("Введіть довжину лінії: "))
    for item in range(0, line):
        print("*", end="")



except Exception as ex:
    print("Erorr: ", ex)
finally:
    print(" Завдання виконано.")

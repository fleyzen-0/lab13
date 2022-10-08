try:
    begin = int(input("begin - "))
    end = int(input("begin - "))
    sum = 0
    for item in range(begin, end+1):
        print(f'{sum} + {item} =', end=" ")
        sum += item
        print(f'{sum}')
    print(f'Sum = {sum}')

except Exception as ex:
    print("Erorr: ", ex);
finally:
    print("Завдання виконано.")



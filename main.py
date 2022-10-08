try:
    number = int(input("numner = "))
    print(f'!{number} = ', end=" ")
    temp = 1
    for item in range(1, number+1):
        if item == number:
            print(item, end=" ")
        else:
            print(f'{temp} *', end=' ')

        temp*=item
    print(f'= {temp}')

except Exception as ex:
    print("Erorr: ", ex);
finally:
    print("Завдання виконано.")



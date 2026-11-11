while True:
    a=input("введите число: ")
    if a.isdigit():
        print("введено целое число: ", a)
        break
    else:
        print("ошибка. попробуйте еще раз. введите число", end=" ")
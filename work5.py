def sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input(f"Enter a number or Q to exit: ").split()
        res = 0
        for el in range(len(number)):
            if number[el] == "exit" or number[el] == "Exit":
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f"Current sum is {sum_res}")
    print(f"Your final sum is {sum_res}")

sum()
def division (*args):
    try:
        number1 = int(input(f"Enter the first number: "))
        number2 = int(input(f"Enter the second number: "))
        res = number1 / number2
    except BaseException:
        return ("ERROR. EXIT.")
        exit(-1)

    return int(res)

print(division())
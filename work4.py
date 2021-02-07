def func(x,y):
    a1 = x ** y
    a2 = 1
    i = 1
    while i <= abs(y):
        a2 *= x
        i += 1

    return a1, 1 / a2

print(

    func(
        int(input(f"a1: ")),
        int(input(f"a2: "))
    )
)
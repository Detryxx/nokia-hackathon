def fibonacci(n):
    fib_1 = 0
    fib_2 = 1
    fib_good = ["0"]

    if type(n) != int or n < 0:
        return "N/A"

    elif n == 0:
        return 0

    else:
        while fib_2 < n:
            fib_3 = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib_3
            if fib_2 > n:
                break
            elif fib_2 % 3 == 0:
                fib_good.append(fib_2)
    solution = ", ".join(str(x) for x in fib_good)
    return solution


with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        try:
            fib_input = int(line.strip("\n"))
        except ValueError:
            pass
        print(fibonacci(fib_input))
        line = file.readline()
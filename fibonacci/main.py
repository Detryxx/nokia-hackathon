"""
    Solves the exercise by seeing if a fibonacci number is divisible by three.
"""
def fibonacci(n):
    """
        Keyword arguments:
        n -- the number to check until

        This function takes all the fibonacci numbers which are divisible by three until the next
        fibonacci number is larger than n.
        This uses a way of generating fibonacci numbers augmented from GeeksForGeeks.
            Link to that article:
                https://www.geeksforgeeks.org/python-program-to-print-the-fibonacci-sequence/
    """
    fib_1 = 0
    fib_2 = 1
    fib_good = ["0"]

    if not isinstance(n, int) or n < 0: #if 'n' is not an integer it returns "N/A"
        return "N/A"

    if n == 0:  #if 'n' is zero, there is no "fibonaccification" to be done and it returns zero
        return 0

    while fib_2 < n:
        fib_3 = fib_1 + fib_2
        fib_1 = fib_2   #the aforementioned way of generating fibonacci numbers
        fib_2 = fib_3
        if fib_2 > n:   #if the fibonacci number gets above 'n' it stops the loop
            break
        if fib_2 % 3 == 0:  #if the fibonacci number mod 3 is 0 than
            fib_good.append(fib_2)  #it appends the number to the list of good numbers
    solution = ", ".join(str(x) for x in fib_good)  #makes the solution look like the example
    return solution #returns all fibonacci numbers divisible by 3 up to 'n'


with open("./input.txt", "r", encoding="utf-8") as file:    #opens the input file
    line = file.readline()  #reads a new line of the file
    while line: #while there are lines to be read
        try:     #it tries to convert the string to an integer
            fib_input = int(line.strip("\n"))   #if it can, it sets that as the value of fib_input
        except ValueError:  #when it encounters a ValueError it goes onto the next line
            pass
        print(fibonacci(fib_input)) #prints the output of the fib. func
        line = file.readline()  #actually reads the new line

# pylint: disable=C0103
"""
    random - needed for random number generation
    ast - needed for literal_eval [https://docs.python.org/3/library/ast.html#ast.literal_eval]
"""
import random as rnd
import ast

def left(lfirst, lsecond, lthird, x, moves):
    """
        'Pulls' the left lever.

        Keyword arguments:
        lfirst -- the first gears' shown value
        lsecond -- the second gears' shown value
        lthird -- the third gears' shown value
        x -- needed for no errors, a counter value but not used
        moves -- what moves were preformed

        Append one to the first and second gear, if the gears are at 4 it resets them to 1
    """
    lfirst += 1 #turns the first gear once
    if lfirst == 4: #if the first gear is at 4 now, it sets it back to 1
        lfirst = 1
    lsecond += 1    #turns the second gear once
    if lsecond == 4:    #if the second gear is at 4 now, it sets it back to 1
        lsecond = 1
    moves.append("left")    #adds 'left' to the moves made
    return lfirst, lsecond, lthird, x, moves    #returns the updated values


def right(rfirst, rsecond, rthird, x, moves):
    """
        'Pulls' the right lever.

        Keyword arguments:
        rfirst -- the first gears' shown value
        rsecond -- the second gears' shown value
        rthird -- the third gears' shown value
        x -- needed for no errors, a counter value but not used
        moves -- what moves were preformed

        Append one to the second and third gear, if the gears are at 4 it resets them to 1
    """
    rsecond += 1    #turns the second gear once
    if rsecond == 4:    #if the second gear is at 4 now, it sets it back to 1
        rsecond = 1
    rthird += 1 #turns the third gear once
    if rthird == 4: #if the third gear is at 4 now, it sets it back to 1
        rthird = 1
    moves.append("right")   #adds 'right' to the moves made
    return rfirst, rsecond, rthird, x, moves    #returns the updated values

def trial(tfirst, tsecond, tthird, counter, moves):
    """
        The actual solver, randomly 'pulls' one lever.

        Keyword arguments:
        tfirst -- the first gears' shown value
        tsecond -- the second gears' shown value
        tthird -- the third gears' shown value
        counter -- how many times the gears were moved
        moves -- what moves were preformed on the gears (left or right)
    """
    lor = rnd.randint(1,2)  #gets a random number between 1 and 2 inclusive
    counter += 1    #adds one to the counter, pertaining to the # of lever pulls
    if lor == 1:    #if the random number is one, the left lever is pulled
        return left(tfirst, tsecond, tthird, counter, moves)    #returns the state after the pull
    if lor == 2:    #if the random number is two, the right lever is pulled
        return right(tfirst, tsecond, tthird, counter, moves)   #returns the state after the pull
    return None #needed for PEP8 compliance

def solver(sfirst, ssecond, sthird, upper = 8):
    """
        Receives the needed output and solves it with the trial function.

        Keyword arguments:
        sfirst -- the first gears' shown value
        ssecond -- the second gears' shown value
        sthird -- the third gears' shown value

        Over 50000 iterations (works with 500 as well but used 50k for redundancy) tries a bunch of
        combinations of lever pulls with a maximum number of moves of 'upper'. Then it puts them
        into a dictionary with the # of moves as the key and the moves themselves as the value.
        And after that it checks for the smallest key and returns the value, which are the moves
        it took to get there.
    """
    solves = {} #makes a dictionary that will contain the hypothetic solutions
    for _ in range(50000):
        moves = []  #makes a list that will contain the moves made
            #makes distinct variables for output of the trial function
        fout, sout, tout, counter, moves = trial(3, 3, 3, 0, moves)
            #while the output of the trial function doesn't equal the needed values
        while fout != sfirst or sout != ssecond or tout != sthird:
                #uses the trial function again
            fout, sout, tout, counter, moves = trial(fout, sout , tout, counter, moves)
            if counter >= (upper + 1):  #if the counter is more than or equal to the upper limit + 1
                break

        solves[counter] = moves #adds the solution to the solves dictionary


    for k, v in sorted(solves.items()): #exctracts the sorted keys and the values of the solves dict
        if k <= upper:  #if the value of a key is less than the max value
            return " ".join(v)  #it returns the value as the solution
        return "Megoldhatatlan" #if it can't, it returns "Megoldhatatlan" according to the exercise
    return None #needed for PEP8 compliance


with open("./input.txt", "r", encoding="utf-8") as file:    #opens the input file
    line = file.readline()  #reads a line of the file
    while line: #while there is a line to be read
        try:
                #tries to convert the string at the third index to an integer to set that as the max
            maximum = int(line.strip().split(" ")[3])
        except IndexError:  #if it can't, it defaults it to 8
            maximum = 8 #
        first, second, third = ast.literal_eval(line[:9])   #extracts the needed values
        print(solver(first, second, third, maximum))    #prints the return of the solver function
        line = file.readline()  #reads a new line

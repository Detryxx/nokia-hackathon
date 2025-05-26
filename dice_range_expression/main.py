"""
    Solves the exercise by subtracting the biggest dice value it can
"""
def dice_range_expression(min_val: int, max_val: int):
    """
    Keyword arguments:
    min_val -- The minimum value of the dice roll
    max_val -- The maximum value of the dice roll

    If the minimum value is positive, the 'biggest' variable is the difference of
    the minimum plus one subtracted from the maximum and the offset is the 'biggest'
    subtracted from the maximum.
    If the minimum value is negative, the 'biggest' variable is the same, but the offset is the
    minimum minus one. Then, if the current die value subtracted from the 'biggest' is more than or
    equal to zero and is odd, it subtracts 3 and adds that to the list of needed dice, because
    that's to only odd number in the allowed dice.
    After that if the size subtracted from the 'biggest' is more than or equal to zero, and is even,
    it adds that to the list of needed dice, and subtracts that number from the 'biggest'.
    It then sorts it descending according to the exercise and when printing it makes it look
    according to the exercise.
    """
    dice_sizes = (20, 10, 8, 6, 4, 3, 2)    #dice sizes allowed
    if min_val >= 0:
        biggest = max_val - min_val + 1
        offset = max_val - biggest
    else:
        biggest = max_val - min_val + 1
        offset = min_val - 1
    needed_dice = []

    for size in dice_sizes:     #takes the items of the dice sizes tuple
        while biggest - size >= 0 and biggest % 2 != 0: #while biggest - size is positive and odd
            needed_dice.append(3)   #it appends 3 to the list of needed dice
            biggest -= 3    #and subtracts 3 from the 'biggest' because that's the only odd dice
        while biggest - size >= 0 and biggest % 2 == 0: #while biggest - size is positive and even
            needed_dice.append(size)    #it appends that die to the list of needed dice
            biggest -= size #and subtracts it from the 'biggest'

    needed_dice.sort(reverse=True)  #sorts the needed dice in descending order
    dice_dict = {}  #creates a dictionary to keep track of how many of each die we have
    for x in needed_dice:
        y = needed_dice.count(x) #counts the appearances of the value x die in the needed dice list
        dice_dict[x] = y    #adds that to the dictionary with the dice value as the key
    final_dice = "" #creates an empty string for the final return
    for k, v in dice_dict.items():
        final_dice += f"{v}d{k}+"   #adds the dice and their respective counts to the final_dice str
    if offset > 0:
        offset = f"+{offset}"   #if the offset is positive, it adds a plus sign to it
    elif offset < 0:
        pass    #if the offset is negative no minus is needed, because it is already stored with one
    else:
        offset = "" #if there is no offset needed, it sets an empty string as the offset
    return f"{final_dice.rstrip('+')}{offset}"  #returns the solution to the respective inputs

with open("./input.txt", "r", encoding="utf-8") as file:    #opens the input file in read mode
    line = file.readline()  #reads a line
    while line: #while there can still be lines read
        minimum = int(line.strip().split(" ")[0])   #sets the fist value as the minimum
        maximum = int(line.strip().split(" ")[1])   #sets the second value as the maximum
        print(dice_range_expression(minimum, maximum))  #prints the solution
        line = file.readline()  #reads another line

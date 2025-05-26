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
    dice_sizes = (20, 10, 8, 6, 4, 3, 2)
    if min_val >= 0:
        biggest = max_val - min_val + 1
        offset = max_val - biggest
    else:
        biggest = max_val - min_val + 1
        offset = min_val - 1
    needed_dice = []

    for size in dice_sizes:
        while biggest - size >= 0 and biggest % 2 != 0:
            needed_dice.append(3)
            biggest -= 3
        while biggest - size >= 0 and biggest % 2 == 0:
            needed_dice.append(size)
            biggest -= size

    needed_dice.sort(reverse=True)
    dice_dict = {}
    for x in needed_dice:
        y = needed_dice.count(x)
        dice_dict[x] = y
    final_dice = ""
    for k, v in dice_dict.items():
        final_dice += f"{v}d{k}+"
    if offset > 0:
        offset = f"+{offset}"
    elif offset < 0:
        pass
    else:
        offset = ""
    print(f"{final_dice.rstrip('+')}{offset}")

with open("./input.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    while line:
        minimum = int(line.strip().split(" ")[0])
        maximum = int(line.strip().split(" ")[1])
        dice_range_expression(minimum, maximum)
        line = file.readline()

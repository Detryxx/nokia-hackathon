def dice_range_expression(min_val: int, max_val: int):
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
            while biggest % 2 != 0 and biggest - size >= 0:
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
        offset = offset
    else:
        offset = ""
    print(f"{final_dice.rstrip("+")}{offset}")

with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        min = int(line.strip().split(" ")[0])
        max = int(line.strip().split(" ")[1])
        dice_range_expression(min, max)0
        line = file.readline()

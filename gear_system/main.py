import random as rnd
import ast
#
# def left_lever(current_state: list) -> list:
#   current_state[0] += 1
#   current_state[1] += 1
#   return current_state
#
# def right_lever(current_state: list) -> list:
#   current_state[1] += 1
#   current_state[2] += 1
#   return current_state
#
# def trial(current_state: list) -> list:
#   lor = rnd.randint(1, 2)
#   if lor == 1:
#     current_state = left_lever(current_state)
#   elif lor == 2:
#     current_state= right_lever(current_state)
#   print(current_state, "asdasd")
#   return current_state
#
# def gear_system(end_result: list, max_moves: int = 8,):
#   first = 3
#   second = 3
#   third = 3
#   left = first + 1, second + 1
#   right = second + 1, third + 1
#   counter = 0
#   states = [first, second, third]
#   required_moves = []
#   while end_result != states:
#     for x in range(0, 3):
#       print(x, "ketiksz")
#       states[x] = (states[x] - 1) % 4
#       print(x, "iksz")
#     states = trial(states)
#   print(states)
#
#
# gear_system([2, 1, 2])

def left(first, second, third, x, moves):
  first += 1
  if first == 4:
    first = 1
  second += 1
  if second == 4:
    second = 1
  if third == 4:
    third = 1
  moves.append("left")
  return first, second, third, x, moves


def right(first, second, third, x, moves):
  if first == 4:
    first = 1
  second += 1
  if second == 4:
    second = 1
  third += 1
  if third == 4:
    third = 1
  moves.append("right")
  return first, second, third, x, moves

def trial(first, second, third, counter, moves):
  lor = rnd.randint(1,2)
  counter += 1
  if lor == 1:
    return left(first, second, third, counter, moves)
  elif lor == 2:
    return right(first, second, third, counter, moves)

def solver(first, second, third, upper = 8):
  solves = {}
  for i in range(500):
    moves = []
    fout, sout, tout, counter, moves = trial(3, 3, 3, 0, moves)
    while fout != first or sout != second or tout != third:
      fout, sout, tout, counter, moves = trial(fout, sout , tout, counter, moves)
      if counter >= (upper + 1):
        break

    solves[counter] = moves


  for k, v in sorted(solves.items()):
    if k <= upper:
      return " ".join(v)
    else:
      return "Megoldhatatlan"


with open("./input.txt", "r") as file:
  line = file.readline()
  while line:
    try:
      max = int(line.strip().split(" ")[3])
    except Exception:
      max = 8
    first, second, third = ast.literal_eval(line[:9])
    print(solver(first, second, third, max))
    line = file.readline()


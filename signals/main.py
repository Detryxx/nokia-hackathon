# Feladatmappa:
#
# signals
# Leírás:
#
# Feladatod hogy dekódold két ellenséges bázis közötti rádió kommunikációt. Belehallgatva a rádióadásukba, rövid csipogásokat hallasz és egy rövid szünetet egy-egy adag csipogás között. Úgy tűnik ez egy kód, gyorsan fel is jegyezted a hallottakat amelyek a következők: 3.4 (3 csipogás, majd egy rövid szünet, majd 4 csipogás) 2.1.2.4 (2 csipogás, 1 csipogás, 2 csipogás, 4 csipogás)
#
# A kódokat minden nap reggelén közvetítik. A nap folyamán történteket is feljegyezted: jelek = [“3.4”, “2.1.2.4”] esemenyek = [“A”, “B”] (Tudjuk, hogy "3.4" és "2.1.2.4" biztosan az "A" és "B" eseményhez köthetőek, de nem tudjuk melyik kód melyik eseméynt jelenti.)
#
# Több napnyi kód összehasonlításával meg tudod fejteni a kódokat; a megoldás pedig így néz ki. decoded = {“3.4”: “B”, “2.1.2.4”: “A”}
#
# Továbbá: - Több napnyi jeleket és eseményeket fogsz kapni, melyeket fel kell majd dolgoznod. - Minden kód csak egy eseményt jelenthet, viszont egy eseménynek lehet több különböző kódja is. - Mindig lesz elegendő információ a feladat megoldásához.
# Bemenet:
#
# A bemenet egy lista lesz, amelyben minden egyes napot egy-egy tuple fog reprezentálni. Egy adott naphoz tartozó tuple-ben lesz két lista:
#
#     Az első lista tartalmazza az adott nap reggelén hallott kódokat mint string-ek (pl.: ["5", "3.4", "2.1.2.4"])
#     A második listában pedig az adott nap eseményei lesznek mint betűk (pl.: ["A", "B", "O", "I"])
#
# Kimenet:
#
# A programnak az adott lista bemenetre ki kell írnia a megfejtést egy dictionary-be rendezve a következő péda szerint. Fontos, hogy a ditonary kulcsaiként szerepeljenek stringként a kódok, az értékeik pedig a történések betűjelei legyenek szintén mint string.
# Példa:
#
# input.txt
#
# [
#     (["4.1", "5"], ["A", "O"]),
#     (["4.1", "5", "1.2.3"], ["T", "O", "A"]),
#     (["5"], ["O"])
# ]
#
# console printout:
#
# {
#     "5": "O",
#     "4.1": "A",
#     "1.2.3": "T"
# }
#
#
# (['8.6.4', '5.9.1', '9.3.8', '6.7.4', '8', '1', '3.8', '7.4', '6'], ['A', 'B', 'C', 'D', 'D', 'E', 'F', 'D', 'G']),
# (['7.1.8', '1', '9.3.8', '7.4', '3.9', '8.6.4'], ['B', 'D', 'H', 'G', 'I', 'D']),
# (['9.3.8', '3.9'], ['I', 'G']),
# (['8.6.4', '7.1.8', '9'], ['D', 'H', 'A']),
# (['6', '1', '8.6.4', '5.9.1', '9.3.8'], ['C', 'G', 'A', 'D', 'D']),
# (['6', '7.4', '3.8', '1', '5.9.1', '9.3.8'], ['D', 'G', 'C', 'D', 'B', 'A']),
# (['5.9.1'], ['A']),
# (['7.1.8', '8.6.4', '7.4', '6.7.4', '9.3.8'], ['D', 'B', 'H', 'F', 'G']),
# (['1', '5.9.1', '7.1.8', '6.7.4', '3.9', '6', '8.6.4', '7.4'], ['B', 'D', 'C', 'H', 'A', 'F', 'D', 'I'])
from dataclasses import asdict


def get_days(input_file) -> dict:
    with open(input_file, 'r') as file:
        line = file.readline().strip()
        counter = 0
        days = {}
        while line:
            counter += 1
            days["day{0}".format(counter)] = line.strip()
            line = file.readline().strip()
        print(days)
        return days


def decode(input_file):
    days = get_days(input_file)
    counter = 0
    coded = {}
    for k, v in days.items():
        code, event = v.split("], [")
        code = code.lstrip("([")
        event = event.rstrip("]),")
        print(code, event, "\n \n")
decode("input.txt")


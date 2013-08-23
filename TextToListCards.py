import sys

if len(sys.argv) != 2:
    print("Must pass card list text file to program.")
    exit(0)

cardListText = sys.argv[1]

f = open(cardListText)
cards = []
for line in f:
    ind = line.find("(")
    if ind >= 0:
        line = line[:ind-1]
    else:
        line = line[:-1]
    cards.append(line)

print(cards)

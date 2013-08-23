import sys

if len(sys.argv) != 2:
    print "Must pass card list text file to program."
    exit(0)

cardListText = sys.argv[1]

f = open(cardListText)
cards = []
for line in f:
    ind = line.find("\t")
    if ind >= 0:
        line = line[ind+1:].strip().replace("\xe2\x80\x99","'")

        if line == "Jack of All Trades":
            line = "Jack of all Trades"
        if line == "Hermit":
            line = "Hermit/Madman"
        if line == "Urchin":
            line = "Urchin/Mercenary"

        cards.append(line)

for c in cards:
    print c

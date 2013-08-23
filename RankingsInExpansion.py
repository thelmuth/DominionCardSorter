import sys
import re

# This program takes as input a list of cards sorted from favorite to least
# favorite (or best to worst). It then asks which expansion you are interested
# in, and prints the rankings of cards from that expansion.

if len(sys.argv) != 2:
    print("Takes 1 argument: list of cards ordered favorite to least favorite.")
    exit(0)

try: input = raw_input
except NameError: pass

f2 = open("CardLists/AllCards.txt")
expansionMap = {}
regexp = re.compile(r'(.*) \((.*)\)')
for line in f2:
    match = re.search(regexp, line)
    (card, expansion) = match.groups()
    expansionMap[card] = expansion

expansions = ["Base", "Intrigue", "Seaside", "Alchemy", "Prosperity", "Cornucopia", "Hinterlands", "Dark Ages", "Guilds", "Promo"]

print("Enter the number of the expansion would you like to display the cards from:")
for i,exp in enumerate(expansions):
    print("  %i. %s" % (i+1, exp))
expOfInterestNum = '0'
while expOfInterestNum not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
    expOfInterestNum = input("Choice: ")

expOfInterest = expansions[int(expOfInterestNum) - 1]

print('')
print("Ranks of cards from " + expOfInterest + ":")

cardListText = sys.argv[1]

f = open(cardListText)
cards = []
for rank, line in enumerate(f):
    ind = line.find("(")
    if ind >= 0:
        line = line[:ind-1]
    else:
        line = line[:-1]

    if expansionMap[line] == expOfInterest:
        print("%-3i %s" % (rank+1, line))

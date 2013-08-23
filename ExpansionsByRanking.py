import sys
import re
import operator

# This program takes as input a list of cards sorted from favorite to least
# favorite (or best to worst). It then prints a list of the expansions, sorted by the average position of cards from that expansion.

if len(sys.argv) != 2:
    print("Takes 1 argument: list of cards ordered favorite to least favorite.")
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

f2 = open("CardLists/AllCards.txt")
expansionMap = {}
regexp = re.compile(r'(.*) \((.*)\)')
for line in f2:
    match = re.search(regexp, line)
    (card, expansion) = match.groups()
    expansionMap[card] = expansion

expansionRankings = [expansionMap[card] for card in cards]

countMap = {}
rankSumMap = {}
for r, exp in enumerate(expansionRankings):
    if exp not in countMap:
        countMap[exp] = 0
        rankSumMap[exp] = 0
    countMap[exp] = countMap[exp] + 1
    rankSumMap[exp] = rankSumMap[exp] + r + 1

avgRankMap = {}
for exp in countMap.keys():
    avgRank = rankSumMap[exp] / float(countMap[exp])
    avgRankMap[exp] = avgRank

sortedExps = sorted(avgRankMap.items(), key=operator.itemgetter(1))

print("The expansions sorted by average rank of cards in that expansion:")

for (exp, rank) in sortedExps:
    print("%-11s %.1f" % (exp, rank))

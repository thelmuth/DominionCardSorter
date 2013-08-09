import sys
import re

if len(sys.argv) != 2:
    print "Takes 1 argument: list of cards ordered favorite to least favorite."
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

f2 = open("AllCards.txt")
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
    if not countMap.has_key(exp):
        countMap[exp] = 0
        rankSumMap[exp] = 0
    countMap[exp] = countMap[exp] + 1
    rankSumMap[exp] = rankSumMap[exp] + r + 1

for exp in countMap.keys():
    avgRank = rankSumMap[exp] / float(countMap[exp])
    print "%-11s %.1f" % (exp, avgRank)
        

import random
from functools import cmp_to_key

allCards = ['Cellar', 'Chapel', 'Moat', 'Courtyard', 'Pawn', 'Secret Chamber', 'Embargo', 'Haven', 'Lighthouse', 'Native Village', 'Pearl Diver', 'Herbalist', 'Hamlet', 'Crossroads', 'Duchess', "Fool's Gold", 'Beggar', 'Poor House', 'Squire', 'Vagrant', 'Candlestick Maker', 'Stonemason', 'Chancellor', 'Village', 'Woodcutter', 'Workshop', 'Great Hall', 'Masquerade', 'Shanty Town', 'Steward', 'Swindler', 'Wishing Well', 'Ambassador', 'Fishing Village', 'Lookout', 'Smugglers', 'Warehouse', 'Loan', 'Trade Route', 'Watchtower', 'Fortune Teller', 'Menagerie', 'Develop', 'Oasis', 'Oracle', 'Scheme', 'Tunnel', 'Forager', 'Hermit/Madman', 'Market Square', 'Sage', 'Storeroom', 'Urchin/Mercenary', 'Doctor', 'Masterpiece', 'Black Market', 'Bureaucrat', 'Feast', 'Gardens', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief', 'Throne Room', 'Baron', 'Bridge', 'Conspirator', 'Coppersmith', 'Ironworks', 'Mining Village', 'Scout', 'Caravan', 'Cutpurse', 'Island', 'Navigator', 'Pirate Ship', 'Salvager', 'Sea Hag', 'Treasure Map', 'Bishop', 'Monument', 'Quarry', 'Talisman', "Worker's Village", 'Farming Village', 'Horse Traders', 'Remake', 'Tournament', 'Young Witch', 'Jack of all Trades', 'Noble Brigand', 'Nomad Camp', 'Silk Road', 'Spice Merchant', 'Trader', 'Armory', 'Death Cart', 'Feodum', 'Fortress', 'Ironmonger', 'Marauder', 'Procession', 'Rats', 'Scavenger', 'Wandering Minstrel', 'Advisor', 'Herald', 'Plaza', 'Taxman', 'Envoy', 'Walled Village', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Market', 'Mine', 'Witch', 'Duke', 'Minion', 'Saboteur', 'Torturer', 'Trading Post', 'Tribute', 'Upgrade', 'Bazaar', 'Explorer', 'Ghost Ship', 'Merchant Ship', 'Outpost', 'Tactician', 'Treasury', 'Wharf', 'Apprentice', 'City', 'Contraband', 'Counting House', 'Mint', 'Mountebank', 'Rabble', 'Royal Seal', 'Vault', 'Venture', 'Harvest', 'Horn of Plenty', 'Hunting Party', 'Jester', 'Cache', 'Cartographer', 'Embassy', 'Haggler', 'Highway', 'Ill-Gotten Gains', 'Inn', 'Mandarin', 'Margrave', 'Stables', 'Bandit Camp', 'Band of Misfits', 'Catacombs', 'Counterfeit', 'Count', 'Cultist', 'Graverobber', 'Junk Dealer', 'Knights', 'Mystic', 'Pillage', 'Rebuild', 'Rogue', 'Baker', 'Butcher', 'Journeyman', 'Merchant Guild', 'Soothsayer', 'Governor', 'Stash', 'Adventurer', 'Harem', 'Nobles', 'Goons', 'Grand Market', 'Hoard', 'Bank', 'Expand', 'Forge', "King's Court", 'Peddler', 'Fairgrounds', 'Border Village', 'Farmland', 'Altar', 'Hunting Grounds', 'Transmute', 'Vineyard', 'Apothecary', 'Scrying Pool', 'University', 'Alchemist', 'Familiar', "Philosopher's Stone", 'Golem', 'Possession']

oneAndTwo = ['Cellar', 'Chapel', 'Moat', 'Courtyard', 'Pawn', 'Secret Chamber', 'Embargo', 'Haven', 'Lighthouse', 'Native Village', 'Pearl Diver', 'Herbalist', 'Hamlet', 'Crossroads', 'Duchess', "Fool's Gold", 'Beggar', 'Poor House', 'Squire', 'Vagrant', 'Candlestick Maker', 'Stonemason']

three = ['Chancellor', 'Village', 'Woodcutter', 'Workshop', 'Great Hall', 'Masquerade', 'Shanty Town', 'Steward', 'Swindler', 'Wishing Well', 'Ambassador', 'Fishing Village', 'Lookout', 'Smugglers', 'Warehouse', 'Loan', 'Trade Route', 'Watchtower', 'Fortune Teller', 'Menagerie', 'Develop', 'Oasis', 'Oracle', 'Scheme', 'Tunnel', 'Forager', 'Hermit/Madman', 'Market Square', 'Sage', 'Storeroom', 'Urchin/Mercenary', 'Doctor', 'Masterpiece', 'Black Market']

four = ['Bureaucrat', 'Feast', 'Gardens', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief', 'Throne Room', 'Baron', 'Bridge', 'Conspirator', 'Coppersmith', 'Ironworks', 'Mining Village', 'Scout', 'Caravan', 'Cutpurse', 'Island', 'Navigator', 'Pirate Ship', 'Salvager', 'Sea Hag', 'Treasure Map', 'Bishop', 'Monument', 'Quarry', 'Talisman', "Worker's Village", 'Farming Village', 'Horse Traders', 'Remake', 'Tournament', 'Young Witch', 'Jack of all Trades', 'Noble Brigand', 'Nomad Camp', 'Silk Road', 'Spice Merchant', 'Trader', 'Armory', 'Death Cart', 'Feodum', 'Fortress', 'Ironmonger', 'Marauder', 'Procession', 'Rats', 'Scavenger', 'Wandering Minstrel', 'Advisor', 'Herald', 'Plaza', 'Taxman', 'Envoy', 'Walled Village']

five = ['Council Room', 'Festival', 'Laboratory', 'Library', 'Market', 'Mine', 'Witch', 'Duke', 'Minion', 'Saboteur', 'Torturer', 'Trading Post', 'Tribute', 'Upgrade', 'Bazaar', 'Explorer', 'Ghost Ship', 'Merchant Ship', 'Outpost', 'Tactician', 'Treasury', 'Wharf', 'Apprentice', 'City', 'Contraband', 'Counting House', 'Mint', 'Mountebank', 'Rabble', 'Royal Seal', 'Vault', 'Venture', 'Harvest', 'Horn of Plenty', 'Hunting Party', 'Jester', 'Cache', 'Cartographer', 'Embassy', 'Haggler', 'Highway', 'Ill-Gotten Gains', 'Inn', 'Mandarin', 'Margrave', 'Stables', 'Bandit Camp', 'Band of Misfits', 'Catacombs', 'Counterfeit', 'Count', 'Cultist', 'Graverobber', 'Junk Dealer', 'Knights', 'Mystic', 'Pillage', 'Rebuild', 'Rogue', 'Baker', 'Butcher', 'Journeyman', 'Merchant Guild', 'Soothsayer', 'Governor', 'Stash']

sixPlus = ['Adventurer', 'Harem', 'Nobles', 'Goons', 'Grand Market', 'Hoard', 'Bank', 'Expand', 'Forge', "King's Court", 'Peddler', 'Fairgrounds', 'Border Village', 'Farmland', 'Altar', 'Hunting Grounds']

potion = ['Transmute', 'Vineyard', 'Apothecary', 'Scrying Pool', 'University', 'Alchemist', 'Familiar', "Philosopher's Stone", 'Golem', 'Possession']

prizes = ['Bag of Gold', 'Diadem', 'Trusty Steed', 'Followers', 'Princess']

knights = ['Sir Martin', 'Dame Anna', 'Dame Josephine', 'Dame Molly', 'Dame Natalie', 'Dame Sylvia', 'Sir Bailey', 'Sir Destry', 'Sir Michael', 'Sir Vander']

ruins = ['Ruined Village', 'Ruined Library', 'Ruined Market', 'Abandoned Mine', 'Survivors']

#####

try: input = raw_input
except NameError: pass

print("Enter the number of the list you wish to sort:")
print("  1. All Cards")
print("  2. Cards costing $1 and $2")
print("  3. Cards costing $3")
print("  4. Cards costing $4")
print("  5. Cards costing $5")
print("  6. Cards costing $6 and more")
print("  7. Cards with Potion in their cost")
print("  8. Prizes")
print("  9. Knights")
print("  10. Ruins")
set = '0'
while set not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
    set = input("Choice: ")

print('')

sets = [allCards, oneAndTwo, three, four, five, sixPlus, potion, prizes, knights, ruins]
cards = sets[int(set) - 1]
random.shuffle(cards)

#####

# Comparator
comparisons = 0
def human_card_comparator(card1, card2):
    global comparisons
    comparisons += 1
    print('')
    print("Select card you think is better:")
    print("1. %s" % card1)
    print("2. %s" % card2)
    choice = 'a'
    while choice != '1' and choice != '2':
        choice = input("Choice: ")
    if choice == '1':
        return -1
    else:
        return 1

cards.sort(key=cmp_to_key(human_card_comparator))

print('')
print("Your ordering after %i comparisons is:" % comparisons)
print('')
for card in cards:
    print(card)
print('')

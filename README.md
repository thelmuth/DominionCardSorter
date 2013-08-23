DominionCardSorter
==================

Contains utilities for sorting lists of Dominion cards. These include:

DominionCardSorter.py
---------------------
This is the main utility. You can use it to sort different lists of Dominion cards, such as $4 cards, Potion cost cards, Knights, and Ruins. Use it from command line with `python DominionCardSorter.py`.


ExpansionsByRanking.py
----------------------
This program takes a list of all the cards that you have sorted into some sort of order, with better (or more favorite) cards coming earlier. It then prints the expansions sorted by the average ranks of the cards in each expansion. For example, to print the expansions using Wandering Winder's Power Rankings 2, you can type `python ExpansionsByRanking.py CardLists/WWPowerRankings2.txt`.

RankingsInExpansion.py
----------------------
This program is similar to ExpansionsByRanking.py. It takes a list of all the cards sorted into an order. It then asks which expansion you are interested in, and prints all of the cards from that expansion along with their ranks in your list. For example, if you want to use Wandering Winder's Power Rankings 2, you can type `python RankingsInExpansion.py CardLists/WWPowerRankings2.txt`.

TextCardsToPythonList.py
------------------------
This is a utility program that takes in a file that contains a list of cards, possibly with expansions after them, and prints a Python-formatted list of cards from that file.

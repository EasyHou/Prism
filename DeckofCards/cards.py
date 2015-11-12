import random

class Deck(object):
	"""A deck of 52 standard cards"""
	def __init__(self):
		self.cards = []
		self.discard = []
		for suit in range(4):
			for number in range(13):
				new_card = Card(suit, number)
				self.cards.append(new_card)
		self.Shuffle()
	
	def Shuffle(self):
		"""Adds all discarded cards back into the deck and randomly 
		shuffles the full deck"""

		self.cards += self.discard
		random.shuffle(self.cards)

	def GetNextCard(self):
		"""Removes the first/top playing card of the deck"""
		try:
			drawn = self.cards.pop(0)
			self.discard.append(drawn)
			return drawn
		except:
			print("There isn't any cards left in the deck! Shuffle the deck!")



class Card(object):
	"""A standard playing cards

	"""
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
	numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
				"Jack", "Queen", "King"]

	def __init__(self, suit, number):
		self.suit = suit
		self.number = number

	def __str__(self):
		return "%s of %s" % (Card.numbers[self.number], Card.suits[self.suit])

	def __repr__(self):
			return "%s of %s" % (Card.numbers[self.number], Card.suits[self.suit])





class Card:
    def __init__(self, cardName, cardValue, cardImage):
        self.cardName = cardName
        self.cardValue = int(cardValue)
        self.cardImage = cardImage
    def __str__(self):
        return f"{self.cardImage}"


class CardDeck:
    def __init__(self):
        self.deck = []
        types = ['♠', '♥', '♦', '♣']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in types:
            for value in values:
                if value in ['J', 'Q', 'K']:
                    card_value = 10
                elif value == 'A':
                    card_value = 11
                else:
                    card_value = int(value)
                card_name = value + suit
                card_image = f".----------.\n|{value.ljust(2)}        |\n|    {suit}     |\n|          |\n|          |\n|    {suit}     |\n|        {value.rjust(2)}|\n`----------'"

                self.deck.append(Card(card_name, card_value, card_image))

    #ChatGPT cheat "the CardDeck class now implements the __iter__ method which initializes the current_index attribute to 0 
    #and returns self as the iterator object. It also implements the __next__ method which checks if the current index is 
    #less than the length of the deck list, and if it is, returns the card at the current index and increments the index. 
    #If the current index is equal to or greater than the length of the deck list, 
    #it raises a StopIteration exception to signal the end of the iteration."

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.deck):
            raise StopIteration
        else:
            card = self.deck[self.current_index]
            self.current_index += 1
            return card

    
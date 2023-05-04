
class Card:
    def __init__(self, cardName, cardValue, cardImage):
        self.cardName = cardName
        self.cardValue = int(cardValue)
        self.cardImage = cardImage



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

    #ChatGPT cheat-code below because I could not figure why i could not iterate through the whole deck to initialize it (to be fair, it was before we went through Python class/magic methods in-lesson)

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

    
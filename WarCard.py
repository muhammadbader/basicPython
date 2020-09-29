
Values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}
Suits=('Hears','Diamonds','Spades','Clubs')
Ranks = [v for v in Values.keys()]

import random
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=Values[self.rank]
    def __str__(self):
        return self.rank +" of "+self.suit


class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in Suits:
            for rank in Ranks:
                self.all_cards.append(Card(suit,rank))


    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():
    def __init__(self,name):
        self.all_cards=[]
        self.name=name

    def take_card(self,card):
        if type(card)==type([]):
            self.all_cards.extend(card)
        else:
            self.all_cards.append(card)


    def give_card(self):
        return self.all_cards.pop(0)

    def shuffle(self):
        random.shuffle(self.all_cards)
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"


def Play_the_Card_Game(p1 = "kassem",p2 = "alfred"):
    player_one=Player(p1)
    player_two=Player(p2)
    deck=Deck()
    deck.shuffle_deck()
    for i in range(26):
        player_one.take_card(deck.deal_one())
        player_two.take_card(deck.deal_one())
    game_on=True

    round_number=0
    while game_on:
        round_number+=1
        if len(player_one.all_cards)==52:
            print("the WINNER:", end=" ")
            print(player_one)
            break
        elif len(player_two.all_cards)==52:
            print("the WINNER:", end=" ")
            print(player_two)
            break


        player_one_cards=[player_one.give_card()]
        player_two_cards=[player_two.give_card()]
        war_on = False
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.take_card(player_one_cards)
            player_one.take_card(player_two_cards)
        elif player_one_cards[-1].value<player_two_cards[-1].value:
            player_two.take_card(player_one_cards)
            player_two.take_card(player_two_cards)
        else:
            war_on=True

        while war_on:
            if len(player_one.all_cards) < 5:
                print("the WINNER:", end=" ")
                print(player_two)
                game_on=False
                break
            elif len(player_two.all_cards) < 5:
                print("the WINNER:",end=" ")
                print(player_one)
                game_on = False
                break

            for i in range(3):
                player_one_cards.append(player_one.give_card())
                player_two_cards.append(player_two.give_card())


            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.take_card(player_one_cards)
                player_one.take_card(player_two_cards)
                war_on = False
                player_one.shuffle()
                player_two.shuffle()
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.take_card(player_one_cards)
                player_two.take_card(player_two_cards)
                war_on = False
                player_one.shuffle()
                player_two.shuffle()


    print(f"they have player: {round_number} Rounds")


# Play_the_Card_Game("Yasir","Nihal")



''' 
            decorators
'''


def hello(name = "Jose"):
    print("Hello() function has been executed")

    def greet():
        return "\t this is the greet() function inside hello()"
    def welcome():
        return "\t this is the welcome() function inside hello()"

    # print(greet())
    # print(welcome())
    # print("this is the end of hello() func")
    print("I am going to return a func")

    if name=="Jose":
        return greet
    else:
        return welcome

def new_decorator(originsal_func):


    def wrap_func():
        print("Some extra code, before the original function")

        originsal_func()

        print("Some extra code, after the original function")

    return wrap_func

@new_decorator
def need_decorator():
    print("I want to be decorated!!")


# need_decorator()




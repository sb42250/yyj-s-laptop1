## Do not change import statements.
import unittest
from SI508_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code. (That's okay!)
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
class card_test(unittest.TestCase):

    def test_suit1(self):
        self.assertEqual(Card(0,1).suit,"Diamonds")
    def test_rank1(self):
        self.assertEqual(Card(0,1).rank,"Ace")
    def test_suit2(self):
        self.assertEqual(Card(3,2).suit,"Spades")
    def test_rank_num(self):
        self.assertEqual(Card(3,2).rank_num,2)
    def test_rank_num_int(self):
        self.assertTrue(type(Card(3,2).rank_num) == int)
    def test_rank2(self):
        self.assertEqual(Card(3,2).rank,2)
    def test_card_return(self):
        self.assertEqual(Card.__str__(Card(3,1)),"Ace of Spades" )

class deck_test(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    def test_deck_length(self):
        self.assertEqual(len(self.deck.cards),52)
    def test_Cardsdic (self):
        self.assertTrue(Card(3,2) in self.deck.cards)   
    def test_pop (self):
        for i in range(len(self.deck.cards)):
            x = self.deck.pop_card()
        self.assertEqual(self.deck.cards,[])
    def test_replace (self):
        x = Card(3,1)
        card_strs = []
        self.deck.replace_card(x)
        for c in self.deck.cards:
            card_strs.append(c.__str__())
        self.assertIn(x.__str__(),card_strs)
    def test_sort(self):
        x = self.deck.pop_card()
        self.deck.sort_cards()
        y = Deck().cards[:-1]
        card_strs = []
        card_strs_2 = []
        for c in self.deck.cards:
            card_strs.append(c.__str__())
        for card in y:
            card_strs_2.append(card.__str__())
        self.assertEqual(card_strs, card_strs_2)
    def test_deal_hand(self):
        hand_cards = []
        for c in self.deck.cards:
            hand_cards.append(c.__str__())
        self.assertEqual(hand_cards,self.deck.deal_hand(52))
        
class play_war_game_test(unittest.TestCase):
    def setUp(self):
        
    def test_play_scope(self):
        self.assertEqual(type(play_war_game(testing= True).p1_score), int)

if __name__ == "__main__":
    unittest.main(verbosity=2)
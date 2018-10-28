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
        self.assertEqual(Card.__str__(Card(3,2)),"2 of Spades" )

class deck_test(unittest.TestCase):
    def test_Cardsdic (self):
        self.assertTrue(Card(3,2) in Deck.cards)
    def test_deck_return (self):
        self.assertTrue("Ace of Diamonds" in Deck.total)    
    def test_pop (self):
        Deck.pop_card(self)
        self.assertTrue(Card(3,13) not in self.cards)
    def test_replace (self):
        Deck.replace_card(Card(3,2))
        self.assertTrue("2 of Spades" in card_strs)
        
class play_war_game_test(unittest.TestCase):
    def test_play_scope(self):
        self.assertTrue(type(p1_score) == int)

if __name__ == "__main__":
    unittest.main(verbosity=2)
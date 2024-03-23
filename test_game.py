import unittest
from game import DiceGame

class TestGame(unittest.TestCase):
    def test_calcProbFirstTurn(self):
        diceGame = DiceGame(3, "Alice")
        self.assertEqual(diceGame.calcProbFirstTurn(3), 1/3)
        self.assertEqual(diceGame.calcProbFirstTurn(90), 1/90)
    
    def test_calcProbSecondTurn(self):
        diceGame = DiceGame(3, "Alice")
        self.assertEqual(diceGame.calcProbSecondTurn(3), 2/9)
        self.assertEqual(diceGame.calcProbSecondTurn(90), 89/8100)

    def test_calcProbability(self):
        diceGame = DiceGame(3, "Alice")
        self.assertEqual(diceGame.calcProbability(), 2/9)

    def test_types(self):
        diceGame = DiceGame("3", 1)
        self.assertRaises(TypeError, diceGame.calcProbFirstTurn, "3")
        self.assertRaises(TypeError, diceGame.calcProbFirstTurn, False)
        self.assertRaises(TypeError, diceGame.calcProbSecondTurn, [])
        self.assertRaises(TypeError, diceGame.calcProbSecondTurn, True)
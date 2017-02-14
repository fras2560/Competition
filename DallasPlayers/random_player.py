'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using a random strategy
'''
from DallasPlayers.player import Player, COOPERATE, DEFECT
import random
import unittest


class RandomPlayer(Player):
    """
    Random Player - just randomly picks one
    """
    def __init__(self):
        self.probing = False

    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Random Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        return random.randint(0, 1)


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = RandomPlayer()

    def testPlay(self):
        count = {DEFECT: 0, COOPERATE: 0}
        for __ in range(0, 100):
            move = self.player.play([], [], [])
            count[move] += 1
        self.assertEqual(count[DEFECT] < 65, True)
        self.assertEqual(count[DEFECT] > 35, True)
        self.assertEqual(count[COOPERATE] < 65, True)
        self.assertEqual(count[COOPERATE] > 35, True)

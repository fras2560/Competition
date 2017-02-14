'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using an adaptive strategy
'''
from DallasPlayers.player import COOPERATE, Player, DEFECT
import unittest
import random


class AdaptivePlayer(Player):
    """
    Adaptive Player - starts with a certain strategy then take
                        choice with best score
    """
    def __init__(self):
        self.moves = {0: COOPERATE,
                      1: COOPERATE,
                      2: COOPERATE,
                      3: COOPERATE,
                      4: COOPERATE,
                      5: DEFECT,
                      6: DEFECT,
                      7: DEFECT,
                      8: DEFECT,
                      9: DEFECT
                      }

    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Adaptive Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        x = len(myHistory)
        if x >= 0 and x < 10:
            move = self.moves[x]
        else:
            move = self.best_score(myHistory, oppHistory1, oppHistory2)
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = AdaptivePlayer()

    def testPlay(self):
        move = self.player.play([], [], [])
        myHistory = []
        e1 = []
        e2 = []
        for __ in range(0, 5):
            move = self.player.play(myHistory, e1, e1)
            self.assertEqual(move, COOPERATE)
            myHistory.append(move)
            e1.append(random.randint(0, 1))
            e2.append(random.randint(0, 1))
        for __ in range(0, 5):
            move = self.player.play(myHistory, e1, e1)
            self.assertEqual(move, DEFECT)
            myHistory.append(move)
            e1.append(random.randint(0, 1))
            e2.append(random.randint(0, 1))
        move = self.player.play(myHistory, e1, e2)
        self.assertEqual(move, self.player.best_score(myHistory, e1, e2))
        # make sure play is dependent on history
        myHistory = []
        e1 = []
        e2 = []
        for __ in range(0, 5):
            move = self.player.play(myHistory, e1, e1)
            self.assertEqual(move, COOPERATE)
            myHistory.append(move)
            e1.append(random.randint(0, 1))
            e2.append(random.randint(0, 1))
        for __ in range(0, 5):
            move = self.player.play(myHistory, e1, e1)
            self.assertEqual(move, DEFECT)
            myHistory.append(move)
            e1.append(random.randint(0, 1))
            e2.append(random.randint(0, 1))
        

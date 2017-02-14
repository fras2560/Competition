'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using a cooperative strategy
'''
from DallasPlayers.player import COOPERATE, Player, DEFECT
import unittest


class CooperatePlayer(Player):
    """
    Cooperate Player - just randomly picks one
    """
    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Cooperate Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        return COOPERATE


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = CooperatePlayer()

    def testPlay(self):
        move = self.player.play([], [], [])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE], [DEFECT], [COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE], [DEFECT], [DEFECT])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE], [COOPERATE], [COOPERATE])
        self.assertEqual(move, COOPERATE)

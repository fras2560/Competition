'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using a defector strategy
'''
from DallasPlayers.player import Player, DEFECT, COOPERATE
import unittest


class DefectPlayer(Player):
    """
    The DefectPlayer always defects (plays 1)
    """
    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Defect Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        return DEFECT


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = DefectPlayer()

    def testPlay(self):
        move = self.player.play([], [], [])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE], [DEFECT], [COOPERATE])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE], [DEFECT], [DEFECT])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE], [COOPERATE], [COOPERATE])
        self.assertEqual(move, DEFECT)

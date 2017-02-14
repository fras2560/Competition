'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using an suspicious strategy
'''
from DallasPlayers.player import COOPERATE, Player, DEFECT
import unittest


class SuspiciousPlayer(Player):
    """
    Suspicious Player - Tit For Tat except begins by defecting.
    """
    def __init__(self):
        self.cooperate = True
        self.times = 0

    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Suspicious Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        # are we cooperating
        if self.first_move(oppHistory1, oppHistory2):
            # WHO CAN YOU TRUST
            move = DEFECT
        else:
            # we are all in this together
            move = COOPERATE
            if oppHistory1[-1] == DEFECT or oppHistory2[-1] == DEFECT:
                # someone is being a bastard
                move = DEFECT
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = SuspiciousPlayer()

    def testPlay(self):
        move = self.player.play([], [], [])
        self.assertEqual(move, DEFECT)
        # test all second moves
        move = self.player.play([COOPERATE], [COOPERATE], [COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE], [COOPERATE], [DEFECT])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE], [DEFECT], [COOPERATE])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE], [DEFECT], [DEFECT])
        self.assertEqual(move, DEFECT)

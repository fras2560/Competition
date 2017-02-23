'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using a grudge strategy
'''
from DallasPlayers.player import COOPERATE, Player, DEFECT
import unittest


class GrudgerPlayer(Player):
    """
    Grudger Player - Co-operate until the opponent defects.
                     Then always defect unforgivingly.
    """
    def __init__(self):
        self.grudge = False

    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Grudger Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        if self.first_move(oppHistory1, oppHistory2):
            # first move so make sure to reset grudge variable
            self.grudge = False
        move = DEFECT
        if not self.grudge:
            move = COOPERATE
            if (not self.first_move(oppHistory1, oppHistory2) and
                    (oppHistory1[-1] == DEFECT or oppHistory2[-1] == DEFECT)):
                # need to hold a grudge now
                self.grudge = True
                move = DEFECT
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = GrudgerPlayer()

    def testPlay(self):
        for x in range(0, 5):
            move = self.player.play(x * [COOPERATE],
                                    x * [COOPERATE],
                                    x * [COOPERATE])
            self.assertEqual(move, COOPERATE)
            self.assertEqual(self.player.grudge, False)
        move = self.player.play([COOPERATE],
                                [COOPERATE],
                                [DEFECT])
        self.assertEqual(move, DEFECT)
        self.assertEqual(self.player.grudge, True)
        self.player = GrudgerPlayer()
        move = self.player.play([COOPERATE],
                                [DEFECT],
                                [COOPERATE])
        self.assertEqual(move, DEFECT)
        self.assertEqual(self.player.grudge, True)
        move = self.player.play([COOPERATE, COOPERATE],
                                [DEFECT, COOPERATE],
                                [COOPERATE, COOPERATE])
        self.assertEqual(move, DEFECT)
        self.assertEqual(self.player.grudge, True)
        # no need to restart player
        move = self.player.play([],
                                [],
                                [])
        self.assertEqual(move, COOPERATE)
        self.assertEqual(self.player.grudge, False)

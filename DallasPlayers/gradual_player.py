'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using an gradual strategy
'''
from DallasPlayers.player import COOPERATE, Player, DEFECT
import unittest


class GradualPlayer(Player):
    """
    Gradual Player - Co-operates until the opponent defects,
                    in such case defects the total number of times
                    the opponent has defected during the game.
                    Followed up by two co-operations.
    """
    def __init__(self):
        self.cooperate = True
        self.times = 0

    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Gradual Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        # are we cooperating
        if self.first_move(oppHistory1, oppHistory2):
            # first move baby
            move = COOPERATE
            self.cooperate = True
            self.times = 0
        elif self.cooperate:
            # has anyone defected ?
            move = COOPERATE
            if oppHistory1[-1] == DEFECT:
                move = DEFECT
                self.cooperate = False
                self.times = oppHistory1.count(DEFECT)
            elif oppHistory2[-1] == DEFECT:
                move = DEFECT
                self.cooperate = False
                self.times = oppHistory2.count(DEFECT)
        else:
            # DEFECT as many times as that person has
            move = DEFECT
            if self.times <= 0:
                # DEFECT enough now time to work together
                move = COOPERATE
            if self.times <= -1:
                # back into cooperating mode
                self.cooperate = True
                self.times = 0
            self.times -= 1
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = GradualPlayer()

    def testPlay(self):
        for x in range(0, 5):
            move = self.player.play(x * [COOPERATE],
                                    x * [COOPERATE],
                                    x * [COOPERATE])
            self.assertEqual(move, COOPERATE)
            self.assertEqual(self.player.cooperate, True)
        # what happens when someone cheats
        move = self.player.play([COOPERATE],
                                [DEFECT],
                                [COOPERATE])
        self.assertEqual(move, DEFECT)
        self.assertEqual(self.player.cooperate, False)
        self.player = GradualPlayer()
        move = self.player.play([COOPERATE],
                                [COOPERATE],
                                [DEFECT])
        self.assertEqual(move, DEFECT)
        self.assertEqual(self.player.cooperate, False)
        # test out the gradual return to COOPERATING
        move = self.player.play([COOPERATE],
                                [COOPERATE],
                                [DEFECT])
        self.assertEqual(move, DEFECT)
        self.assertEqual(self.player.cooperate, False)
        move = self.player.play([COOPERATE],
                                [COOPERATE],
                                [DEFECT])
        self.assertEqual(move, COOPERATE)
        self.assertEqual(self.player.cooperate, False)
        move = self.player.play([COOPERATE],
                                [COOPERATE],
                                [DEFECT])
        self.assertEqual(move, COOPERATE)
        self.assertEqual(self.player.cooperate, True)

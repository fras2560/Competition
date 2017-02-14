'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using naive prober strategy
'''
from DallasPlayers.player import Player, DEFECT, COOPERATE
import random
import unittest


class NaiveProberPlayer(Player):
    """
    Naive Prober - Tit for Tat but probe by defecting in lieu of co-operating
    """
    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Naive Prober Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        move = DEFECT
        if self.first_move(oppHistory1, oppHistory2):
            move = COOPERATE
        elif oppHistory1[-1] == COOPERATE and oppHistory2[-1] == COOPERATE:
            # repeat opponent last choice if both choose corporation
            move = COOPERATE
            if random.random() < self.JUMP:
                # randomly defect
                move = DEFECT
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = NaiveProberPlayer()

    def testPlay(self):
        move = self.player.play([], [], [])
        self.assertEqual(move, COOPERATE)
        for x in range(1, 5):
            move = self.player.play(x * [COOPERATE],
                                    x * [DEFECT],
                                    x * [COOPERATE])
            self.assertEqual(move, DEFECT)
        for x in range(1, 5):
            move = self.player.play(x * [COOPERATE],
                                    x * [COOPERATE],
                                    x * [DEFECT])
            self.assertEqual(move, DEFECT)
        # test random defects
        count = 0
        for x in range(1, 100):
            move = self.player.play(x * [COOPERATE],
                                    x * [COOPERATE],
                                    x * [COOPERATE])
            if move == DEFECT:
                count += 1
        self.assertEqual(count <= (self.player.JUMP * 100) + 10, True)
        self.assertEqual(count > 0, True)

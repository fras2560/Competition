'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using naive peace maker strategy
'''
from DallasPlayers.player import Player, DEFECT, COOPERATE
import random
import unittest


class NaivePeaceMakerPlayer(Player):
    """
    Naive Peace Maker - Tit For Tat with Random Co-operation
    """
    def __init__(self):
        pass

    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Naive Peace Maker"

    def play(self, myHistory, oppHistory1, oppHistory2):
        move = DEFECT
        if self.first_move(oppHistory1, oppHistory2):
            # first move so cooperate
            move = COOPERATE
        elif oppHistory1[-1] == COOPERATE and oppHistory2[-1] == COOPERATE:
            # repeat opponent last choice if both choose corporation
            move = COOPERATE
        if move == DEFECT and random.random() < self.JUMP:
            # sometime try to make peace
            move = COOPERATE
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = NaivePeaceMakerPlayer()

    def testPlay(self):
        for x in range(0, 5):
            move = self.player.play(x * [COOPERATE],
                                    x * [COOPERATE],
                                    x * [COOPERATE])
            self.assertEqual(move, COOPERATE)
        # see how many times it jumps back
        count = 0
        for x in range(0, 100):
            move = self.player.play([COOPERATE], [DEFECT], [COOPERATE])
            if move == COOPERATE:
                count += 1
        # should less than the average jump factor, greater than zero
        self.assertEqual(count <= (self.player.JUMP * 100) + 10, True)
        self.assertEqual(count > 0, True)
        # see how many times it jumps back
        count = 0
        for x in range(0, 100):
            move = self.player.play([COOPERATE], [COOPERATE], [DEFECT])
            if move == COOPERATE:
                count += 1
        # should less than the average jump factor, greater than zero
        self.assertEqual(count <= (self.player.JUMP * 100) + 10, True)
        self.assertEqual(count > 0, True)
        # make sure player gives back what is given
        move = self.player.play([COOPERATE, COOPERATE],
                                [COOPERATE, COOPERATE],
                                [DEFECT, COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE, COOPERATE],
                                [DEFECT, COOPERATE],
                                [COOPERATE, COOPERATE])
        self.assertEqual(move, COOPERATE)

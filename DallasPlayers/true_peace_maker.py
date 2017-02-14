'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using true peace maker strategy
'''
from DallasPlayers.player import Player, DEFECT, COOPERATE
import random
import unittest


class TruePeaceMakerPlayer(Player):
    """
    True Peace Maker - (hybrid of Tit For Tat and
                        Tit For Two Tats with Random Co-operation)
    """
    def __init__(self):
        self.probing = False

    def studentID(self):
        return "20652186"

    def agentName(self):
        return "True Peace Maker Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        move = COOPERATE
        cheater = [DEFECT, DEFECT]
        if len(oppHistory1) > 1 and len(oppHistory2) > 1:
            if oppHistory1[-2:] == cheater or oppHistory2[-2:] == cheater:
                # one is a clear dishonest person
                move = DEFECT
                if random.random() < self.JUMP:
                    # try to make peace at times
                    move = COOPERATE
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = TruePeaceMakerPlayer()

    def testPlay(self):
        move = self.player.play([], [], [])
        self.assertEqual(move, COOPERATE)
        # just try the randomness factor
        count = 0
        expect = DEFECT
        for __ in range(0, 100):
            move = self.player.play([COOPERATE, COOPERATE],
                                    [COOPERATE, COOPERATE],
                                    [DEFECT, DEFECT])
            if move != expect:
                count += 1
        self.assertEqual(count <= (self.player.JUMP * 100) + 15, True)
        self.assertEqual(count > 0, True)

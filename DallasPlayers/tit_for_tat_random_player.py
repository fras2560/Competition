'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using tit for tat with some random element
'''
from DallasPlayers.player import Player, COOPERATE, DEFECT
import random
import unittest


class TitForTatRandomPlayer(Player):
    """
    Tit for Tat player - repeat two opponent's last choice
    (cheat if one cheats), jumps decision randomly
    """
    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Random Tit for Tat Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        move = DEFECT
        if self.first_move(oppHistory1, oppHistory2):
            move = COOPERATE
        elif oppHistory1[-1] == COOPERATE and oppHistory2[-1] == COOPERATE:
            # repeat opponent last choice if both choose corporation
            move = COOPERATE
        if random.random() < self.JUMP:
            # if above below a threshold then jump to another answer
            move = (move + 1) % 2
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = TitForTatRandomPlayer()

    def testPlay(self):
        move = self.player.play([], [], [])
        self.assertEqual(move, COOPERATE)
        # test all second moves and its randomness
        expect = COOPERATE
        count = 0
        for __ in range(0, 100):
            move = self.player.play([COOPERATE], [COOPERATE], [COOPERATE])
            if move != expect:
                count += 1
        self.assertEqual(count < (self.player.JUMP * 100) + 15, True)
        self.assertEqual(count > 0, True)

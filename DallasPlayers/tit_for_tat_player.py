'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using tit for tat
'''
from DallasPlayers.player import Player, DEFECT, COOPERATE
import unittest


class TitForTatPlayer(Player):
    """
    Tit for Tat player - repeat two opponent's last choice
    (cheat if one cheats)
    """
    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Tit for Tat Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        move = DEFECT
        if self.first_move(oppHistory1, oppHistory2):
            move = COOPERATE
        elif oppHistory1[-1] == COOPERATE and oppHistory2[-1] == COOPERATE:
            # repeat opponent last choice if both choose corporation
            move = COOPERATE
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = TitForTatPlayer()

    def testPlay(self):
        move = self.player.play([], [], [])
        self.assertEqual(move, COOPERATE)
        # test all second moves
        move = self.player.play([COOPERATE], [COOPERATE], [COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE], [COOPERATE], [DEFECT])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE], [DEFECT], [COOPERATE])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE], [DEFECT], [DEFECT])
        self.assertEqual(move, DEFECT)

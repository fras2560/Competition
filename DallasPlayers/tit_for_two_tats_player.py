'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using tit for two tats
'''
from DallasPlayers.player import Player, DEFECT, COOPERATE
import unittest


class TitForTwoTatsPlayer(Player):
    """
    Tit for two Tats player - repeat two opponent's last choice
    (cheat if one cheats)
    """
    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Tit for Two Tats Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        move = DEFECT
        if not self.first_move(oppHistory1, oppHistory2):
            if len(oppHistory1) > 1 and len(oppHistory2) > 1:
                cheater = [DEFECT, DEFECT]
                move = COOPERATE
                if (oppHistory1[-2:] == cheater or
                        oppHistory2[-2:] == cheater):
                    move = DEFECT
            else:
                if (oppHistory1[-1] == COOPERATE and
                        oppHistory2[-1] == COOPERATE):
                    # repeat opponent last choice if both choose corporation
                    move = COOPERATE
        else:
            move = COOPERATE
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = TitForTwoTatsPlayer()

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
        # test all third moves
        move = self.player.play([COOPERATE, COOPERATE],
                                [COOPERATE, COOPERATE],
                                [COOPERATE, COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE, COOPERATE],
                                [DEFECT, COOPERATE],
                                [COOPERATE, COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE, COOPERATE],
                                [COOPERATE, DEFECT],
                                [COOPERATE, COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE, COOPERATE],
                                [COOPERATE, COOPERATE],
                                [DEFECT, COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE, COOPERATE],
                                [COOPERATE, COOPERATE],
                                [COOPERATE, DEFECT])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE, COOPERATE],
                                [DEFECT, DEFECT],
                                [COOPERATE, COOPERATE])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE, COOPERATE],
                                [DEFECT, COOPERATE],
                                [DEFECT, COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE, COOPERATE],
                                [DEFECT, COOPERATE],
                                [COOPERATE, DEFECT])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE, COOPERATE],
                                [COOPERATE, DEFECT],
                                [DEFECT, COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE, COOPERATE],
                                [COOPERATE, DEFECT],
                                [COOPERATE, DEFECT])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE, COOPERATE],
                                [COOPERATE, COOPERATE],
                                [DEFECT, DEFECT])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE, COOPERATE],
                                [COOPERATE, DEFECT],
                                [DEFECT, DEFECT])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE, COOPERATE],
                                [DEFECT, COOPERATE],
                                [DEFECT, DEFECT])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE, COOPERATE],
                                [DEFECT, DEFECT],
                                [COOPERATE, DEFECT])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE, COOPERATE],
                                [DEFECT, DEFECT],
                                [DEFECT, COOPERATE])
        self.assertEqual(move, DEFECT)
        move = self.player.play([COOPERATE, COOPERATE],
                                [DEFECT, DEFECT],
                                [DEFECT, DEFECT])
        self.assertEqual(move, DEFECT)

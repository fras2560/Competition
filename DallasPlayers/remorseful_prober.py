'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using remorseful prober strategy
'''
from DallasPlayers.player import Player, DEFECT, COOPERATE
import random
import unittest


class RemorsefulProberPlayer(Player):
    """
    Remorseful Prober - Tit for Tat but probe
                        by defecting in lieu of co-operating but be
                        remorseful if they defect in response
    """
    def __init__(self):
        self.probing = False

    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Remorseful Prober"

    def play(self, myHistory, oppHistory1, oppHistory2):
        move = DEFECT
        if self.first_move(oppHistory1, oppHistory2):
            move = COOPERATE
            self.probing = False
        elif (not self.probing and oppHistory1[-1] == COOPERATE and
                oppHistory2[-1] == COOPERATE):
            # repeat opponent last choice if both choose corporation
            move = COOPERATE
            if random.random() < self.JUMP:
                # randomly defect and try probing
                move = DEFECT
                self.probing = True
        elif (self.probing and
              oppHistory1[-1] == DEFECT or
              oppHistory2[-1] == DEFECT):
            # if was probing but one responded by defecting then be remorseful
            move = COOPERATE
            self.probing = False
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = RemorsefulProberPlayer()

    def testPlay(self):
        # test first move
        move = self.player.play([], [], [])
        self.assertEqual(move, COOPERATE)
        done = False
        # COOPERATE UNTIL TRY PROBING
        while not done:
            move = self.player.play([COOPERATE], [COOPERATE], [COOPERATE])
            if self.player.probing:
                done = True
                self.assertEqual(move, DEFECT)
            else:
                self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE], [COOPERATE], [COOPERATE])
        self.assertEqual(move, DEFECT)
        self.assertEqual(self.player.probing, True)
        move = self.player.play([COOPERATE], [DEFECT], [COOPERATE])
        self.assertEqual(move, COOPERATE)
        self.assertEqual(self.player.probing, False)

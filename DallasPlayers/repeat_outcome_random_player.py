'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using a repeat (Pavlov) strategy with some randomness
'''
from DallasPlayers.player import COOPERATE, Player, DEFECT
import random
import unittest


class RepeatOutcomeRandomPlayer(Player):
    """
    Repeat Outcome Random Player - repeat last choice if good outcome
                                    but sometimes makes a random choice
    """
    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Repeat Outcome Random Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        if self.first_move(oppHistory1, oppHistory2):
            # start off cooperating
            move = COOPERATE
        else:
            score = self.last_score(myHistory, oppHistory1, oppHistory2)
            if score >= self.ACCEPTABLE:
                # getting a result we like
                move = myHistory[-1]
            else:
                # change move, try another approach
                move = (myHistory[-1] + 1) % 2
            if random.random() < self.JUMP:
                # make a random move sometimes
                move = (move + 1) % 2
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = RepeatOutcomeRandomPlayer()

    def testPlay(self):
        # test first move
        move = self.player.play([], [], [])
        self.assertEqual(move, COOPERATE)
        # need to test for the randomness
        count = 0
        # test all possible second moves when cooperating
        expect = COOPERATE
        for __ in range(0, 80):
            move = self.player.play([COOPERATE], [COOPERATE], [COOPERATE])
            if move != expect:
                count += 1
        expect = COOPERATE
        for __ in range(0, 80):
            move = self.player.play([COOPERATE], [DEFECT], [COOPERATE])
            if move != expect:
                count += 1
        expect = COOPERATE
        for __ in range(0, 80):
            move = self.player.play([COOPERATE], [COOPERATE], [DEFECT])
            if move != expect:
                count += 1
        expect = DEFECT
        for __ in range(0, 80):
            move = self.player.play([COOPERATE], [DEFECT], [DEFECT])
            if move != expect:
                count += 1
        # test all possible second moves when defecting
        expect = DEFECT
        for __ in range(0, 80):
            move = self.player.play([DEFECT], [COOPERATE], [COOPERATE])
            if move != expect:
                count += 1
        expect = DEFECT
        for __ in range(0, 80):
            move = self.player.play([DEFECT], [DEFECT], [COOPERATE])
            if move != expect:
                count += 1
        expect = DEFECT
        for __ in range(0, 80):
            move = self.player.play([DEFECT], [COOPERATE], [DEFECT])
            if move != expect:
                count += 1
        expect = COOPERATE
        for __ in range(0, 80):
            move = self.player.play([DEFECT], [DEFECT], [DEFECT])
            if move != expect:
                count += 1
        self.assertEqual(count <= (self.player.JUMP * 80 * 8) + 20, True)
        self.assertEqual(count > 0, True)

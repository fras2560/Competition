'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using a repeat (Pavlov) strategy
'''
from DallasPlayers.player import COOPERATE, Player, DEFECT
import unittest


class RepeatOutcomePlayer(Player):
    """
    Repeat Outcome Player - repeat last choice if good outcome
    """
    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Repeat Outcome Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        if self.first_move(oppHistory1, oppHistory2):
            # start off cooperating
            move = COOPERATE
        else:
            # calculate score
            score = self.last_score(myHistory, oppHistory1, oppHistory2)
            if score >= self.ACCEPTABLE:
                # getting a result we like
                move = myHistory[-1]
            else:
                # change move, try another approach
                move = (myHistory[-1] + 1) % 2
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = RepeatOutcomePlayer()

    def testPlay(self):
        # test first move
        move = self.player.play([], [], [])
        self.assertEqual(move, COOPERATE)
        # test all possible second moves when cooperating
        move = self.player.play([COOPERATE], [COOPERATE], [COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE], [DEFECT], [COOPERATE])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE], [COOPERATE], [DEFECT])
        self.assertEqual(move, COOPERATE)
        move = self.player.play([COOPERATE], [DEFECT], [DEFECT])
        self.assertEqual(move, DEFECT)
        # try all possible second moves when defecting
        move = self.player.play([DEFECT], [COOPERATE], [COOPERATE])
        self.assertEqual(move, DEFECT)
        move = self.player.play([DEFECT], [DEFECT], [COOPERATE])
        self.assertEqual(move, DEFECT)
        move = self.player.play([DEFECT], [COOPERATE], [DEFECT])
        self.assertEqual(move, DEFECT)
        move = self.player.play([DEFECT], [DEFECT], [DEFECT])
        self.assertEqual(move, COOPERATE)

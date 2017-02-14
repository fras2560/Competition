'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using an soft grudge strategy
'''
from DallasPlayers.player import COOPERATE, Player, DEFECT
import unittest


class SoftGrudgerPlayer(Player):
    """
    Soft Grudger Player - Co-operates until the opponent defects,
                            in such case opponent is punished with d,d,d,d,c,c.
    """
    def __init__(self):
        self.grudge = False
        self.moves = []

    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Soft Grudge Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        # are we cooperating
        if self.first_move(oppHistory1, oppHistory2):
            self.grudge = False
            self.moves = []
            move = COOPERATE
        else:
            if not self.grudge:
                # lets work together
                move = COOPERATE
                if oppHistory1[-1] == DEFECT or oppHistory2[-1] == DEFECT:
                    # someone has betrayed us, now have a grudge
                    move = DEFECT
                    self.grudge = True
                    self.moves = 2 * [COOPERATE] + 3 * [DEFECT]
            else:
                # still have a grudge
                move = self.moves.pop()
                if len(self.moves) == 0:
                    # can move on now, no more grudge
                    self.grudge = False
        return move


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = SoftGrudgerPlayer()

    def testPlay(self):
        for x in range(0, 5):
            # no grudge everyone gets along
            move = self.player.play(x * [COOPERATE],
                                    x * [COOPERATE],
                                    x * [COOPERATE])
            self.assertEqual(move, COOPERATE)
            self.assertEqual(self.player.grudge, False)
        # now test the grudge
        moves = 2 * [COOPERATE] + 3 * [DEFECT]
        # HERE COMES THE GRUDGE
        move = self.player.play([COOPERATE], [DEFECT], [COOPERATE])
        self.assertEqual(move, DEFECT)
        self.assertEqual(self.player.grudge, True)
        # grudge it out
        while len(moves) > 0:
            move = self.player.play([COOPERATE], [DEFECT], [COOPERATE])
            self.assertEqual(move, moves.pop())
        # grudge should be gone
        self.assertEqual(self.player.grudge, False)
        # now back to life being good
        for x in range(0, 5):
            # no grudge everyone gets along
            move = self.player.play(x * [COOPERATE],
                                    x * [COOPERATE],
                                    x * [COOPERATE])
            self.assertEqual(move, COOPERATE)
            self.assertEqual(self.player.grudge, False)

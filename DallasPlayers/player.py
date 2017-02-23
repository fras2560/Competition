'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains base class for players
'''
import unittest
PAYOFF = [[[6, 3], [3, 0]], [[8, 5], [5, 2]]]
DEFECT = 1
COOPERATE = 0


class Player(object):
    """
    This defines an interface for a player of the 3-player.
    Inherit and modify this class by declaring the following:
    class SecretStrategyPlayer(Player)
        # code goes here
        # make sure you implement the play(...) function
    Attributes:
    While you are not prohibited from adding attributes.  You should not need
    to implement do so.  The parameters to play(...) contain all information
    available about the current state of play.
    """
    JUMP = 0.2
    ACCEPTABLE = 3

    GOD = 'Dallas'

    def studentID(self):
        """ Returns the creator's numeric studentID """
        raise NotImplementedError("studentID not implemented")

    def agentName(self):
        """ Returns a creative name for the agent """
        return self.__class__.__name__

    def first_move(self, oppHistory1, oppHistory2):
        """ Returns True if first move, False otherwise
        """
        return (len(oppHistory1) == 0 and len(oppHistory2) == 0)

    def last_score(self, myHistory, oppHistory1, oppHistory2):
        """ Returns the score of the last play
        """
        pay = 0
        if not self.first_move(oppHistory1, oppHistory2):
            pay = PAYOFF[myHistory[-1]][oppHistory1[-1]][oppHistory2[-1]]
        return pay

    def best_score(self, myHistory, oppHistory1, oppHistory2):
        assert len(myHistory) == len(oppHistory1) == len(oppHistory2)
        result = COOPERATE
        if not self.first_move(oppHistory1, oppHistory2):
            scores = {DEFECT: 0, COOPERATE: 0}
            times = {DEFECT: 0, COOPERATE: 0}
            for i in range(0, len(myHistory)):
                a1 = myHistory[i]
                a2 = oppHistory1[i]
                a3 = oppHistory2[i]
                scores[a1] += PAYOFF[a1][a2][a3]
                times[a1] += 1
            result = COOPERATE
            if times[DEFECT] > 0 and times[COOPERATE] > 0:
                if (scores[DEFECT] / times[DEFECT] and
                        scores[COOPERATE] / times[COOPERATE]):
                    result = DEFECT
        return result

    def play(self, myHistory, oppHistory1, oppHistory2):
        """
        Given a history of play, computes and returns your next move
        ( 0 = cooperate; 1 = defect )
        myHistory = list of int representing your past plays
        oppHisotry1 = list of int representing opponent 1's past plays
        oppHisotry2 = list of int representing opponent 2's past plays
        NB: use len(myHistory) to find the number of games played
        """
        raise NotImplementedError("play not implemented")


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def testFirstMove(self):
        move = self.player.first_move([], [])
        self.assertEqual(move, True)
        move = self.player.first_move([DEFECT], [DEFECT])
        self.assertEqual(move, False)

    def testLastScore(self):
        score = self.player.last_score([], [], [])
        self.assertEqual(score, 0)
        score = self.player.last_score([DEFECT], [COOPERATE], [COOPERATE])
        self.assertEqual(score, 8)
        score = self.player.last_score([DEFECT], [DEFECT], [COOPERATE])
        self.assertEqual(score, 5)
        score = self.player.last_score([DEFECT], [COOPERATE], [DEFECT])
        self.assertEqual(score, 5)
        score = self.player.last_score([DEFECT], [DEFECT], [DEFECT])
        self.assertEqual(score, 2)
        score = self.player.last_score([COOPERATE], [COOPERATE], [COOPERATE])
        self.assertEqual(score, 6)
        score = self.player.last_score([COOPERATE], [DEFECT], [COOPERATE])
        self.assertEqual(score, 3)
        score = self.player.last_score([COOPERATE], [DEFECT], [COOPERATE])
        self.assertEqual(score, 3)
        score = self.player.last_score([COOPERATE], [DEFECT], [DEFECT])
        self.assertEqual(score, 0)

    def testBestScore(self):
        score = self.player.best_score([], [], [])
        self.assertEqual(score, COOPERATE)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [COOPERATE, COOPERATE],
                                       [COOPERATE, COOPERATE])
        self.assertEqual(score, DEFECT)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [DEFECT, COOPERATE],
                                       [COOPERATE, COOPERATE])
        self.assertEqual(score, DEFECT)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [COOPERATE, DEFECT],
                                       [COOPERATE, COOPERATE])
        self.assertEqual(score, COOPERATE)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [COOPERATE, COOPERATE],
                                       [DEFECT, COOPERATE])
        self.assertEqual(score, DEFECT)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [COOPERATE, COOPERATE],
                                       [COOPERATE, DEFECT])
        self.assertEqual(score, COOPERATE)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [DEFECT, DEFECT],
                                       [COOPERATE, COOPERATE])
        self.assertEqual(score, DEFECT)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [DEFECT, COOPERATE],
                                       [DEFECT, COOPERATE])
        self.assertEqual(score, DEFECT)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [DEFECT, COOPERATE],
                                       [COOPERATE, DEFECT])
        self.assertEqual(score, DEFECT)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [COOPERATE, DEFECT],
                                       [DEFECT, COOPERATE])
        self.assertEqual(score, DEFECT)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [COOPERATE, DEFECT],
                                       [COOPERATE, DEFECT])
        self.assertEqual(score, COOPERATE)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [COOPERATE, DEFECT],
                                       [DEFECT, DEFECT])
        self.assertEqual(score, COOPERATE)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [DEFECT, COOPERATE],
                                       [DEFECT, DEFECT])
        self.assertEqual(score, DEFECT)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [DEFECT, DEFECT],
                                       [COOPERATE, DEFECT])
        self.assertEqual(score, COOPERATE)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [DEFECT, DEFECT],
                                       [DEFECT, COOPERATE])
        self.assertEqual(score, DEFECT)
        score = self.player.best_score([COOPERATE, DEFECT],
                                       [DEFECT, DEFECT],
                                       [DEFECT, DEFECT])

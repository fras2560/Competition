'''
This Python module models the three-player Prisoner's Dilemma game.
We use the integer "0" to represent cooperation, and "1" to represent 
defection. 

Recall that in the 2-players dilemma, U(DC) > U(CC) > U(DD) > U(CD), where
we give the payoff for the first player in the list. We want the three-player game 
to resemble the 2-player game whenever one player's response is fixed, and we
also want symmetry, so U(CCD) = U(CDC) etc. This gives the unique ordering

U(DCC) > U(CCC) > U(DDC) > U(CDC) > U(DDD) > U(CDD)

The payoffs for player 1 are given by the following matrix:

@author: akhtsang
Created on Feb 9, 2017
'''

import random
import math
from DallasPlayers.grudger_player import GrudgerPlayer
from DallasPlayers.tit_for_tat_player import TitForTatPlayer
from DallasPlayers.defect_player import DefectPlayer
from random import randint
from numpy import number
from __builtin__ import True
PHONEBOOK = {}
CLASSSIZE = 145
PAYOFF = [[[6, 3], [3, 0]], [[8, 5], [5, 2]]]
NROUNDS = 100

"""
So payoff[i][j][k] represents the payoff to player 1 when the first
player's action is i, the second player's action is j, and the
third player's action is k.

In this simulation, triples of players will play each other repeatedly in a
'match'. A match consists of about 100 rounds, and your score from that match
is the average of the payoffs from each round of that match. For each round,
your strategy is given a list of the previous plays (so you can remember what
your opponent did) and must compute the next action.
 """


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

    def studentID(self):
        """ Returns the creator's numeric studentID """
        raise NotImplementedError("studentID not implemented")

    def agentName(self):
        """ Returns a creative name for the agent """
        return self.__class__.__name__

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


class NicePlayer(Player):
    """
    The nicePlayer always cooperates (plays 0)
    """
    def studentID(self):
        return "42"

    def agentName(self):
        return "Nice Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        return 0


class MeanPlayer(Player):
    """
    The nicePlayer always defects (plays 1)
    """
    def studentID(self):
        return "42"

    def agentName(self):
        return "Mean Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        return 1


class RandomPlayer(Player):
    """
    The nicePlayer always defects (plays 1)
    """
    def studentID(self):
        return "42"

    def agentName(self):
        return "Mean Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        return random.randint(0, 1)


def playRound(player1, player2, player3, history1, history2, history3):
    """
    Computes one round of play between 3 players (give players and their
    histories.  Returns a list containing their actions.
    """
    a1 = player1.play(history1, history2, history3)
    a2 = player2.play(history2, history3, history1)
    a3 = player3.play(history3, history1, history2)
    return [a1, a2, a3]


def scoreRound(action1, action2, action3):
    """
    Given actions for three players, returns a list containing their
    respective scores
    """
    s1 = PAYOFF[action1][action2][action3]
    s2 = PAYOFF[action2][action3][action1]
    s3 = PAYOFF[action3][action1][action2]
    return [s1, s2, s3]


def scoreGame(player1, player2, player3, nRounds):
    """
    Given three players, allow them to play the iterated game for nRounds
    number of rounds.  Return their scores.
    """
    history1 = []
    history2 = []
    history3 = []
    score1 = 0
    score2 = 0
    score3 = 0
    for __ in range(nRounds):
        [a1, a2, a3] = playRound(player1,
                                 player2,
                                 player3,
                                 history1,
                                 history2,
                                 history3)
        history1.append(a1)
        history2.append(a2)
        history3.append(a3)
        [s1, s2, s3] = scoreRound(a1, a2, a3)
        score1 += s1
        score2 += s2
        score3 += s3
    return [score1, score2, score3]


def init_phonebook(grudgers):
    global PHONEBOOK
    PHONEBOOK = {}
    for i in range(0, grudgers):
        PHONEBOOK[i] = GrudgerPlayer
    for j in range(grudgers, CLASSSIZE):
        PHONEBOOK[j] = DefectPlayer


def getPlayer(i):
    """ This function organizes all participating players in a 0+ natural number
    index, and returns an instance of a given player given an index
    """
    if i < 0 or i >= len(PHONEBOOK):
        raise IndexError("getPlayer() index out of bounds")
        # return RandomPlayer()
    return PHONEBOOK[i]()


def scheduleGamesForPlayer(nPlayers, pIndex):
    """ Given the total number of players (nPlayers), and the index of the current
    player (pIndex), returns a list of games scheduled against the player such
    that pIndex will play against each player (including herself) at least
    once, at most twice, in the least number of games possible, with no game
    containing two opponents of the same type.  These games occur in
    randomized order (and opponent pairs are also randomized).
    Games are returned as a 2D list of player indices,
        result = scheduleGamesForPlayer(...)
    result[0] is the first game to be played
    result[0][0] is always pIndex
    result[0][1] and result[0][2] are the opponents
    Example usage:
    > scheduleGamesForPlayer(10, 1)
    produces 5 games as follows:
    > [[1, 0, 4], [1, 5, 9], [1, 3, 7], [1, 8, 2], [1, 1, 6]]
    """
    playerList = [i for i in range(nPlayers)]
    random.shuffle(playerList)
    nBasicGames = int(math.floor(nPlayers / 2))
    schedule = []
    for i in range(nBasicGames):
        schedule.append([pIndex, playerList[i*2], playerList[i*2+1]])
    # If number of players is odd, we schedule one extra game with the
    # remaining opponent and a randomly selected player.  The additional
    # opponent cannot be the same as this last outstanding opponent.
    if nPlayers % 2 == 1:
        r = random.randint(0, nPlayers-2)
        if r == playerList[-1]:
            r += 1
        schedule.append([pIndex, playerList[-1], r])
    return schedule


def runTournament(nPlayers):
    """
    Runs a tournament for the specified number of players, returning a list
    containing their average performance for their ceil(nPlayers/2) games.
    NB: nPlayers should correspond to the number of players specified in the
    getPlayers(...) function
    """
    tournamentResults = []
    for p in range(nPlayers):
        schedule = scheduleGamesForPlayer(nPlayers, p)
        pTally = 0
        pGames = 0
        for s in schedule:
            [s1, s2, s3] = scoreGame(getPlayer(s[0]),
                                     getPlayer(s[1]),
                                     getPlayer(s[2]),
                                     NROUNDS)
            pTally += s1
            pGames += 1
        tournamentResults.append((getPlayer(p).agentName(), pTally / pGames))
    return tournamentResults


def checkTournament(tournament):
    groups = {}
    for agent in sorted(tournament, key=lambda tup: tup[1], reverse=True):
        score = agent[1]
        name = agent[0]
        if score not in groups.keys():
            groups[score] = []
        groups[score].append(name)
    print(groups)
    pos = 0
    sorted_scores = sorted(groups, reverse=True)
    # check to see where all grudger are better than defects
    defect_found = False
    better = True
    while better and pos < len(sorted_scores):
        if DefectPlayer().agentName() in groups[sorted_scores[pos]]:
            defect_found = True
        if defect_found:
            if GrudgerPlayer().agentName() in groups[sorted_scores[pos]]:
                better = False
        pos += 1
    return better


def tipping_point():
    number_of_grudgers = 1
    init_phonebook(number_of_grudgers)
    while not checkTournament(runTournament(CLASSSIZE)):
        print(number_of_grudgers)
        number_of_grudgers += 1
        init_phonebook(number_of_grudgers)
    print("The tipping point is {}".format(number_of_grudgers))

if __name__ == "__main__":
    tipping_point()

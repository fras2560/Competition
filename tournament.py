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
from DallasPlayers import PLAYERS as DALLASPLAYERS
from TomPlayers import PLAYERS as TOMPLAYERS
from GeorgePlayers import PLAYERS as GEORGEPLAYERS

import random
import math
from collections import defaultdict

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


def getPlayer(i):
    """ This function organizes all participating players in a 0+ natural number
    index, and returns an instance of a given player given an index
    """
    phoneBook = {
        0: DALLASPLAYERS[0],
        1: DALLASPLAYERS[1],
        2: DALLASPLAYERS[2],
        3: TOMPLAYERS[0],
        4: TOMPLAYERS[1],
        5: TOMPLAYERS[2],
        6: GEORGEPLAYERS[0],
        7: GEORGEPLAYERS[1],
        8: GEORGEPLAYERS[2],
    }
    if i < 0 or i >= len(phoneBook):
        raise IndexError("getPlayer() index out of bounds")
        # return RandomPlayer()
    return phoneBook[i]()


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
    god_scores = defaultdict(list)
    agent_scores = defaultdict(list)
    for p in range(nPlayers):
        schedule = scheduleGamesForPlayer(nPlayers, p)
        pTally = 0
        pGames = 0
        for s in schedule:
            p1 = getPlayer(s[0])
            p2 = getPlayer(s[1])
            p3 = getPlayer(s[2])
            [s1, s2, s3] = scoreGame(p1, p2, p3, NROUNDS)
            for player, score in [(p1,s1), (p2,s2), (p3,s3)]:
                god_scores[player.GOD].append(score)
                agentname = player.GOD + ' ' + player.agentName()
                agent_scores[agentname].append(score)

            pTally += s1
            pGames += 1
        tournamentResults.append(pTally / pGames)
    return tournamentResults, dict(god_scores), dict(agent_scores)

# print(scheduleGamesForPlayer(3, 0))
def mergescores(score_dict1, score_dict2):
    """ Merges two score dictionaries by concatenating score lists at key """
    sd1 = dict(**score_dict1) # copy dict
    for k, scores in score_dict2.items():
        if k not in sd1: sd1[k] = scores
        else: sd1[k] += scores
    return sd1

def print_scores(score_dict):
    def average(arr):
        return sum(arr) / len(arr)

    fld = max(map(len, score_dict.keys())) + 1
    for key, scores in sorted(score_dict.items(), key=lambda x: average(x[1]), reverse=True):
        print("{name:>{fieldw}}: {avg:.1f} (games={count})".format(
            fieldw=fld, name=key, avg=average(scores), count=len(scores)
        ))

gods = {}
agents = {}
for i in range(100):
    tourn, god_scores, agent_scores = runTournament(3*3)
    gods = mergescores(gods, god_scores)
    agents = mergescores(agents, agent_scores)

print_scores(gods)
print()
print_scores(agents)

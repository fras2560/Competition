'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using tit for two tats and jumping randomly at times
'''
from DallasPlayers.player import Player, DEFECT, COOPERATE
import random


class TitForTwoTatsRandomPlayer(Player):
    """
    Tit for two Tats player - repeat two opponent's last choice
    (cheat if one cheats), jump randomly at times
    """
    def studentID(self):
        return "20652186"

    def agentName(self):
        return "Random Tit for Two Tats Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        move = DEFECT
        if len(oppHistory1) > 1 and len(oppHistory2) > 1:
            correct = [COOPERATE, COOPERATE]
            if (oppHistory1[-2:] == correct and oppHistory2[-2:] == correct):
                move = COOPERATE
        else:
            if self.first_move(oppHistory1, oppHistory2):
                move = COOPERATE
            elif oppHistory1[-1] == COOPERATE and oppHistory2[-1] == COOPERATE:
                # repeat opponent last choice if both choose corporation
                move = COOPERATE
        if random.random() < self.JUMP:
            # jump moves randomly
            move = (move + 1) % 2
        return move

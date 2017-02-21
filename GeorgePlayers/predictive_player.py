from .player import Player, COOPERATE, DEFECT, PAYOFF

import math
import random

def coinflip():
    return random.random() > 0.5

def average(arr):
    return sum(arr) / len(arr)


class PredictivePlayer(Player):

    def play(self, my_history, opp1_history, opp2_history):
        if len(opp1_history) == 0 or len(opp2_history) == 0:
            return COOPERATE if coinflip() else DEFECT

        THRESH = 0.8

        opp1_coop_rate = opp1_history.count(COOPERATE) / len(opp1_history)
        opp1_prediction = COOPERATE if opp1_coop_rate > THRESH else DEFECT

        opp2_coop_rate = opp2_history.count(COOPERATE) / len(opp2_history)
        opp2_prediction = COOPERATE if opp2_coop_rate > THRESH else DEFECT

        coop_score = PAYOFF[COOPERATE][opp1_prediction][opp2_prediction]
        def_score = PAYOFF[DEFECT][opp1_prediction][opp2_prediction]

        if coop_score >= def_score:
            return COOPERATE
        else:
            return DEFECT

from .player import Player, COOPERATE, DEFECT


class TitForTatPlayer(Player):

    def play(self, my_history, opp1_history, opp2_history):
        def last(history):
            return history[-1]

        if len(opp1_history) == 0 and len(opp2_history) == 0:
            return COOPERATE
        if last(opp1_history) == DEFECT or last(opp2_history) == DEFECT:
            return DEFECT
        else:
            return COOPERATE

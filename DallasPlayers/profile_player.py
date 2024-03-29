'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-13
@note: contains a player using a strategy where profile players
'''
import unittest
import sys
import time
from random import randint
# Adds higher directory to python modules path.
sys.path.append("..") 
from DallasPlayers.player import Player, DEFECT, COOPERATE
from DallasPlayers.adaptive_player import AdaptivePlayer
from DallasPlayers.cooperate_player import CooperatePlayer
from DallasPlayers.defect_player import DefectPlayer
from DallasPlayers.gradual_player import GradualPlayer
from DallasPlayers.grudger_player import GrudgerPlayer
from DallasPlayers.naive_peace_maker_player import NaivePeaceMakerPlayer
from DallasPlayers.naive_prober_player import NaiveProberPlayer
from DallasPlayers.random_player import RandomPlayer
from DallasPlayers.remorseful_prober import RemorsefulProberPlayer
from DallasPlayers.repeat_outcome_player import RepeatOutcomePlayer
from DallasPlayers.repeat_outcome_random_player \
    import RepeatOutcomeRandomPlayer
from DallasPlayers.soft_grudger_player import SoftGrudgerPlayer
from DallasPlayers.suspicious_player import SuspiciousPlayer
from DallasPlayers.tit_for_tat_player import TitForTatPlayer
from DallasPlayers.tit_for_tat_random_player import TitForTatRandomPlayer
from DallasPlayers.tit_for_two_tats_player import TitForTwoTatsPlayer
from DallasPlayers.tit_for_two_tats_random_player \
    import TitForTwoTatsRandomPlayer
from DallasPlayers.true_peace_maker import TruePeaceMakerPlayer
ALL_PLAYERS = [AdaptivePlayer,
               CooperatePlayer,
               DefectPlayer,
               GradualPlayer,
               GrudgerPlayer,
               NaivePeaceMakerPlayer,
               NaiveProberPlayer,
               RandomPlayer,
               RemorsefulProberPlayer,
               RepeatOutcomePlayer,
               RepeatOutcomeRandomPlayer,
               SoftGrudgerPlayer,
               SuspiciousPlayer,
               TitForTatPlayer,
               TitForTatRandomPlayer,
               TitForTwoTatsPlayer,
               TitForTwoTatsRandomPlayer,
               TruePeaceMakerPlayer]
VIABLE_STRATEGIES = [
                    AdaptivePlayer,
                    TitForTatPlayer,
                    GrudgerPlayer,
                    GradualPlayer
                    ]
PROFILES = [
            AdaptivePlayer,
            CooperatePlayer,
            DefectPlayer,
            GradualPlayer,
            GrudgerPlayer,
            NaivePeaceMakerPlayer,
            RandomPlayer,
            RepeatOutcomePlayer,
            SuspiciousPlayer,
            TitForTatPlayer,
            TitForTwoTatsPlayer,
            TruePeaceMakerPlayer
            ]
PLAYER_LOOKUP = {
                    "Adaptive Player": AdaptivePlayer(),
                    "Cooperate Player": CooperatePlayer(),
                    "Defect Player": DefectPlayer(),
                    "Gradual Player": GradualPlayer(),
                    "Grudger Player": GrudgerPlayer(),
                    "Naive Peace Maker": NaivePeaceMakerPlayer(),
                    "Naive Prober Player": NaiveProberPlayer(),
                    "Random Player": RandomPlayer(),
                    "Repeat Outcome Player": RepeatOutcomePlayer(),
                    "Suspicious Player": SuspiciousPlayer(),
                    "Tit for Tat Player": TitForTatPlayer(),
                    "Tit for Two Tats Player": TitForTwoTatsPlayer(),
                    "True Peace Maker Player": TruePeaceMakerPlayer()
                    }
STRATEGY_LOOKUP = {'Tit for Tat Player': {'Tit for Tat Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Grudger Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Tit for Two Tats Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'True Peace Maker Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Random Player': {'Tit for Tat Player': 1, 'Defect Player': 3, 'Grudger Player': 3, 'Suspicious Player': 1}, 'Repeat Outcome Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Gradual Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Naive Peace Maker': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Cooperate Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Adaptive Player': {'Adaptive Player': 1}, 'Defect Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Naive Prober Player': {'Grudger Player': 2}}, 'Grudger Player': {'Tit for Tat Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Grudger Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Tit for Two Tats Player': 1}, 'Tit for Two Tats Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'True Peace Maker Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Random Player': {'Defect Player': 2, 'Grudger Player': 3, 'Naive Prober Player': 1}, 'Repeat Outcome Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Gradual Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Naive Peace Maker': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Cooperate Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Adaptive Player': {'Tit for Tat Player': 2, 'Grudger Player': 2}, 'Defect Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Suspicious Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'Naive Prober Player': 1}, 'Naive Prober Player': {'Tit for Tat Player': 2, 'Grudger Player': 1}}, 'Tit for Two Tats Player': {'Tit for Tat Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Grudger Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Tit for Two Tats Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'True Peace Maker Player': {'Tit for Tat Player': 2, 'Grudger Player': 2, 'True Peace Maker Player': 2, 'Repeat Outcome Player': 2, 'Gradual Player': 2, 'Naive Peace Maker': 2, 'Cooperate Player': 2, 'Tit for Two Tats Player': 2, 'Suspicious Player': 1}, 'Random Player': {'Naive Peace Maker': 3}, 'Repeat Outcome Player': {'Tit for Tat Player': 3, 'Grudger Player': 3, 'True Peace Maker Player': 3, 'Repeat Outcome Player': 3, 'Gradual Player': 3, 'Naive Peace Maker': 3, 'Cooperate Player': 3, 'Tit for Two Tats Player': 3, 'Suspicious Player': 2}, 'Gradual Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Naive Peace Maker': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Cooperate Player': {'Random Player': 2}, 'Adaptive Player': {'Adaptive Player': 1}, 'Defect Player': {'Defect Player': 1, 'Suspicious Player': 1}}, 'True Peace Maker Player': {'Tit for Tat Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Grudger Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Tit for Two Tats Player': {'Tit for Tat Player': 2, 'Grudger Player': 2, 'True Peace Maker Player': 2, 'Repeat Outcome Player': 2, 'Gradual Player': 2, 'Naive Peace Maker': 2, 'Cooperate Player': 2, 'Tit for Two Tats Player': 2, 'Suspicious Player': 1}, 'True Peace Maker Player': {'Tit for Tat Player': 3, 'Grudger Player': 3, 'True Peace Maker Player': 3, 'Repeat Outcome Player': 3, 'Gradual Player': 3, 'Naive Peace Maker': 3, 'Cooperate Player': 3, 'Tit for Two Tats Player': 3, 'Suspicious Player': 2}, 'Random Player': {'Naive Peace Maker': 2}, 'Repeat Outcome Player': {'Naive Prober Player': 2}, 'Gradual Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Naive Peace Maker': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Cooperate Player': {'Random Player': 1}, 'Adaptive Player': {'Suspicious Player': 3, 'Adaptive Player': 1}, 'Defect Player': {'Defect Player': 1, 'Suspicious Player': 3}}, 'Random Player': {'Tit for Tat Player': {'Tit for Tat Player': 1, 'Defect Player': 3, 'Grudger Player': 3, 'Suspicious Player': 1}, 'Grudger Player': {'Defect Player': 2, 'Grudger Player': 3, 'Naive Prober Player': 1}, 'Tit for Two Tats Player': {'Naive Peace Maker': 3}, 'True Peace Maker Player': {'Naive Peace Maker': 2}, 'Random Player': {'Defect Player': 1, 'Grudger Player': 2, 'Adaptive Player': 3}, 'Repeat Outcome Player': {'Defect Player': 2, 'Grudger Player': 1, 'Adaptive Player': 3}, 'Gradual Player': {'Defect Player': 1, 'Grudger Player': 2, 'Suspicious Player': 3}, 'Naive Peace Maker': {'Defect Player': 1, 'Grudger Player': 2, 'Naive Prober Player': 3}, 'Cooperate Player': {'Defect Player': 1, 'Grudger Player': 2, 'Adaptive Player': 3}, 'Adaptive Player': {'Tit for Tat Player': 2, 'Suspicious Player': 3}, 'Defect Player': {'Suspicious Player': 1}, 'Suspicious Player': {'Defect Player': 1, 'Suspicious Player': 2}, 'Naive Prober Player': {'Defect Player': 2, 'Grudger Player': 1, 'Suspicious Player': 3}}, 'Repeat Outcome Player': {'Tit for Tat Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Grudger Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Tit for Two Tats Player': {'Tit for Tat Player': 3, 'Grudger Player': 3, 'True Peace Maker Player': 3, 'Repeat Outcome Player': 3, 'Gradual Player': 3, 'Naive Peace Maker': 3, 'Cooperate Player': 3, 'Tit for Two Tats Player': 3, 'Suspicious Player': 2}, 'True Peace Maker Player': {'Naive Prober Player': 2}, 'Random Player': {'Defect Player': 2, 'Grudger Player': 1, 'Adaptive Player': 3}, 'Repeat Outcome Player': {'Defect Player': 1, 'Adaptive Player': 3}, 'Gradual Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Naive Peace Maker': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Cooperate Player': {'Defect Player': 1, 'Adaptive Player': 2}, 'Adaptive Player': {'Tit for Tat Player': 2, 'Suspicious Player': 1, 'Naive Prober Player': 3}}, 'Gradual Player': {'Tit for Tat Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Grudger Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'True Peace Maker Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Random Player': {'Defect Player': 1, 'Grudger Player': 2, 'Suspicious Player': 3}, 'Repeat Outcome Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Gradual Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Naive Peace Maker': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Cooperate Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1, 'Suspicious Player': 1}, 'Tit for Two Tats Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Defect Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Naive Prober Player': {'Tit for Tat Player': 2, 'Grudger Player': 3}}, 'Naive Peace Maker': {'Tit for Tat Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Grudger Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Tit for Two Tats Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'True Peace Maker Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Random Player': {'Defect Player': 1, 'Grudger Player': 2, 'Naive Prober Player': 3}, 'Repeat Outcome Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Gradual Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Naive Peace Maker': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Cooperate Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Adaptive Player': {'Tit for Tat Player': 3, 'Adaptive Player': 1}, 'Defect Player': {'Defect Player': 2, 'Suspicious Player': 3}}, 'Cooperate Player': {'Tit for Tat Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Grudger Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Tit for Two Tats Player': {'Random Player': 2}, 'True Peace Maker Player': {'Random Player': 1}, 'Random Player': {'Defect Player': 1, 'Grudger Player': 2, 'Adaptive Player': 3}, 'Repeat Outcome Player': {'Defect Player': 1, 'Adaptive Player': 2}, 'Gradual Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1, 'Suspicious Player': 1}, 'Naive Peace Maker': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'True Peace Maker Player': 1, 'Repeat Outcome Player': 1, 'Gradual Player': 1, 'Naive Peace Maker': 1, 'Cooperate Player': 1, 'Tit for Two Tats Player': 1}, 'Cooperate Player': {'Defect Player': 1, 'Adaptive Player': 2}, 'Adaptive Player': {'Adaptive Player': 1, 'Naive Prober Player': 3}, 'Defect Player': {'Defect Player': 1, 'Suspicious Player': 1}}, 'Adaptive Player': {'Tit for Tat Player': {'Adaptive Player': 1}, 'Grudger Player': {'Tit for Tat Player': 2, 'Grudger Player': 2}, 'Tit for Two Tats Player': {'Adaptive Player': 1}, 'True Peace Maker Player': {'Suspicious Player': 3, 'Adaptive Player': 1}, 'Random Player': {'Tit for Tat Player': 2, 'Suspicious Player': 3}, 'Repeat Outcome Player': {'Tit for Tat Player': 2, 'Suspicious Player': 1, 'Naive Prober Player': 3}, 'Naive Peace Maker': {'Tit for Tat Player': 3, 'Adaptive Player': 1}, 'Cooperate Player': {'Adaptive Player': 1, 'Naive Prober Player': 3}, 'Adaptive Player': {'Defect Player': 1, 'Grudger Player': 2}, 'Defect Player': {'Defect Player': 2, 'Suspicious Player': 2}}, 'Defect Player': {'Tit for Tat Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Grudger Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Tit for Two Tats Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'True Peace Maker Player': {'Defect Player': 1, 'Suspicious Player': 3}, 'Random Player': {'Suspicious Player': 1}, 'Gradual Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Naive Peace Maker': {'Defect Player': 2, 'Suspicious Player': 3}, 'Cooperate Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Adaptive Player': {'Defect Player': 2, 'Suspicious Player': 2}, 'Defect Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Suspicious Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Naive Prober Player': {'Defect Player': 1, 'Suspicious Player': 1}}, 'Suspicious Player': {'Random Player': {'Defect Player': 1, 'Suspicious Player': 2}, 'Defect Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Suspicious Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Grudger Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'Naive Prober Player': 1}, 'Naive Prober Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'Naive Prober Player': 1}}, 'Naive Prober Player': {'Tit for Tat Player': {'Grudger Player': 2}, 'Grudger Player': {'Tit for Tat Player': 2, 'Grudger Player': 1}, 'Random Player': {'Defect Player': 2, 'Grudger Player': 1, 'Suspicious Player': 3}, 'Gradual Player': {'Tit for Tat Player': 2, 'Grudger Player': 3}, 'Defect Player': {'Defect Player': 1, 'Suspicious Player': 1}, 'Suspicious Player': {'Tit for Tat Player': 1, 'Grudger Player': 1, 'Naive Prober Player': 1}, 'Naive Prober Player': {'Tit for Tat Player': 2}}}


class ProfilePlayer(Player):
	"""
	The ProfilePlayers profiles it competitors
		and picks the best strategy based upon data obtained
	"""
	THRESH = 0.7
	def studentID(self):
		"""Returns the student id
		"""
		return "20652186"

	def agentName(self):
		"""Returns the agent name
		"""
		return "Stalker Player"

	def play(self, myHistory, oppHistory1, oppHistory2):
		"""Returns the play

		Args:
			myHistory: history of plays for this player
			oppHistory1: the history of player 1
			oppHistory2: the history of player 2
			player: the player to profile
		Returns:
			: 1 for DEFECT, 0 for COOPERATE
		"""
		# what player profile should be use
		player = self.best_profile(myHistory, oppHistory1, oppHistory2)
		# get the player caught up to date
		for move in range(0, len(myHistory)):
			player.play(myHistory[0:move],
						oppHistory1[0:move],
						oppHistory2[0:move])
		return player.play(myHistory, oppHistory1, oppHistory2)

	def profile(self, myHistory, oppHistory1, oppHistory2, player):
		"""Returns the amount the player represents myHistory

		Args:
			myHistory: history of plays for this player
			oppHistory1: the history of player 1
			oppHistory2: the history of player 2
			player: the player to profile
		Returns:
			: the probability the player represents myHistory (0<=p<=1)
		"""
		correct = 0
		for i in range (0, len(myHistory)):
			play = player.play(	myHistory[0:i],
								oppHistory1[0:i],
								oppHistory2[0:i])
			if play == myHistory[i]:
				correct += 1
		return correct / len(myHistory)

	def best_profile(self, myHistory, oppHistory1, oppHistory2):
		"""Returns the best profile given the current history

		Args:
			myHistory: history of plays for this player
			oppHistory1: the history of player 1
			oppHistory2: the history of player 2
		Returns:
			best_player: the Class Name for the best profile
		"""
		if len(myHistory) >= 1:
			player_one = {}
			player_two = {}
			# get a profile for all the players
			for profile in PROFILES:
				p1_prob = self.profile(	oppHistory1,
										myHistory,
										oppHistory2,
										profile())
				if p1_prob > self.THRESH:
					player_one[profile().agentName()] = p1_prob
				p2_prob = self.profile(	oppHistory2,
										myHistory,
										oppHistory1,
										profile())
				if p2_prob > self.THRESH:
					player_two[profile().agentName()] = p2_prob
			# if no profile then just assume is a random player
			if len(player_one.keys()) == 0:
				player_one[PLAYER_LOOKUP["Random Player"]] = 1
			if len(player_two.keys()) == 0:
				player_two[PLAYER_LOOKUP["Random Player"]] = 1
			# calculate the expect rank for each strategy
			best_rank = 15000000
			best_player = None
			for strategy in VIABLE_STRATEGIES:
				player = strategy()
				expected_rank = 0
				# loop through all possible profiles for player 1
				for p1, p1_prob in player_one.items():
					# loop through all possible profiles for player 2
					for p2, p2_prob in player_two.items():
						# assume rank is bad unless noted
						rank = 15
						try:
							if strategy in STRATEGY_LOOKUP[p1][p2].keys():
								rank = STRATEGY_LOOKUP[p1][p2][strategy]
						except KeyError:
							pass
						expected_rank += rank * p1_prob * p2_prob
				# have new best player
				if expected_rank < best_rank:
					best_rank = expected_rank
					best_player = strategy
			best_player = best_player()
		else:
			best_player = PLAYER_LOOKUP["Cooperate Player"]
		return best_player


class Test(unittest.TestCase):
	def setUp(self):
		self.player = ProfilePlayer()
		self.start = time.time()

	def tearDown(self):
		t = time.time() - self.start
		print("{}: {:.3f}".format(self.id(), t))

	def testProfile(self):
		prob = self.player.profile(	[COOPERATE],
									[COOPERATE],
									[COOPERATE],
									PLAYER_LOOKUP["Cooperate Player"])
		self.assertEqual(prob, 1)
		prob = self.player.profile(	[DEFECT],
									[COOPERATE],
									[COOPERATE],
									PLAYER_LOOKUP["Cooperate Player"])
		self.assertEqual(prob, 0)


	def testPlayTime(self):
		play = self.player.play(	
								[randint(0, 1) for x in range(0, 100)],
								[randint(0, 1) for x in range(0, 100)],
								[randint(0, 1) for x in range(0, 100)]
								)	

	def testRandomPlay(self):
		for x in range(0, 100):
			play = self.player.play(	
								[randint(0, 1) for x in range(0, 100)],
								[randint(0, 1) for x in range(0, 100)],
								[randint(0, 1) for x in range(0, 100)]
								)			


if __name__ == "__main__":
	# import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
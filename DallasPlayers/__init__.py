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
PLAYERS = [GrudgerPlayer, AdaptivePlayer, SuspiciousPlayer]
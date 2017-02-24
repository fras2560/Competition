'''
@author: Dallas Fraser
@id: 20652186
@class: CS686
@date: 2016-02-18
@note: analyzing the different players
'''
from tournament import scoreGame
from DallasPlayers.profile_player import ProfilePlayer, ALL_PLAYERS as PLAYERS


def run_matchup(p1, p2, p3, matches, rounds):
    p1_score = 0
    p2_score = 0
    p3_score = 0
    wins = 0
    for __ in range(0, matches):
        [p1_temp, p2_temp, p3_temp] = scoreGame(p1, p2, p3, rounds)
        p1_score += p1_temp
        p2_score += p2_temp
        p3_score += p3_temp
        if p1_temp >= p2_temp and p1_temp >= p3_temp:
            wins += 1
    return (p1_score / matches, p2_score / matches, p3_score / matches, wins)


def player_pairs():
    for p2 in range(0, len(PLAYERS)):
        for p3 in range(p2, len(PLAYERS)):
            yield(PLAYERS[p2](), PLAYERS[p3]())


def run(matches, rounds):
    with open("stalkeroutputs.csv", "w+") as f:
        for p in PLAYERS:
            for competitors in player_pairs():
                print("{} & {}".format(competitors[0].agentName(),
                                       competitors[1].agentName()))
                player = p()
                results = run_matchup(player,
                                      competitors[0],
                                      competitors[1],
                                      matches,
                                      rounds)
                s = "{},{},{},,{:.2f},{:.2f},{:.2f},{},{:.3f}"
                print(s.format(
                                player.agentName(),
                                competitors[0].agentName(),
                                competitors[1].agentName(),
                                results[0],
                                results[1],
                                results[2],
                                results[3],
                                results[3] / matches), file=f)
                print(",,,,,,,,,,", file=f)


if __name__ == "__main__":
    run(100, 100)

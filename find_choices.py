'''
Created on Feb 22, 2017

@author: d6fraser
'''

from pprint import PrettyPrinter
from DallasPlayers import PLAYER_LOOKUP


def parse_line(line):
    columns = line.strip().split(",")
    players = [
                PLAYER_LOOKUP[columns[0].strip()],
                PLAYER_LOOKUP[columns[1].strip()],
                PLAYER_LOOKUP[columns[2].strip()]
               ]
    rank = int(columns[-1])
    wins = float(columns[-2])
    return (players, rank, wins)


def run(filename):
    pp = PrettyPrinter(indent=1)
    with open(filename) as f:
        strategy_lookup = {}
        for line in f:
            try:
                (players, rank, wins) = parse_line(line)
                if rank < 4 and wins > 0.70:
                    p1 = players[1].agentName()
                    p2 = players[2].agentName()
                    strategy = players[0].agentName()
                    if p1 not in strategy_lookup.keys():
                        strategy_lookup[p1] = {}
                    if p2 not in strategy_lookup.keys():
                        strategy_lookup[p2] = {}
                    if p2 not in strategy_lookup[p1].keys():
                        strategy_lookup[p1][p2] = {}
                    if p1 not in strategy_lookup[p2].keys():
                        strategy_lookup[p2][p1] = {}
                    strategy_lookup[p1][p2][strategy] = rank
                    strategy_lookup[p2][p1][strategy] = rank
            except KeyError:
                pass
    print(strategy_lookup)
    pp.pprint(strategy_lookup)

if __name__ == "__main__":
    run("pairings.csv")

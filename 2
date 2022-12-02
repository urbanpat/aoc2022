from pathlib import Path

path = Path(__file__).parent / "input"

games = path.read_text().split("\n")

HisMapping = {
    "A": "R",
    "B": "P",
    "C": "S",
}
MyMapping = {
    "X": "R",
    "Y": "P",
    "Z": "S",
}

PointsOfFirstPlayer = {
    "RP": 0,
    "RS": 6,
    "RR": 3,
    "PP": 3,
    "PS": 0,
    "PR": 6,
    "SP": 6,
    "SS": 3,
    "SR": 0,
}

ChoiceScores = {
    "R": 1,
    "P": 2,
    "S": 3,
}

GameResults = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}


class Game:
    def __init__(self, game_string: str):
        if len(game_string) != 3:
            print("pruser")

        self.his = HisMapping[game_string.split(" ")[0]]
        self.my = MyMapping[game_string.split(" ")[1]]
        self.res = game_string.split(" ")[1]

    @property
    def game_tuple(self):
        return self.my + self.his

    @property
    def game_result_score1(self):
        return PointsOfFirstPlayer[self.game_tuple]

    @property
    def choice_score(self):
        return ChoiceScores[self.my]

    @property
    def total_score1(self):
        return self.game_result_score1 + self.choice_score

    @property
    def what_to_pick(self):
        return score_to_pick(self.res, self.his)

    def total_score2(self):
        return ChoiceScores[self.what_to_pick] + GameResults[self.res]


def score_to_pick(result: str, his_choise: str):
    score = GameResults[result]
    viable_strategies = [strat for strat, sc in PointsOfFirstPlayer.items() if sc == score]
    the_strat = [strat for strat in viable_strategies if strat[1] == his_choise]
    return the_strat[0][0]


game_results = [Game(game).total_score1 for game in games[:-1]]
print(sum(game_results))

game_results2 = [Game(game).total_score2() for game in games[:-1]]
print(sum(game_results2))



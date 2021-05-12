from collections import defaultdict


class ResultsTable:
    def __init__(self, results):
        self.results = defaultdict(lambda: {
            "W": 0,
            "D": 0,
            "L": 0,
        })

        for row in results:
            self.add_result(row)

    def add_result(self, row):
        team, opponent, outcome = row.split(";")
        if outcome == "win":
            self.results[team]["W"] += 1
            self.results[opponent]["L"] += 1
        elif outcome == "loss":
            self.results[team]["L"] += 1
            self.results[opponent]["W"] += 1
        else:  # draw
            self.results[team]["D"] += 1
            self.results[opponent]["D"] += 1

    def _calculate_points(self, team):
        return 3 * self.results[team]["W"] + self.results[team]["D"]

    def _calculate_matches_played(self, team):
        return sum(self.results[team].values())

    def to_table(self):
        fmt_str = "{0:30} | " + " | ".join(f"{{{i}:>2}}" for i in range(1, 6))
        table = [fmt_str.format("Team", "MP", "W", "D", "L", "P")]
        points = {team: self._calculate_points(team)
                  for team in self.results}
        matches = {team: self._calculate_matches_played(team)
                   for team in self.results}

        def sort_teams(team):
            return (-points[team], team)

        sorted_teams = sorted(self.results.keys(), key=sort_teams)

        for team in sorted_teams:
            table.append(fmt_str.format(
                team,
                matches[team],
                self.results[team]["W"],
                self.results[team]["D"],
                self.results[team]["L"],
                points[team],
            ))

        return table


def tally(rows):
    table = ResultsTable(rows)
    return table.to_table()

"""Function to help create a ranking table.
collections module is used to give a default value to the new keys.
"""

from collections import defaultdict

def tally(rows):
    """Create a ranking table with how many matches, wins, draws, losses, and points have each team.
    
    :param rows: list[str] - list with each match: "team1;team2;result_related_to_team1".
    :return: list[str] - ranking table.
    """
    teams = defaultdict(lambda: [0, 0, 0, 0, 0])
    outcomes = {"win": [(1, 0, 0, 3), (0, 0, 1, 0)], "draw": [(0, 1, 0, 1), (0, 1, 0, 1)], "loss": [(0, 0, 1, 0), (1, 0, 0, 3)]}
    for match in rows:
        team1, team2, result = match.split(";")
        stats1, stats2 = outcomes[result]
        for team, stat in [(team1, stats1), (team2, stats2)]:
            teams[team][0] += 1
            teams[team][1] += stat[0]
            teams[team][2] += stat[1]
            teams[team][3] += stat[2]
            teams[team][4] += stat[3]
    sorted_teams = sorted(teams.items(), key = lambda x: (-x[1][4], x[0]))
    table = [f"{'Team':<30} | MP |  W |  D |  L |  P"]
    for name, info in sorted_teams:
        row = f"{name:<30} | {info[0]:>2} | {info[1]:>2} | {info[2]:>2} | {info[3]:>2} | {info[4]:>2}"
        table.append(row)
    return table
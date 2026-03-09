from collections import defaultdict

"""Function to help create a position table.
"""

def tally1(rows):
    """Create a position table with data about  matches, win, draws, losses, and point of each team.
    
    :param rows: list[str] - list with each match (team1;team2;result_relationing_to_team1)
    :return: list[str] - position table.
    """
    teams = {}
    for match in rows:
        team1, team2, result = match.split(";")
        info_team1 = [1, 1 if "win" == result else 0, 1 if "draw" == result else 0, 1 if "loss" == result else 0]
        info_team1 = info_team1 + [3 * info_team1[1] + info_team1[2]]
        info_team2 = [1, 1 if "loss" == result else 0, 1 if "draw" == result else 0, 1 if "win" == result else 0]
        info_team2 = info_team2 + [3 * info_team2[1] + info_team2[2]]
        if team1 not in teams:
            teams[team1] = info_team1
        else:
            for index in range(5): teams[team1][index] += info_team1[index]
        if team2 not in teams:
            teams[team2] = info_team2
        else:
            for index in range(5): teams[team2][index] += info_team2[index]
    teams_ordered = sorted(teams.items(), key = lambda x: (-x[1][-1], x[0]))
    result = ["Team                           | MP |  W |  D |  L |  P"]
    for key, value in teams_ordered:
        result.append(key + (31 - len(key)) * " " + "|  " + str(value[0]) + " |  " + str(value[1]) + " |  " + str(value[2]) + " |  " + str(value[3]) + (" |  " if len(str(value[4])) == 1 else " | ") + str(value[4]))
    return result

def tally(rows):
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
"""Function to help create a position table.
"""

def tally(rows):
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
"""Solution to high_scores exercise.
"""

class HighScores:
    """Create a HighScores object with a initial scores list.

    Attributes
    ----------
    scores: list - of scores.

    Methods
    -------
    latest(): returns the las added score.
    personal_best(): returns the best score.
    personal_top_three(): returns the three best scores.
    """

    def __init__(self, scores):
        self.scores = scores
    
    def latest(self):
        "Return the las added score."
        return self.scores[-1]
    
    def personal_best(self):
        "Return the best score."
        return max(self.scores)
    
    def personal_top_three(self):
        "Return the three best scores."
        return sorted(self.scores, reverse=True)[:3]

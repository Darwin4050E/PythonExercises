"""Solution to space_age exercise.
"""

class SpaceAge:
    """Create and SpaceAge object with a initial age in seconds.

    Mehods
    ------
    on_earth(): return the age, in seconds, in Earth Years.
    on_mercury(): return the age, in seconds, in Mercury Years.
    on_venus(): return the age, in seconds, in Venus Years.
    on_mars(): return the age, in seconds, in Mars Years.
    on_jupiter(): return the age, in seconds, in Jupiter Years.
    on_saturn(): return the age, in seconds, in Saturn Years.
    on_uranus(): return the age, in seconds, in Uranus Years.
    on_neptune(): return the age, in seconds, in Neptune Years.
    """

    def __init__(self, seconds):
        self.seconds = seconds
    
    def on_earth(self):
        return round(self.seconds * (1 / 31557600), 2)

    def on_mercury(self):
        return round(self.seconds * (1 / 31557600) * (1 / 0.2408467), 2)

    def on_venus(self):
        return round(self.seconds * (1 / 31557600) * (1 / 0.61519726), 2)

    def on_mars(self):
        return round(self.seconds * (1 / 31557600) * (1 / 1.8808158), 2)
    
    def on_jupiter(self):
        return round(self.seconds * (1 / 31557600) * (1 / 11.862615), 2)

    def on_saturn(self):
        return round(self.seconds * (1 / 31557600) * (1 / 29.447498), 2)

    def on_uranus(self):
        return round(self.seconds * (1 / 31557600) * (1 / 84.016846), 2)

    def on_neptune(self):
        return round(self.seconds * (1 / 31557600) * (1 / 164.79132), 2)
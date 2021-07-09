class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self._earth_year = seconds / 31557600

    def _round(self, value):
        decimals = 2
        return round(value, decimals)

    def on_earth(self):
        return self._round(self._earth_year)

    def on_mercury(self):
        return self._round(self._earth_year / 0.2408467)

    def on_venus(self):
        return self._round(self._earth_year / 0.61519726)

    def on_mars(self):
        return self._round(self._earth_year / 1.8808158)

    def on_jupiter(self):
        return self._round(self._earth_year / 11.862615)

    def on_saturn(self):
        return self._round(self._earth_year / 29.447498)

    def on_uranus(self):
        return self._round(self._earth_year / 84.016846)

    def on_neptune(self):
        return self._round(self._earth_year / 164.79132)

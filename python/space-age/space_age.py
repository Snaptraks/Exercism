class SpaceAge:
    SECONDS_PER_YEAR = {planet: ratio * 31557600 for planet, ratio in {
        "earth": 1.0,
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }.items()}

    def __init__(self, seconds):
        self.seconds = seconds

        for planet, seconds_per_year in self.SECONDS_PER_YEAR.items():
            setattr(self, f"on_{planet}", self._on_planet(seconds_per_year))

    def _on_planet(self, seconds_per_year):
        return lambda: round(self.seconds / seconds_per_year, 2)

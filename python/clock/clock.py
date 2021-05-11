class Clock:
    def __init__(self, hour, minute):
        self._parse_time(hour, minute)

    def _parse_time(self, hour, minute):
        self._minute = minute % 60
        self._hour = (hour + minute // 60) % 24

    def __repr__(self):
        return f"{self._hour:02d}:{self._minute:02d}"

    def __eq__(self, other):
        return (self._hour, self._minute) == (other._hour, other._minute)

    def __add__(self, minutes):
        return self.__class__(self._hour, self._minute + minutes)

    def __sub__(self, minutes):
        return self.__add__(-minutes)

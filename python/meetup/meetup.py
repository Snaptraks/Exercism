from datetime import date, timedelta

WEEKDAY = ["Monday", "Tuesday", "Wednesday",
           "Thursday", "Friday", "Saturday", "Sunday"]


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    day = date(year, month, 1)  # first day of the month
    one_day = timedelta(days=1)
    one_week = timedelta(days=7)

    # get the correct day
    while WEEKDAY[day.weekday()] != day_of_week:
        day += one_day

    # get the correct week
    if week == "1st":
        pass  # we are already the first day_of_week

    elif week == "2nd":
        day += one_week

    elif week == "3rd":
        day += 2 * one_week

    elif week == "4th":
        day += 3 * one_week

    elif week == "5th":
        day += 4 * one_week

    elif week == "last":
        while (next_week := day + one_week).month == month:
            day = next_week

    elif week == "teenth":
        while not (13 <= (day := day + one_week).day <= 19):
            pass

    if day.year != year or day.month != month:
        raise MeetupDayException("No such day exists!")

    return day

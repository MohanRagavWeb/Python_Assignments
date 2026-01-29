import calendar

def get_day_name(month, day, year):
    day_index = calendar.weekday(year, month, day)
    days = [
        "MONDAY", "TUESDAY", "WEDNESDAY",
        "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
    ]
    return days[day_index]

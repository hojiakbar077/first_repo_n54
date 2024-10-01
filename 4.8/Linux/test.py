import datetime


def log_day_week(log_data):

    year, month, day = int(log_data[:4]), int(log_data[5:7]), int(log_data[8:10])

    log_day = datetime.date(year, month, day)

    return log_day.strftime("%A")

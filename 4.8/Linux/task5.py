import datetime
import json

FILE = "logs.txt"


def log_day_week(log_data):
    year, month, day = int(log_data[:4]), int(log_data[5:7]), int(log_data[8:10])

    log_day = datetime.date(year, month, day)

    return log_day.strftime("%A")


def weekly_log(log_file):
    weekday_log = {
        "Monday": {}, "Tuesday": {}, "Wednesday": {}, "Thursday": {}, "Friday": {}, "Saturday": {}, "Sunday": {}
    }
    log_stats = ["INFO", "ERROR", "WARNING", "DEBUG"]

    with open(log_file) as file:
        lines = file.readlines()

    for log_status in log_stats:
        for line in lines:
            if log_status in line:
                if log_status in weekday_log[log_day_week(line)]:
                    weekday_log[log_day_week(line)][log_status] += 1
                else:
                    weekday_log[log_day_week(line)][log_status] = 0

    return weekday_log


def most_active_day(log_file):
    active_day = 0
    result = str

    for key, value in weekly_log(log_file).items():
        daily_logs = 0
        for log_status in value:
            daily_logs += value[log_status]
            if daily_logs > active_day:
                result = key
            active_day = daily_logs

    return result


def most_log_status(weekday):
    daily_log = weekly_log(FILE)[weekday]
    most_status_occurrence = 0
    active_status = None
    for log_status in weekly_log(FILE)[weekday]:
        if daily_log[log_status] > most_status_occurrence:
            active_status = log_status

    return active_status


most_day = most_active_day(FILE)

print(f"The most active day => {most_day}"
      f"\nThe most frequent log status => {most_log_status(most_day)}")

# with open("weekly_log.json", "w") as j_file:
#     json.dump(weekly_log("logs.txt"), j_file, indent=4)

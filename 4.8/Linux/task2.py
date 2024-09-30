FILE = "logs.txt"

new_file = ""


def error_detector(file_name):
    hours = []
    with open(file_name) as file:
        content = file.readlines()
    for line in content:
        hours.append(line[10:13])

    return f"{max(hours)} was the most active hour."


print(error_detector(FILE))

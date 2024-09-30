FILE = "logs.txt"


def error_detector(file_name):
    with open(file_name) as file:
        content = file.read()
    all_logs = content.count("\n")
    errors = content.count("ERROR")

    result = errors / all_logs * 100
    return f"{round(result, 2)} % errors."


print(error_detector(FILE))


def error_logs(filename):
    count = 0
    count_two = 0
    logs = []
    with open(filename, 'r') as file:
        for line in file:

            if "ERROR" in line:
                count += 1

            if any(keyword in line for keyword in ["DEBUG", "INFO", "ERROR", "WARNING"]):
                logs.append(line.strip())

    for log in logs:
        print(log)
        count_two += 1

    print(f"ERRORS: {count}")
    print(f"Logs: {count_two}")

    if count_two > 0:
        error_percentage = (count / count_two) * 100
        print(f"Xatoliklar foizi: {error_percentage:.2f}%")
    else:
        print("Loglar mavjud emas.")

error_logs('errors.txt')

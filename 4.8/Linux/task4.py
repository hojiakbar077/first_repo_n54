FILE = "logs.txt"


def info_detector(file_name):
    with open(file_name) as file:
        content = file.read()
        info = content.count("INFO")
        all_logs = content.count("\n")

    result = info / all_logs * 100
    return f"{round(result, 2)} % info messages."


def info_stat(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    info_data = {}

    for line in lines:
        if "INFO" in line:
            info_status = line[28:-1]
            if info_status in info_data:
                info_data[info_status] += 1
            else:
                info_data[info_status] = 1

    for key in info_data:
        if info_data[key] == max(info_data.values()):
            return key, info_data[key]


print(f"The most occurred info status => {info_stat(FILE)[0]} occurred {info_stat(FILE)[1]} times.")
print(info_detector(FILE))

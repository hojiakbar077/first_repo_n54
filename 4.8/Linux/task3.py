FILE = "logs.txt"

new_file = ""


def log_detector(file_name, log_status):
    status_dict = {}
    with open(file_name) as file:
        content = file.readlines()

    for line in content:
        if log_status in line:
            if line[:10] in status_dict:
                status_dict[line[:10]] += 1
            else:
                status_dict[line[:10]] = 1

    return status_dict


for key, value in log_detector(FILE, "ERROR").items():
    print(key, value)

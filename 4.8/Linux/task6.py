import matplotlib.pyplot as plt


def info_stat(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    all_errors = 0
    info_data = {}

    for line in lines:
        if "ERROR" in line:
            all_errors += 1
            info_status = line[29:-1]
            if info_status in info_data:
                info_data[info_status] += 1
            else:
                info_data[info_status] = 1

    return info_data, all_errors


info_data_, all_errors_ = info_stat("logs.txt")
error_status = []
error_percent = []


for key, value in info_data_.items():
    error_status.append(key)
    status_percent = round((value / all_errors_ * 100), 2)
    error_percent.append(status_percent)

print(error_percent)
plt.pie(error_percent, labels=error_status)
plt.show()


print(info_stat("logs.txt"))

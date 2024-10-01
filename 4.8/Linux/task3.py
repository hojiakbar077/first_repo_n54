import matplotlib.pyplot as plt

FILE = "logs.txt"


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

    sorted_keys = sorted([key for key in status_dict.keys()])
    status_dict = {key: status_dict[key] for key in sorted_keys}

    return status_dict


print(log_detector(FILE, "WARNING"))


warning_data = log_detector(FILE, "WARNING")
debug_data = log_detector(FILE, "DEBUG")

warning_data_count = [value for value in warning_data.values()]
warning_data_date = [key for key in warning_data.keys()]

debug_data_count = [value for value in debug_data.values()]
debug_data_date = [key for key in debug_data.keys()]


ax = plt.axes()
plt.plot(warning_data_date, warning_data_count, color="red")
plt.plot(debug_data_date, debug_data_count, color="blue")

plt.text(55, 750, "warning", fontsize=25, color="red")
plt.text(10, 750, "debug", fontsize=25, color="blue")

labels = ["2024-07-01", "2024-07-15", "2024-08-01", "2024-08-15", "2024-09-01", "2024-09-15"]
ax.set_xticks([0, 18, 36, 54, 72, 90], labels, rotation=70)


plt.show()

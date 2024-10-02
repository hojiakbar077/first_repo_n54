import matplotlib.pyplot as plt
from collections import Counter
import re
from datetime import datetime

# # Load the large log file content (for demonstration purposes, I will simulate with a few entries)
# log_file_path = '../log_file.txt'
#
# # Simulating loading data from a file (actual implementation will load the file directly)
# with open(log_file_path, 'r') as file:
#     log_lines = file.readlines()
#
# # Regular expression to match log entries and extract timestamp and status
# log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (WARNING|DEBUG):')
#
# # Extract timestamps and statuses for "WARNING" and "DEBUG"
# warning_times = []
# debug_times = []
#
# for line in log_lines:
#     match = log_pattern.search(line)
#     if match:
#         timestamp_str, status = match.groups()
#         timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
#         if status == "WARNING":
#             warning_times.append(timestamp.date())
#         elif status == "DEBUG":
#             debug_times.append(timestamp.date())
#
# # Count occurrences of WARNING and DEBUG log entries by date
# warning_counts = Counter(warning_times)
# debug_counts = Counter(debug_times)
#
# # Sort dates and prepare data for plotting
# dates = sorted(set(warning_counts.keys()).union(set(debug_counts.keys())))
# warning_values = [warning_counts.get(date, 0) for date in dates]
# debug_values = [debug_counts.get(date, 0) for date in dates]
#
# # Plot the data
# plt.figure(figsize=(10, 6))
# plt.plot(dates, warning_values, label='WARNING', marker='o')
# plt.plot(dates, debug_values, label='DEBUG', marker='x')
# plt.xlabel('Date')
# plt.ylabel('Log Count')
# plt.title('Warning vs Debug Log Entries Over Time')
# plt.legend()
# plt.xticks(rotation=45)
# plt.tight_layout()
#
# # Display the plot
# plt.show()


# Simulating data for "ERROR" log entries to solve the 6th task (Error Type Breakdown)
import re
from collections import Counter

log_lines = [
    "2024-01-01 12:30:45 - ERROR: Failed to connect to database.\n",
    "2024-01-01 14:25:30 - ERROR: Authentication failed.\n",
    "2024-01-02 09:12:12 - ERROR: Invalid input detected.\n",
    "2024-01-02 16:55:01 - ERROR: Failed to connect to database.\n",
    "2024-01-03 10:45:23 - ERROR: Service unavailable, retrying...\n",
    "2024-01-03 15:21:33 - ERROR: Authentication failed.\n",
    "2024-01-04 11:11:11 - ERROR: Access denied for user.\n",
    "2024-01-05 08:22:45 - ERROR: Failed to connect to database.\n",
    "2024-01-05 11:45:12 - ERROR: Invalid input detected.\n",
]

# Regular expression to match ERROR log entries and extract messages
error_pattern = re.compile(r'ERROR: (.+)\.')

# Extract and categorize error messages
error_messages = []

for line in log_lines:
    match = error_pattern.search(line)
    if match:
        error_message = match.group(1)
        error_messages.append(error_message)

# Count occurrences of different error types
error_counts = Counter(error_messages)

# Prepare data for plotting
error_types = list(error_counts.keys())
error_values = list(error_counts.values())

# Plot the error type breakdown
plt.figure(figsize=(10, 6))
plt.barh(error_types, error_values, color='skyblue')
plt.xlabel('Count')
plt.ylabel('Error Type')
plt.title('Error Type Breakdown')
plt.tight_layout()

# Display the plot
plt.show()
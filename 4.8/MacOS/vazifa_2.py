
import re                         ### (regular expressions) yani (soat:daqiq:soniya) bolish u/n kutubxona
import matplotlib.pyplot as plt  ### diagrammalar chizish uchun

with open('C:/Users/Lenovo PC/Desktop/8-lesson/errors.txt', 'r') as file:
    logs = file.readlines()

hours = {}
for log in logs:
    time = re.search(r'\d{2}:\d{2}:\d{2}', log)  # vaqtni qidiradi (00:00:00 kabi formatdagi vaqtni topadi).
    if time:
        hour = time.group().split(':')[0]  # Faqat soatni olish
        if hour in hours:
            hours[hour] += 1
        else:
            hours[hour] = 1

print("Har bir soatdagi loglar soni:")
for hour, miqdor in hours.items():
    print(f"Soat {hour}: {miqdor} ta log")

plt.bar(hours.keys(),hours.values())
plt.xlabel('Soat')
plt.ylabel('Loglar soni')
plt.title('Har bir soatdagi loglar soni')
plt.show()

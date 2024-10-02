
import re
from collections import defaultdict
from datetime import datetime


with open('C:/Users/Lenovo PC/Desktop/8-lesson/errors.txt', 'r') as file:
    logs = file.readlines()


kunlar = defaultdict(
    lambda: {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0})  # Har bir kun uchun turli xabarlarni sanash

# Har bir logni tekshirish
for log in logs:
    sana = re.search(r'\d{4}-\d{2}-\d{2}', log)  # Log sanasini topish
    if sana:
        sana = sana.group()
        hafta_kuni = datetime.strptime(sana, '%Y-%m-%d').strftime('%A')  # Haftaning kunini aniqlash

        if 'INFO' in log:
            kunlar[hafta_kuni]['INFO'] += 1
        elif 'ERROR' in log:
            kunlar[hafta_kuni]['ERROR'] += 1
        elif 'DEBUG' in log:
            kunlar[hafta_kuni]['DEBUG'] += 1
        elif 'WARNING' in log:
            kunlar[hafta_kuni]['WARNING'] += 1

eng_kop_kun = max(kunlar, key=lambda k: sum(kunlar[k].values()))
print(f"Eng ko'p log yozuvi bo'lgan kun: {eng_kop_kun}")

print(f"{eng_kop_kun} kuni log turlari:")
for tur, miqdor in kunlar[eng_kop_kun].items():
    print(f"{tur}: {miqdor} ta")

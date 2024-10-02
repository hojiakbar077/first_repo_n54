
import re
import matplotlib.pyplot as plt
from collections import defaultdict

with open('C:/Users/Lenovo PC/Desktop/8-lesson/errors.txt', 'r') as file:
    logs = file.readlines()  # Log faylidagi barcha qatorlarni o'qidi

# Har bir kunda WARNING va DEBUG yozuvlarini sanash
yozuvlar = defaultdict(lambda: {'WARNING': 0, 'DEBUG': 0})  # Har bir kun uchun lug'at yaratish

for log in logs:  # Har bir log qatorini tekshirish
    sana = re.search(r'\d{4}-\d{2}-\d{2}', log)
    if sana:
        sana = sana.group()  # Sanani olish
        if 'WARNING' in log:  # Agar logda WARNING bo'lsa
            yozuvlar[sana]['WARNING'] += 1  # WARNING sonini oshirish
        elif 'DEBUG' in log:  # Agar logda DEBUG bo'lsa
            yozuvlar[sana]['DEBUG'] += 1  # DEBUG sonini oshirish

kunlar = list(yozuvlar.keys())  # Sanalar ro'yxatini olish
warning_counts = [yozuvlar[kun]['WARNING'] for kun in kunlar]  # Har bir kun uchun WARNING soni
debug_counts = [yozuvlar[kun]['DEBUG'] for kun in kunlar]  # Har bir kun uchun DEBUG soni


plt.plot(kunlar, warning_counts, marker='o', label='WARNING')  # WARNING yozuvlari chizish
plt.plot(kunlar, debug_counts, marker='x', label='DEBUG')  # DEBUG yozuvlari chizish
plt.xlabel('Kunlar')  # X o'qining nomi
plt.ylabel('LOG Count')  # Y o'qining nomi
plt.title('Kunlik WARNING va DEBUG yozuvlari')  # Diagramma sarlavhasi
plt.legend()
plt.show()  # Diagrammani ko'rsatish, ishga tushirish

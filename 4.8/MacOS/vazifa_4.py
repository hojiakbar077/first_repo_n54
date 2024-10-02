

from collections import defaultdict

# Log faylni ochish va barcha qatorlarni o'qib olish
with open('C:/Users/Lenovo PC/Desktop/8-lesson/errors.txt', 'r') as file:
    logs = file.readlines()

# Harakat turlari va umumiy loglarni sanash uchun lug'atlar yaratish
action_types = defaultdict(int)  # Har bir harakat turi uchun sanash
info_count = 0  # "INFO" yozuvlari sonini hisoblash uchun o'zgaruvchi
total_logs = 0  # Umumiy log yozuvlarini hisoblash uchun o'zgaruvchi

#  Har bir log qatorini ko'rib chiqish
for log in logs:
    total_logs += 1  # Har bir log qatori umumiy loglar soniga qo'shilyapti
    if 'INFO' in log:  # Agar log qatorida "INFO" bo'lsa
        info_count += 1  # INFO logini hisoblash
        # Muvaffaqiyatli harakatlarni aniqlash uchun ba'zi kalit so'zlarni tekshirish
        if 'tizimga kirish' in log:  # Foydalanuvchi tizimga kirishi
            action_types['Tizimga kirish'] += 1
        elif 'ma’lumotlarni olish' in log:  # Ma'lumotlarni olish
            action_types['Ma’lumotlarni olish'] += 1
        else:
            action_types['Boshqa harakatlar'] += 1  # Boshqa harakatlar

#  Foizlarni hisoblash
if total_logs > 0:
    success_percentage = (info_count / total_logs) * 100
    print(f"Umumiy loglar soni: {total_logs}")
    print(f"INFO yozuvlari soni: {info_count}")
    print(f"Muvaffaqiyatli harakatlarning foizi: {success_percentage:.2f}%")

    # Har bir harakat turi sonini chop qilish
    for action, count in action_types.items():
        print(f"{action}: {count} ta")
else:
    print("Log faylda yozuvlar mavjud emas.")

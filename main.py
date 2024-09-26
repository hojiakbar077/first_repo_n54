numbers = [1, 2, 3, 4, 5]

number_tuple = (1, 2, 3, 4, 5)

number_set = {1, 2, 3, 4, 5}

number_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

total = 0
for num in numbers:
    total += num

average = total / len(numbers)

print("Umumiy yig'indi:", total)
print("O'rtacha qiymat:", average)

if average > 3:
    print("O'rtacha qiymat 3 dan katta.")
else:
    print("O'rtacha qiymat 3 dan kichik yoki teng.")

total_tuple = sum(number_tuple)
average_tuple = total_tuple / len(number_tuple)

print("Tuple uchun umumiy yig'indi:", total_tuple)
print("Tuple uchun o'rtacha qiymat:", average_tuple)

total_set = sum(number_set)
average_set = total_set / len(number_set)

print("Set uchun umumiy yig'indi:", total_set)
print("Set uchun o'rtacha qiymat:", average_set)

total_dict = sum(number_dict.values())
average_dict = total_dict / len(number_dict)

print("Dictionary uchun umumiy yig'indi:", total_dict)
print("Dictionary uchun o'rtacha qiymat:", average_dict)

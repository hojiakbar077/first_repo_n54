numbers = [1, 2, 3, 4, 5]

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

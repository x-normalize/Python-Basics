# Напишете програма, която чете цяло число от конзолата и на всеки следващ ред цели числа,
# докато тяхната сума стане по-голяма или равна на първоначал
# ното число. След приключване на четенето
# да се отпечата сумата на въведените числа.
max_num = int(input())
all_numbers = 0
while max_num > all_numbers:
    number = int(input())
    all_numbers += number
else:
    print(all_numbers)







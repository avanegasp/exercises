num = 1000
new_num = []

new_num = [n < 1000 for n in num]
new_num = 0

for n in range(num, 0, -1):
    if n % 3 == 0 and n % 5 == 0:
        new_num.append(n)
print(new_num)

while num > 0:
    if num % 3 == 0 and num % 5 == 0:
        print(num)
    num -= 1

new_num = [n for n in range(num) if n % 3 == 0 or n % 5 == 0]
print(new_num)
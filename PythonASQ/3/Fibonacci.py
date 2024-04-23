last = 1
current = 1

for i in range(20):
    if i == 0 or i == 1:
        print(1)
    else:
        temp = current
        current = current + last
        last = temp
        print(current)

print()

last = 1
current = 1
i = 0
while i < 20:
    if i == 0 or i == 1:
        print(1)
    else:
        temp = current
        current = current + last
        last = temp
        print(current)
    i += 1
    
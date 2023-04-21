count = 0
for i in range(26):
    for j in range(26-i):
        for k in range(26-i-j):
            for l in range(26-i-j-k):
                for m in range(26-i-j-k-l):
                    count += 1
print(count)
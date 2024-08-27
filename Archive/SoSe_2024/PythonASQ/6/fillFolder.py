
for i in range(1,1001):
    with open(f"voll/{i}.txt", "w") as f:
        f.write("Python\n"*i)
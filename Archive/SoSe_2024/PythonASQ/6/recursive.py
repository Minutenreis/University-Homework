import os
import sys
import time

if len(sys.argv) > 2:
    print("Usage: python recursive.py <num>")
    sys.exit(1)
num = int(sys.argv[1]) if len(sys.argv) == 2 else 0
if num >= 5:
    sys.exit(0)
ownPath = __file__

script = open(ownPath, "r").read()

os.mkdir(f"folder{num}")
os.chdir(f"folder{num}")

with open(f"recursive{num}.py", "w") as f:
    f.write(script)

os.system(f"python3 recursive{num}.py {num+1}")

if num == 4:
    time.sleep(15)

os.remove(f"recursive{num}.py")
os.chdir("..")
os.rmdir(f"folder{num}")
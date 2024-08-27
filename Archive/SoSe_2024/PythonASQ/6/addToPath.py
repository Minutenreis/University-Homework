import sys
import os

if len(sys.argv) != 2:
    print("Usage: python addToPath.py <path>")
    sys.exit(1)

path = sys.argv[1]
if not os.path.exists(path):
    print("Path does not exist")
    sys.exit(1)

if path not in sys.path:
    sys.path.append(path)
    print("Path added to sys.path")
else:
    print("Path already in sys.path")
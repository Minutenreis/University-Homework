from pathlib import Path
import sys
import resource
import gc

def chrAndStart(str: list[str]):
    x = str.split("\t")
    # get chromosome number
    chr = int(x[0][3:])
    # get start position
    start = int(x[1])
    return chr, start

if len(sys.argv) != 3:
    print("Usage: python mergeAnnotation.py <file1> <file2>")
    sys.exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]
usedMemory = 0
sharedList = []

with open(file1, "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
        sharedList.append(line)
    
with open(file2, "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
        sharedList.append(line)

sharedList.sort(key=chrAndStart)

# merge overlapping regions with same chromosome number

mergedList = []
mergedList.append(sharedList[0])

for i in range(1, len(sharedList)):
    shared_list_i = sharedList[i].split()
    merged_list_min_1 = mergedList[-1].split()
    if shared_list_i[0] == merged_list_min_1[0] and shared_list_i[1] <= merged_list_min_1[2]:
        mergedList[-1] = f"{merged_list_min_1[0]}\t{merged_list_min_1[1]}\t{shared_list_i[2]}\t{merged_list_min_1[3]}{shared_list_i[3]}\n"
    else:
        mergedList.append(sharedList[i])

del sharedList
gc.collect()

Path("bin").mkdir(parents=True, exist_ok=True)
with open("bin/mergedAnnotation.bed", "w") as f:
    f.write("chr\tstart\tend\tannotation\n")
    for line in mergedList:
        f.write(line)

statPeakMemoryMB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
print(f"Peak memory usage: {statPeakMemoryMB:.2f} MB")
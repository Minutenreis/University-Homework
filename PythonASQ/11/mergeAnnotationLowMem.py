from pathlib import Path
import sys
import resource
import subprocess

if len(sys.argv) != 3:
    print("Usage: python mergeAnnotationLowMem.py <file1> <file2>")
    sys.exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]

# check if appendAndSortList.out exists
if not Path("bin/appendAndSort.out").is_file():
    subprocess.run(["g++","-std=c++20", "appendAndSortList.cpp", "-O3","-march=native", "-o", "bin/appendAndSort.out"])    

subprocess.run(["bin/appendAndSort.out", file1, file2])
# merge overlapping regions with same chromosome number

mergedList = []
with open("bin/sorted.bed", "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            mergedList.append(line)
            continue
        shared_list_i = line.split()
        merged_list_min_1 = mergedList[-1].split()
        if shared_list_i[0] == merged_list_min_1[0] and int(shared_list_i[1]) <= int(merged_list_min_1[2]):
            mergedList[-1] = f"{merged_list_min_1[0]}\t{merged_list_min_1[1]}\t{max(int(shared_list_i[2]),int(merged_list_min_1[2]))}\t{merged_list_min_1[3]}{shared_list_i[3]}\n"
        else:
            mergedList.append(line)

Path("bin").mkdir(parents=True, exist_ok=True)
with open("bin/mergedAnnotation.bed", "w") as f:
    f.write("chr\tstart\tend\tannotation\n")
    for line in mergedList:
        f.write(line)

statPeakMemoryMB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
print(f"Peak Memory Python: {statPeakMemoryMB:.2f} MB")
import sys
import re

if len(sys.argv) != 2:
    print("Usage: textanalysis.py filename")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as file:
    text = file.read()

sentencePattern = re.compile(r"[.!?]")
numSentences = len(sentencePattern.findall(text))
print(f"Anzahl Sätze: {numSentences}")

yearPattern = re.compile(r"\b\d{4}\b")
years = yearPattern.findall(text)
yearNumbers = [int(year) for year in years]
yearNumbers.sort()

currentCentury = 0
first = True
for year in yearNumbers:
    if year // 100 != currentCentury:
        if not first:
            print()
        currentCentury = year // 100
        print(f"{currentCentury}00er : {year}", end="")
        first = False
    else:
        print(f", {year}", end="")
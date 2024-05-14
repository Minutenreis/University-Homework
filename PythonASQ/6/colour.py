colourOccurances = {}

with open("Farben.txt","r") as f:
    colors = f.readlines()
    for color in colors:
        color = color.strip()
        colourOccurances[color] = colourOccurances.get(color,0) + 1

sortedColours = sorted(colourOccurances.items(), key=lambda x: x[1])
for color in sortedColours:
    print(f"{color[0]}: {color[1]}")
print("most common color: ", sortedColours[-1][0])
print("least common color: ", sortedColours[0][0])
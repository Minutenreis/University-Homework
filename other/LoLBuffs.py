import os

mypath = os.path.dirname(__file__)
BalancesFile = "Balances.txt"
SkinReleasesFile = "SkinReleases.txt"
Buffs = []
Nerfs = []
Adjustments = []

with open(os.path.join(mypath, BalancesFile), "r") as f:
    Balances = f.read().splitlines()
    for patch, line in enumerate(Balances,0):
        skins = line.split()
        Buffs.append([])
        Nerfs.append([])
        Adjustments.append([])
        for i, champ in enumerate(skins,1):
            if i == 1:
                continue
            elif champ.startswith("+"):
                Buffs[patch].append(champ[1:])
            elif champ.startswith("-"):
                Nerfs[patch].append(champ[1:])
            elif champ.startswith("."):
                Adjustments[patch].append(champ[1:])
            else:
                print("Error: Unrecognized change type")
                print(champ)

skins = []
with open(os.path.join(mypath, SkinReleasesFile), "r") as f:
    SkinReleases = f.read().splitlines()
    for patch, line in enumerate(SkinReleases,0):
        champs = line.split()
        skins.append([])
        for i, champ in enumerate(champs,1):
            if i == 1:
                continue
            else:
                skins[patch].append(champ)

numBuffsBeforeSkin = 0
numNerfsBeforeSkin = 0
numAdjustmentsBeforeSkin = 0

def isInLastNPatches(champ, data, start:int, n: int) -> bool:
    for i in range(start-n, start+1):
        if(i < 0):
            continue
        if champ in data[i]:
            return True
    return False

numOfPatchesToCheck = 3

for patch, data in enumerate(skins,0):
    for champ in data:
        if isInLastNPatches(champ, Buffs, patch, numOfPatchesToCheck):
            numBuffsBeforeSkin += 1
        if isInLastNPatches(champ, Nerfs, patch, numOfPatchesToCheck):
            numNerfsBeforeSkin += 1
        if isInLastNPatches(champ, Adjustments, patch, numOfPatchesToCheck):
            numAdjustmentsBeforeSkin += 1
print("Buffs before skin: " + str(numBuffsBeforeSkin))
print("Nerfs before skin: " + str(numNerfsBeforeSkin))
print("Adjustments before skin: " + str(numAdjustmentsBeforeSkin))
print()
print("BuffsTotal: " + str(sum(len(x) for x in Buffs)))
print("NerfsTotal: " + str(sum(len(x) for x in Nerfs)))
buffNerfRatio = sum(len(x) for x in Buffs)/sum(len(x) for x in Nerfs)
print("AdjustmentsTotal: " + str(sum(len(x) for x in Adjustments)))
print("SkinsTotal: " + str(sum(len(x) for x in skins)))
print()
print("Buffs before skin relative to Buff/Nerf ratio: " + str(numBuffsBeforeSkin/numNerfsBeforeSkin * buffNerfRatio))
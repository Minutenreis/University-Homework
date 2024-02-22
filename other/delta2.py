#Lolalytics Algorithm for Delta2

def expectedWR(wr1,wr2):
    return (wr1-wr1*wr2)/(wr1+wr2-2*wr1*wr2)

def delta2(wr1,wr2,wr1vs2,avgWR):
    diff = avgWR - 0.5
    wr1vs2 = wr1vs2-diff
    wr1 = wr1-diff
    wr2 = wr2-diff
    return wr1vs2-expectedWR(wr1,wr2)

def delta2_percent(wr1,wr2,wr1vs2,avgWR):
    wr1 = wr1/100
    wr2 = wr2/100
    wr1vs2 = wr1vs2/100
    avgWR = avgWR/100
    return delta2(wr1,wr2,wr1vs2,avgWR) * 100

# Example:
# TF Mid WR: 51.35%
# Maokai Sup WR: 55.67%
# TF vs Maokai WR: 48.03%
# Average WR: 50.31%

print(delta2_percent(51.35,55.67,48.03,50.31)) # 2.04965

# Lolalytics Delta2: 2.05
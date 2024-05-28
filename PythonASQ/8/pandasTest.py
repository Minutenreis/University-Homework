import pandas as pd

dataframes = []

for i in range(1,101):
    dataframes.append(pd.read_csv(f'beispieldaten/Experiment_{i}.csv'))

df = pd.concat(dataframes)
print('Messungen gesamt:',df.shape[0])
for i, frame in enumerate(dataframes):
    print(f'Messungen mit Wert ≥ 10 in Experiment {i+1}:',frame.loc[frame['Messwert'] > 10].shape[0])
    
medianAda = df.loc[df['Person'] == 'Ada']['Messwert'].median()
maxDaniel = df.loc[df['Person'] == 'Daniel']['Messwert'].max()
if medianAda > maxDaniel:
    print('Ada hat höheren Median als Daniels Maximum')
else:
    print('Daniel hat höheren Maximalwert als Adas Median')
    
medians = pd.Series([frame["Messwert"].median() for frame in dataframes])
medianOfMedians = medians.median()
print('Median der Mediane:',medianOfMedians)

mostCommonRadio = df.loc[df['Messgerät'] == 'Radiometer'].value_counts('Person')
print('Häufigste Person bei Radiometer:',mostCommonRadio.index[0])

aprilLaser = pd.Series([frame.loc[(frame['Monat'] == 'Apr') & (frame['Messgerät'] == 'Laser')].shape[0] for frame in dataframes])
print(f"Experiment {aprilLaser.idxmax()+1} hat die meisten Laser-Messungen im April")
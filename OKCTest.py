    
import pandas as pd
from functions import FG_stats, eFGCalc2, zoneSort
# 1. read in the .csv file as Pandas dataframe shotData
shotData = pd.read_csv('OKCTest.csv')

shotData = shotData.groupby(shotData.team)
teamA = pd.DataFrame(shotData.get_group("A"))
teamB = pd.DataFrame(shotData.get_group("B"))
#C3 = teamA[(teamA['y'] <= 7.8) & (teamA['x'].abs() > 22)]
#C3 = C3[C3['x']**2 > 22]
#print(C3)

# Get the team's total number of shot attempts
totalFGA = teamB.shape[0]

print("totalFGA\n", totalFGA)
eFG1, eFG2, efg3 = eFGCalc2(teamB)

print(eFG1)
print(eFG2)
print(efg3)
# 2. Split the dataframe into separate dataframes for each team
#TPTA, C3A, NC3A = zoneSort(teamA)

#TPTB, C3B, NC3B = zoneSort(teamB)

'''
print("TPT\n", TPT)
print("C3\n", C3)
print("NC3\n", NC3)
print("END TEST")
print("")
'''

# 3. split the dataframe into three sub data frame for each shot zone
#NC3 = shotData.loc[shotData['Y'] > 7.8 and shotData['X'] >= 23.75]

#eFG = eFGCalc(NC3, "NC3")
# 4. Calculate the number of shots attempted and the number of shots made for each zone. 
#FGM, FGA = FG_stats()

# 5. Calculate the Effective Field Goal % for each zone (TPT, C3, NC3)

# 5a. eFG for TPT: FGM/FGA due to absence of 3-point shots
#eFG = (FGM + (0.5 * FGM)) /FGA

# 5b. eFG for C3 and NC3
#eFG = (FGM + (0.5 * FGM))/FGA
 
'''
    Create function that reads in dataframe and sums up total shots attempted and shots made
    def (df):
        FGM = df['fgmade'] == 1]
        FGA = df['fgmade']
    return FGM, FGA

'''

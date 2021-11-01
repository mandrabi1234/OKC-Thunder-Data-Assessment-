    
# Author: Mohi Andrabi, 10/31/2021 9:00 PM
# Note: 2-Pointer = PT2, Corner 3 = C3, Non-Corner 3 = NC3

import pandas as pd
from functions import eFGCalc2, shotDist

# 1. read in the .csv file as Pandas dataframe shotData
shotData = pd.read_csv('shots_data.csv')

# 2. Split the main dataframe into separate dataframes for each team
shotData = shotData.groupby(shotData.team)
teamA = pd.DataFrame(shotData.get_group("Team A"))
teamB = pd.DataFrame(shotData.get_group("Team B"))

# 3. Get each team's total number of shot attempts
totalFG_A = teamA.shape[0]
totalFG_B = teamB.shape[0]


# 4. Sort each team's shots into one of three zones and calculate the Effective Field Goal % for each zone.
PT2_FGA_A, C3_FGA_A, NC3_FGA_A, PT2_eFG_A, C3_eFG_A, NC3_eFG_A = eFGCalc2(teamA)

PT2_FGA_B, C3_FGA_B, NC3_FGA_B, PT2_eFG_B, C3_eFG_B, NC3_eFG_B = eFGCalc2(teamB)

# 5. Calculate the percentage of team shots attempted (shot distribution) for each shot zone
# -- Team A -- 
PT2_shotDist_A = shotDist(totalFG_A, PT2_FGA_A)
C3_shotDist_A = shotDist(totalFG_A, C3_FGA_A)
NC3_shotDist_A = shotDist(totalFG_A, NC3_FGA_A)

# -- Team B --
PT2_shotDist_B = shotDist(totalFG_B, PT2_FGA_B)
C3_shotDist_B = shotDist(totalFG_B, C3_FGA_B)
NC3_shotDist_B = shotDist(totalFG_B, NC3_FGA_B)

# 6. Print out the analysis results for each team
print("---Team A Stats---")
print("Effective Field Goal % (PT2, C3, NC3)\n")
print("* 2-Pointer eFG: ", PT2_eFG_A)
print("* Corner 3 eFG: ", C3_eFG_A)
print("* Non-Corner 3 eFG: ", NC3_eFG_A)
print(" ")
print("Shot Distribution (PT2, C3, NC3)\n")
print("* 2-Pointer: ", PT2_shotDist_A, "%")
print("* Corner 3: ", C3_shotDist_B, "%")
print("* Non-Corner 3: ", NC3_shotDist_B, "%")
print("------------------")
print(" ")
print("---Team B Stats---")
print("Effective Field Goal % (PT2, C3, NC3)\n")
print("* 2-Pointer eFG: ", PT2_eFG_B, "%")
print("* Corner 3 eFG: ", C3_eFG_B, "%")
print("* Non-Corner 3 eFG: ", NC3_eFG_B, "%")
print(" ")
print("Shot Distribution (PT2, C3, NC3)\n")
print("* 2-Pointer : ", PT2_shotDist_B, "%")
print("* Corner 3: ", C3_shotDist_B, "%")
print("* Non-Corner 3: ", NC3_shotDist_B, "%")
print("------------------")



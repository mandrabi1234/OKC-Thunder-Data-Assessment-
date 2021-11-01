import pandas as pd
def FG_stats(df):
    FGM = sum(df.fgmade == 1)
   # print("FGM\n", FGM)
    FGA = df.shape[0]
   # print("FGA\n", FGA)
    return FGM, FGA

# Function: eFGCalc
#   *Purpose: calculate effective field goal percenter
'''
def eFGCalc(df, dfName):
    FGM, FGA = FG_stats(df)

    if (dfName == "TPT"):
        eFG = FGM/FGA
    elif (dfName == "C3" or dfName == "NC3"):
        eFG = (FGM + (0.5 * FGM))/FGA
    else:
        eFG = "Dataset Inconsistency"
    return eFG
'''
def zoneSort(df):

    C3 = df[(df['y'] <= 7.8) & (df['x'].abs() > 22)]

    TPT = df[(df['y'] <= 7.8) & (df['x'].abs() < 22)]

    NC3 = df[df['y'] > 7.8]

    NC3app, TPTapp, NC3app2 = corner3Sort(NC3)

    NC3.append(NC3app)
    NC3.append(NC3app2)
    TPT.append(TPTapp)
    return TPT, C3, NC3

def corner3Sort(df):
    NC3app = df[df['y'] > 23.75]
    
    xy = df['x']**2 + df['y']**2

    TPTapp = df[(df['y'] > 7.8) & (xy <= 23.75**2)]

    NC3app2 = df[(df['y'] > 7.8) & (xy > 23.75**2)]

    return NC3app, TPTapp, NC3app2

def eFGCalc2(df):
    PT2, C3, NC3 = zoneSort(df)
    
    PT2_FGM, PT2_FGA = FG_stats(PT2)

    C3_FGM, C3_FGA = FG_stats(C3)

    #print(C3_FGM, C3_FGA)
    NC3_FGM, NC3_FGA = FG_stats(NC3)
    #print(NC3_FGM, NC3_FGA)

    PT2_eFG = PT2_FGM/PT2_FGA

    C3_eFG = (C3_FGM + (0.5 * C3_FGM))/ C3_FGA

    NC3_eFG = (NC3_FGM + (0.5 * NC3_FGM))/ NC3_FGA

    return PT2_eFG, C3_eFG, NC3_eFG

def shotDist(totalFGA, FGM):
    shotDist = (FGM/totalFGA) * 100
    return shotDist
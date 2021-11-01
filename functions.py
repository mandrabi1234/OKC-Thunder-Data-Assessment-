import pandas as pd
def FG_stats(df):
    FGM = sum(df.fgmade == 1)
    FGA = df.shape[0]
    return FGM, FGA

def zoneSort(df):

    C3 = df[(df['y'] <= 7.8) & (df['x'].abs() > 22)]

    PT2 = df[(df['y'] <= 7.8) & (df['x'].abs() <= 22)]

    NC3 = df[df['y'] > 7.8]

    NC3app, PT2app, NC3app2 = corner3Sort(NC3)

    NC3.append(NC3app)
    NC3.append(NC3app2)
    PT2.append(PT2app)
    
    return PT2, C3, NC3

def corner3Sort(df):
    NC3app = df[df['y'] > 23.75]
    
    xy = df['x']**2 + df['y']**2

    PT2app = df[(df['y'] > 7.8) & (xy <= 23.75**2)]

    NC3app2 = df[(df['y'] > 7.8) & (xy > 23.75**2)]

    return NC3app, PT2app, NC3app2

def eFGCalc2(df):
    PT2, C3, NC3 = zoneSort(df)
    
    PT2_FGM, PT2_FGA = FG_stats(PT2)

    C3_FGM, C3_FGA = FG_stats(C3)

    NC3_FGM, NC3_FGA = FG_stats(NC3)

    PT2_eFG = round((PT2_FGM/PT2_FGA), 3)

    C3_eFG = round(((C3_FGM + (0.5 * C3_FGM))/ C3_FGA), 3)

    NC3_eFG = round(((NC3_FGM + (0.5 * NC3_FGM))/ NC3_FGA), 3)

    return PT2_FGA, C3_FGA, NC3_FGA, PT2_eFG, C3_eFG, NC3_eFG

def shotDist(totalFGA, FGA):
    shotDist = (FGA/totalFGA)
    shotDist = round(shotDist, 3)
    return shotDist
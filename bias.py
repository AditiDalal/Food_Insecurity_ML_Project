from sklearn.metrics import classification_report
import pandas as pd

# Run the model and get data
from train import run_model
df, model = run_model()

# turns amount to a share and if higher than 25% turns it into a flag
df["HighBlackShare"] = (df["TractBlack"] / df["Pop2010"] > 0.20).astype(int)
df["HighHispanicShare"] = (df["TractHispanic"] / df ["Pop2010"] > 0.35).astype(int) 
df["HighWhiteShare"] = (df["TractWhite"] / df["Pop2010"]>0.40).astype(int) #turns into int 0/1
df["HighAsianShare"] = (df["TractAsian"]/df["Pop2010"] > 0.10).astype(int)
df["HighMultiShare"] = (df["TractOMultir"]/df["Pop2010"]>0.10).astype(int)

# assigns the group values into each var 
black_group = df[df["HighBlackShare"] == 1]
less_blackgroup = df[df["HighBlackShare"] == 0]

#hispanic for above
hispanic_group = df[df["HighHispanicShare"]== 1]
less_hispanicgroup = df[df["HighHispanicShare"] == 0]

#white
white_group = df[df["HighWhiteShare"]==1]
less_whitegroup = df[df["HighWhiteShare"]==0]

#asian
asian_group = df[df["HighAsianShare"] == 1]
less_asiangroup = df[df["HighAsianShare"] == 0]

#multiracial
multi_group = df[df["HighMultiShare"] == 1]
less_multigroup = df[df["HighMultiShare"] == 0]

# Classification report for each group
print("High Black Share Tracts")
print(classification_report(black_group["LILATracts_1And20"], black_group["prediction"], digits=3))

print("\nLower Black Share Tracts")
print(classification_report(less_blackgroup["LILATracts_1And20"], less_blackgroup["prediction"], digits=3))

print("\nHispanic")
print(classification_report(hispanic_group["LILATracts_1And20"], hispanic_group["prediction"], digits=3))
print("\nLower-Hispanic")
print(classification_report(less_hispanicgroup["LILATracts_1And20"], less_hispanicgroup["prediction"], digits=3))

#white
print("\nWhite")
print(classification_report(white_group["LILATracts_1And20"], white_group["prediction"], digits=3))
print("\nLower-White")
print(classification_report(less_whitegroup["LILATracts_1And20"], less_whitegroup["prediction"], digits=3))

#asian
print("\nAsian")
print(classification_report(asian_group["LILATracts_1And20"], asian_group["prediction"], digits=3))
print("\nLower-Asian")
print(classification_report(less_asiangroup["LILATracts_1And20"], less_asiangroup["prediction"], digits=3))

#multi racial
print("Multi-Racial")
print(classification_report(multi_group["LILATracts_1And20"], multi_group["prediction"], digits=3))
print("\nLower-MultiRacial")
print(classification_report(less_multigroup["LILATracts_1And20"], less_multigroup["prediction"], digits=3))




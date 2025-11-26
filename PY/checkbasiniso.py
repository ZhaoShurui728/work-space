import pandas as pd

df = pd.read_csv("landshare_basiniso_full.csv")

check = df.groupby(["lon"],["lat"])["landarea_share"].sum().reset_index()

problem_point = check[(check["landarea_share"]<1e-6)|check["landarea_share"]>1e-6]

print("总数",len(check))
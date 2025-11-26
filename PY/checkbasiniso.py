import pandas as pd

df = pd.read_csv("./CSV/landshare_basiniso_full.csv")

check = df.groupby(["lon","lat"])["landarea_share"].sum().reset_index()

problem_points = check[(check["landarea_share"]<1 - 1e-6)|check["landarea_share"]>1 + 1e-6]

print("总数",len(check))
print("不等于 1 的格点数：", len(problem_points))
print(problem_points.head())
import pandas as pd


df = pd.read_csv("landshareG.csv")

mapping = {}

# 先按 G 分组
for G, subdf in df.groupby("G"):

    # 找到同 G 的第一个没有下划线的 Rall
    parent = subdf.loc[~subdf["Rall"].str.contains("_"), "Rall"].iloc[0]

    # 找到该 G 下所有 xxx_xxxx
    children = subdf.loc[subdf["Rall"].str.contains("_"), "Rall"]

    # 建立 mapping
    for child in children:
        mapping[child] = parent

print(mapping)

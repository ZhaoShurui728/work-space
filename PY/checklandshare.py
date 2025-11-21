import pandas as pd
import numpy as np

df = pd.read_csv("./work-space/CSV/landshareG.csv")

# 是否为子项
df["is_sub"] = df["Rall"].str.contains("_")

for G in df["G"].unique():
    df_g = df[df["G"] == G]

    # 子项
    df_sub = df_g[df_g["is_sub"]]

    # 如果根本没有子项 → 跳过，不打印
    if df_sub.empty:
        continue

    # 合计子项
    sub_sum = df_sub["Value"].sum()

    # 子项合计 ≠ 1 才打印
    if not np.isclose(sub_sum, 1.0, atol=1e-8):
        print(f"### G = {G}, 子项合计 = {sub_sum}")
        print(df_g)
        print("\n")

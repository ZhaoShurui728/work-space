import numpy as np 
import pandas as pd

df = pd.read_csv("./original/CSV/compare_region_basin/region_area.csv")

# 1. 只取 CL
df_cl = df[df["type"] == "CL"]

# 2. 取 2005 和 2100，展开
df_wide = (
    df_cl[df_cl["year"].isin([2005, 2100])]
    .pivot(index="country", columns="year", values="Value")
    .dropna()
)

# 3. 相对变化率
df_wide["rel_change"] = (df_wide[2100] - df_wide[2005]) / df_wide[2005]

# 4. 是否在 ±20% 内
df_wide["within_20pct"] = df_wide["rel_change"].abs() <= 0.2

# 5. 变化方向（只对 within 的国家有意义）
df_wide["direction"] = np.where(
    df_wide["rel_change"] > 0, "increase",
    np.where(df_wide["rel_change"] < 0, "decrease", "no_change")
)

# 6. 最终结果（只保留 ±20% 内的）
result = (
    df_wide[df_wide["within_20pct"]]
    .reset_index()[["country", 2005, 2100, "rel_change", "direction"]]
)
print(result)
import gdxpds
import pandas as pd

# ---------- 第一次运行：读取 GDX ----------
gdx = gdxpds.to_dataframes("./GDX/basin analysis.gdx")

df = gdx["Area"].copy()
df.columns = ["country","year","type" ,"Value"]

# 保存为 CSV（这是关键）
df.to_csv("./original/CSV/compare_region_basin/basin_area.csv", index=False)

print("第一次处理完成，已保存csv！以后都不需要再读GDX。")

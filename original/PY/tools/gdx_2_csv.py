import gdxpds
import pandas as pd

# ---------- 第一次运行：读取 GDX ----------
gdx = gdxpds.to_dataframes("./GDX/agludata.gdx")

df = gdx["AgLULandusedata"].copy()
df.columns = ["scenario","basin","type","year" ,"value"]

# 保存为 CSV（这是关键）
df.to_csv("./original/CSV/aglu/agludata.csv", index=False)

print("第一次处理完成，已保存csv！以后都不需要再读GDX。")

import gdxpds
import pandas as pd

# ---------- 第一次运行：读取 GDX ----------
gdx = gdxpds.to_dataframes("./GDX/Mergedcomparison_region.gdx")

df = gdx["IAMCTemp"].copy()
df.columns = ["scenario","region","type","*","year" ,"value"]
df = df[df["type"] == "Emi_CO2_AFO"]
# 保存为 CSV（这是关键）
df.to_csv("./original/CSV/IAMC/Emi_CO2_basin.csv", index=False)

print("第一次处理完成，已保存csv！以后都不需要再读GDX。")

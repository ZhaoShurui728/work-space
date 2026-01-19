import gdxpds
import pandas as pd

# ---------- 第一次运行：读取 GDX ----------
gdx = gdxpds.to_dataframes("./GDX/agludata.gdx")

df = gdx["AgLULandusedata"].copy()
df.columns = ["sce","basin","var" ,"year","Value"]
df = df[df["sce"].isin(["SSP2_BaU_NoCC"])].copy()
# 现在列为: ["basin","var","year","Value"]
df_sub = df[df["var"].isin(["CL", "CROP_FLW"])].copy()
df_wide = (
    df_sub
    .pivot(index=["basin", "year"], columns="var", values="Value")
    .reset_index()
)

df_wide["Value"] = df_wide["CL"] - df_wide["CROP_FLW"].fillna(0)
df_wide[["country", "basin"]] = df_wide["basin"].str.split("_", n=1, expand=True)
df_final = df_wide[["basin", "country", "year", "Value"]].copy()




# 保存为 CSV（这是关键）
df_final.to_csv("./original/CSV/aglu/cropland(no fallowland).csv", index=False)

print("第一次处理完成，已保存csv！以后都不需要再读GDX。")
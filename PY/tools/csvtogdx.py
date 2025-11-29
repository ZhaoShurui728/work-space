import pandas as pd
import gdxpds

df = pd.read_csv("Area_year_region_crop.csv")

# 保证列顺序（year, region_agg, crop, value）
df = df[["year", "region_agg", "crop", "value"]]

# 设置 symbol 名字（可选）
df.name = "Area"

# ★ 正确写法：gdxpds 要求传 dict，不是 DataFrame
gdxpds.to_gdx({"Area": df}, "Area.gdx")

print("写入 Area.gdx 成功！")

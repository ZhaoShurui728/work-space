import pandas as pd
import xarray as xr

df_list = pd.read_csv("./original/CSV/compare_region_basin/basin_region_consistent_20pct.csv")
basin_keep = df_list["country"].unique().tolist()
nc = xr.open_dataset(".")
nc_diff = xr.open_dataset("./original/")
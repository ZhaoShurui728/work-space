import pandas as pd
import xarray as xr
import numpy as np


df_list = pd.read_csv(
    "./original/CSV/compare_region_basin/basin_region_consistent_20pct_NODIR.csv"
)
basin_keep = df_list["basin"].unique().tolist()


nc = xr.open_dataset("./original/NC/compare.nc")
nc_diff = xr.open_dataset("./original/NC/compare_diff.nc")


df_map = pd.read_csv("./original/CSV/gridset/grid_basin_output.csv")
df_map_keep = df_map[df_map["basin"].isin(basin_keep)]


lat_vals = nc["lat"].values
lon_vals = nc["lon"].values

mask = np.zeros((len(lat_vals), len(lon_vals)), dtype=bool)


for _, row in df_map_keep.iterrows():
    i = int(row["I"])
    j = int(row["J"])
    mask[i, j] = True

mask_da = xr.DataArray(
    mask,
    coords={"lat": nc["lat"], "lon": nc["lon"]},
    dims=("lat", "lon")
)

nc_sel = nc[["basin_agri", "region_agri"]]
nc_masked = nc_sel.where(mask_da)

nc_diff_masked = nc_diff.where(mask_da)


nc_masked.to_netcdf(
    "./original/NC/compare_region_basin_consistent_NODIR.nc"
)
nc_diff_masked.to_netcdf(
    "./original/NC/compare_diff_region_basin_consistent_NODIR.nc"
)

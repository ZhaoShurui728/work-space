import xarray as xr

nc = xr.open_dataset("./original/NC/compare_diff.nc")

basin_diff = nc["basin_agri_diff"]
region_diff = nc["region_agri_diff"]

basin_inc = basin_diff.where(basin_diff > 0)
region_inc = region_diff.where(region_diff > 0)

import numpy as np

def calc_top_share_timeseries(da, top_frac):

    Rt_list = []
    years = range(2010,2101,10)
    for y in years:
        times = f"{y}-01-01"
        da_y = da.sel(time=times)

        vals = da_y.values.flatten()
        vals = vals[np.isfinite(vals)]
        vals = vals[vals > 0]

        vals_sorted = np.sort(vals)[::-1]
        n_top = int(np.ceil(len(vals_sorted) * top_frac))

        top_sum = vals_sorted[:n_top].sum()
        total_sum = vals_sorted.sum()

        Rt_list.append(top_sum / total_sum)

    return Rt_list

# basin
basin_5  = calc_top_share_timeseries(basin_diff, 0.05)
basin_10 = calc_top_share_timeseries(basin_diff, 0.10)
basin_20 = calc_top_share_timeseries(basin_diff, 0.20)

# region
region_5  = calc_top_share_timeseries(region_diff, 0.05)
region_10 = calc_top_share_timeseries(region_diff, 0.10)
region_20 = calc_top_share_timeseries(region_diff, 0.20)

import pandas as pd

# 年份

years = range(2010,2101,10)
# 组装成 DataFrame
df = pd.DataFrame({
    "year": years,
    "basin_top5": basin_5,
    "basin_top10": basin_10,
    "basin_top20": basin_20,
    "region_top5": region_5,
    "region_top10": region_10,
    "region_top20": region_20,
})

# 保存为 CSV
df.to_csv(
    "./original/CSV/landuse_change_concentration_timeseries.csv",
    index=False
)

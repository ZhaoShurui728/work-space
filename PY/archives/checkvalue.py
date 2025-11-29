import xarray as xr
import numpy as np

# 打开文件
ncbasin = xr.open_dataset("basin master.nc")
ncregion = xr.open_dataset("region master.nc")

# 生成格点面积 (m^2)
R = 6371000  # 地球半径 (m)
dlat = np.deg2rad(0.5)   # 纬度分辨率
dlon = np.deg2rad(0.5)   # 经度分辨率

lat = ncbasin["lat"].values

# 使用球面公式
lat_bounds_low  = np.deg2rad(lat - 0.25)
lat_bounds_high = np.deg2rad(lat + 0.25)

area_lat = R**2 * dlon * (np.sin(lat_bounds_high) - np.sin(lat_bounds_low))
# area_lat shape = (lat,)

# 扩展为 2D area (lat, lon)
area_2d = np.repeat(area_lat[:, np.newaxis], len(ncbasin["lon"]), axis=1)

# 转到 xarray
area_xr = xr.DataArray(
    data=area_2d,
    dims=("lat", "lon"),
    coords={"lat": ncbasin.lat, "lon": ncbasin.lon}
)

years = range(2010, 2110, 10)
with open("output.txt", "w", encoding="utf-8") as f:
    for var in ncbasin.data_vars:
        difflist = []

        for i in years:
            basin = ncbasin[var].sel(time=f"{i}-01-01").astype("float64")
            region = ncregion[var].sel(time=f"{i}-01-01").astype("float64")

            # ★ 做面积加权（m^2）
            sum1_m2 = float((basin * area_xr).sum())
            sum2_m2 = float((region * area_xr).sum())

            # ★ 转成平方千米 (km^2)
            sum1 = sum1_m2 / 1e10
            sum2 = sum2_m2 / 1e10

            difflist.append(sum1 - sum2)

        avg = np.nanmean(difflist)


        f.write(f"From 2010–2100, {var}: averagediff = {avg:.2f} Mha\n")

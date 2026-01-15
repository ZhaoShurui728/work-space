import xarray as xr

nc = xr.open_dataset("./work-space/original/NC/compare.nc")

basin = nc["basin_agri"]
region = nc["region_agri"]

basin_diff = basin.diff(dim="year")
region_diff = region.diff(dim="year")

basin_diff = basin_diff.rename("basin_agri_diff")
region_diff = region_diff.rename("region_agri_diff")

nc_diff = xr.Dataset(
    {
        "basin_agri_diff": basin_diff,
        "region_agri_diff": region_diff
    }
)
nc_diff.to_netcdf("./work-space/original/NC/compare_diff.nc")

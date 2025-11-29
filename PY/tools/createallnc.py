import xarray as xr
import numpy as np
import os

# --- 切换到脚本目录 ---
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# --- 读入数据 ---
basin = xr.open_dataset("../NC/basin master.nc")
region = xr.open_dataset("../NC/region master.nc")

# --- 定义一个函数（对 Dataset 生成大类） ---
def generate_classes(ds):
    out = {}

    out["agri"] =  ds["c3ann"] + ds["c3nfx"] + ds["c3per"] + ds["c4ann"] + ds["c4per"]

    out["irrig_agri"] = ds["irrig_c3ann"] + ds["irrig_c3nfx"] + ds["irrig_c3per"] + ds["irrig_c4ann"] + ds["irrig_c4per"]

    out["grain"] = ds["rice"] + ds["wheat"] + ds["maize"]

    out["econ"] =  ds["sugarcrops"] + ds["oilcrops"] + ds["othercrops"]
    
    out["grassland"] = ds["pastr"] + ds["range"]

    out["forest"] = ds["primf"] + ds["secdf"] + ds["pltns"]

    return out


# --- 为 basin 和 region 分别生成 ---
basin_cls = generate_classes(basin)
region_cls = generate_classes(region)

# --- 把所有内容合并到一个 Dataset ---
newnc = xr.Dataset()

for name, data in basin_cls.items():
    newnc[f"basin_{name}"] = data

for name, data in region_cls.items():
    newnc[f"region_{name}"] = data

# --- 保存 ---
newnc.to_netcdf("../NC/compare.nc")

print("Saved compare.nc successfully!")

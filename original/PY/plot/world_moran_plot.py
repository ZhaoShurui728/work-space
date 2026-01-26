import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./original/CSV/moran/world_moran_3f.csv")

variables = ["agri", "forest", "grassland"]

for var in variables:
    plt.figure(figsize=(6,4))
    
    plt.plot(df["year"], df[f"basin_{var}"], marker="o", label=f"basin_{var}",linewidth =2)
    plt.plot(df["year"], df[f"region_{var}"], marker="o", label=f"region_{var}",linewidth =2)
    
    plt.xlabel("Year",fontsize=14)
    plt.ylabel("Global Moran's I",fontsize=14)
    plt.ylim(0.5, 1)
    plt.legend(loc = "lower right",fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"./original/plot/moran/{var}_moran.png", dpi=600, bbox_inches="tight")
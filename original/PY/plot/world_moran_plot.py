import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./original/CSV/moran/world_moran_3f.csv")

variables = ["agri", "forest", "grassland"]
titles    = ["Agriculture", "Forest", "Grassland"]

fig, axes = plt.subplots(
    1, 3,
    figsize=(15, 4),
    sharey=True
)

for ax, var, title in zip(axes, variables, titles):

    ax.plot(
        df["year"],
        df[f"basin_{var}"],
        marker="o",
        linewidth=2,
        label="Basin"
    )

    ax.plot(
        df["year"],
        df[f"region_{var}"],
        marker="o",
        linewidth=2,
        label="Region"
    )

    ax.set_title(title, fontsize=14)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylim(0.5, 1.0)
    ax.grid(True, alpha=0.3)

# 只在最左边放 y 轴标签
axes[0].set_ylabel("Global Moran's I", fontsize=14)

# 只放一个 legend（避免重复）
axes[-1].legend(
    loc="lower right",
    fontsize=12
)

plt.tight_layout()

plt.savefig(
    "./original/plot/moran/moran_all_landuse.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()

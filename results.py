# results_viz.py
#
# Visual summary for Warren, George, Ray, and Cathie
# - Bar chart of final portfolio values + P/L
# - Per-agent bar charts of holdings (shares per symbol)

import matplotlib.pyplot as plt
import numpy as np

# ---------- 1. Raw data (from your dashboard) ----------

INITIAL_CAPITAL = 10_000

agents = {
    "Warren": {
        "final_value": 9769,      # from earlier run ($9,769)
        "holdings": {
            "LI": 440,
            "HBAN": 50,
            "BRK.B": 0,
            "AAPL": 2,
            "JNJ": 1,
            "PG": 0,
            "KO": 2,
        },
    },
    "George": {
        "final_value": 9890,      # "$9,890 ⬇ $-110"
        "holdings": {
            "VTV": 30,
            "HYG": 8,
            "TLT": 10,
            "XLK": 5,
            "XLF": 3,
            "XLP": 4,
        },
    },
    "Ray": {
        "final_value": 9854,      # "$9,854 ⬇ $-146"
        "holdings": {
            "EEM": 40,
            "VWO": 40,
            "VHT": 5,
            "EIDO": 45,
            "IEMG": 10,
            "SCHE": 10,
            "XBI": 3,
        },
    },
    "Cathie": {
        "final_value": 9580,      # "$9,580 ⬇ $-420"
        "holdings": {
            "BITO": 150,
            "SOL": 350,
            "XRP": 150,
            "ETHE": 55,
            "SATO": 25,
            "DAPP": 75,
        },
    },
}

# Add P/L (absolute and %) for convenience
for name, info in agents.items():
    fv = info["final_value"]
    pnl = fv - INITIAL_CAPITAL
    info["pnl"] = pnl
    info["pnl_pct"] = pnl / INITIAL_CAPITAL * 100.0

# ---------- 2. Figure 1: Final portfolio values ----------

names = list(agents.keys())
final_values = [agents[n]["final_value"] for n in names]
pnls = [agents[n]["pnl"] for n in names]

x = np.arange(len(names))

fig1, ax1 = plt.subplots(figsize=(8, 4))
bars = ax1.bar(x, final_values)

ax1.set_xticks(x)
ax1.set_xticklabels(names)
ax1.set_ylabel("Final Portfolio Value ($)")
ax1.set_title("Final Portfolio Value per Agent")

# Annotate bars with P/L
for i, (bar, pnl) in enumerate(zip(bars, pnls)):
    height = bar.get_height()
    label = f"{height:,.0f}\n({pnl:+.0f})"
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        label,
        ha="center",
        va="bottom",
        fontsize=9,
    )

fig1.tight_layout()

# ---------- 3. Figure 2: Holdings per agent ----------

fig2, axes = plt.subplots(2, 2, figsize=(10, 6))
axes = axes.flatten()

for ax, name in zip(axes, names):
    holdings = agents[name]["holdings"]
    symbols = list(holdings.keys())
    qty = list(holdings.values())

    ax.bar(symbols, qty)
    ax.set_title(name)
    ax.set_ylabel("Quantity")
    ax.set_xticklabels(symbols, rotation=45, ha="right")

fig2.suptitle("Holdings per Agent", fontsize=14)
fig2.tight_layout(rect=[0, 0.03, 1, 0.95])

# ---------- 4. Show plots ----------

plt.show()

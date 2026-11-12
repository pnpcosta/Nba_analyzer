
import pandas as pd
import numpy as np

df = pd.read_csv("data/raw/players_2025_26.csv")

league_pct = (
    df["three_point_makes"].sum()
    / df["three_point_attempts"].sum()
)

k = 100

df["adjusted_3p_pct"] = (
    df["three_point_makes"] + k * league_pct
) / (df["three_point_attempts"] + k)

df["three_pa_per36"] = (
    df["three_point_attempts"] / df["minutes"] * 36
)

eligible = df[
    (df["minutes"] >= 500) &
    (df["three_point_attempts"] >= 50)
].copy()

# Efficiency Score - Normalização logística
median_e = eligible["adjusted_3p_pct"].median()

s = 0.10

eligible["E"] = 100 / (
    1 + np.exp(
        -(eligible["adjusted_3p_pct"] - median_e) / s
    )
)

# Volume Score - Normalização linear
volume_ref = 13.2

eligible["V"] = 100 * np.clip(
    eligible["three_pa_per36"] / volume_ref,
    0,
    1
)

# Shooting Score - Média geométrica ponderada
eligible["shooting_score"] = (
    eligible["E"] ** 0.60
    * eligible["V"] ** 0.40
)

# Ordenar jogadores por Shooting Score
top_shooters = eligible.sort_values(
    "shooting_score",
    ascending=False
)

print("\nTop 20 Shooters:")
print(
    top_shooters[[
        "player_name",
        "adjusted_3p_pct",
        "three_pa_per36",
        "E",
        "V",
        "shooting_score"
    ]].head(20).round(3).to_string(index=False)
)

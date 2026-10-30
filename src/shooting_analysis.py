
import pandas as pd

# Carregar os jogadores
df = pd.read_csv("data/raw/players_2025_26.csv")

# Calcular a percentagem de referência
total_makes = df["three_point_makes"].sum()
total_attempts = df["three_point_attempts"].sum()

league_pct = total_makes / total_attempts

print(f"Percentagem de referência: {league_pct:.2%}")

# Regularização das percentagens
k = 100

df["adjusted_3p_pct"] = (
    df["three_point_makes"] + k * league_pct
) / (
    df["three_point_attempts"] + k
)

# Volume de lançamento por 36 minutos
df["three_pa_per36"] = (
    df["three_point_attempts"] / df["minutes"] * 36
)

# Evitar resultados pouco representativos
eligible = df[
    (df["minutes"] >= 500) &
    (df["three_point_attempts"] >= 50)
].copy()

# Apresentar os melhores por percentagem ajustada
top_shooters = eligible.sort_values(
    "adjusted_3p_pct",
    ascending=False
)

print("\nTop 15 — Percentagem de triplos ajustada:")
print(top_shooters[[
    "player_name",
    "team",
    "three_point_pct",
    "three_point_attempts",
    "three_pa_per36",
    "adjusted_3p_pct"
]].head(15).to_string(index=False))

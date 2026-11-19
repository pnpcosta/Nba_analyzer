import pandas as pd

df = pd.read_csv("data/raw/players_2025_26.csv")

eligible = df[df["minutes"] >= 500].copy()

columns = [
    "assists_pg",
    "ast_pct",
    "turnovers",
    "tov_pct",
    "usage_rate",
    "minutes"
]

print("Jogadores elegíveis:", len(eligible))

print("\nDistribuição das estatísticas:")
print(eligible[columns].describe())

print("\nTop 15 por AST%:")
print(
    eligible.sort_values("ast_pct", ascending=False)[
        ["player_name", "assists_pg", "ast_pct",
         "tov_pct", "usage_rate"]
    ].head(15).round(3).to_string(index=False)
)


eligible["assists_per36"] = (
    eligible["assists"] / eligible["minutes"] * 36
)

eligible["ast_to_tov"] = (
    eligible["assists"]
    / eligible["turnovers"].replace(0, float("nan"))
)

metrics = [
    "assists_pg",
    "assists_per36",
    "ast_pct",
    "ast_to_tov",
    "tov_pct",
    "usage_rate"
]

print("\nCorrelação entre métricas:")
print(eligible[metrics].corr().round(3))

# Assistências por 36 minutos
eligible["assists_per36"] = (
    eligible["assists"] / eligible["minutes"] * 36
)

# Relação assistências / turnovers
eligible["ast_to_tov"] = (
    eligible["assists"]
    / eligible["turnovers"].replace(0, float("nan"))
)

print("\nTop 15 — Assists per 36 minutes:")
print(
    eligible.sort_values(
        "assists_per36", ascending=False
    )[[
        "player_name",
        "assists_per36",
        "ast_pct",
        "ast_to_tov"
    ]].head(15).round(3).to_string(index=False)
)
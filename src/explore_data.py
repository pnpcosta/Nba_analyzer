
import pandas as pd

# 1. Ler o dataset
df = pd.read_csv("data/raw/players_2025_26.csv")

# 2. Verificar dimensões
print("Número de registos:", len(df))
print("Número de colunas:", len(df.columns))

# 3. Mostrar as colunas
print("\nColunas disponíveis:")
print(df.columns.tolist())

# 4. Mostrar os primeiros jogadores
print("\nPrimeiros 5 jogadores:")
print(df[[
    "player_name",
    "team",
    "age",
    "points_pg",
    "three_point_pct",
    "games_played"
]].head())

# 5. Verificar valores em falta
print("\nValores em falta por coluna:")
print(df.isnull().sum())


# 6. Contar jogadores únicos
print("\nJogadores únicos:")
print(df["player_name"].nunique())

# 7. Procurar jogadores repetidos
duplicados = df[
    df.duplicated(subset=["player_name"], keep=False)
]

print("\nRegistos com nomes repetidos:")
print(duplicados[
    ["player_name", "team", "games_played"]
].sort_values("player_name").head(20))

# 8. Analisar jogadores sem posição
print("\nJogadores sem posição:")
print(df[df["position"].isna()][
    ["player_name", "team", "games_played"]
].head(15))

# 9. Estatísticas gerais
print("\nResumo estatístico:")
print(df[[
    "points_pg",
    "three_point_pct",
    "three_point_attempts",
    "ts_pct",
    "minutes"
]].describe())


import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("data/raw/players_2025_26.csv")

# Calcular a percentagem ajustada
league_pct = (
    df["three_point_makes"].sum()
    / df["three_point_attempts"].sum()
)

k = 100

df["adjusted_3p_pct"] = (
    df["three_point_makes"] + k * league_pct
) / (df["three_point_attempts"] + k)

# Calcular o volume por 36 minutos
df["three_pa_per36"] = (
    df["three_point_attempts"] / df["minutes"] * 36
)

# Selecionar uma amostra de referência
eligible = df[
    (df["minutes"] >= 500) &
    (df["three_point_attempts"] >= 50)
].copy()

print("Jogadores elegíveis:", len(eligible))

# Distribuição da eficiência
plt.hist(eligible["adjusted_3p_pct"], bins=25)
plt.xlabel("Adjusted 3P%")
plt.ylabel("Number of players")
plt.title("Distribution of Adjusted 3P%")
plt.show()

# Distribuição do volume
plt.hist(eligible["three_pa_per36"], bins=25)
plt.xlabel("3PA per 36 minutes")
plt.ylabel("Number of players")
plt.title("Distribution of Shooting Volume")
plt.show()

# Resumo estatístico
print("\nEfficiency:")
print(eligible["adjusted_3p_pct"].describe())

print("\nVolume:")
print(eligible["three_pa_per36"].describe())

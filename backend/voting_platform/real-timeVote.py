from collections import Counter

# Exemple de données : liste des votes
votes = [
    "Nominee A", "Nominee B", "Nominee A", "Nominee C",
    "Nominee B", "Nominee A", "Nominee C", "Nominee C",
    "Nominee A", "Nominee B"
]

# Utilisation de Counter pour compter les votes
vote_count = Counter(votes)

# Affichage des résultats
print("Résultats du vote :")
for nominee, count in vote_count.items():
    print(f"{nominee}: {count} votes")

# Trouver le gagnant
winner = vote_count.most_common(1)[0]
print(f"\nLe gagnant est {winner[0]} avec {winner[1]} votes !")
import pandas as pd
import json

# Nom exact de ton fichier
fichier_excel = 'Liste compétences - JDR.xlsx'

# Lecture du fichier Excel
df = pd.read_excel(fichier_excel, sheet_name='Feuille 1')

# Nettoyage : Remplir les valeurs vides (les cellules fusionnées dans Excel)
df['Compétence'] = df['Compétence'].ffill()
df['Statistiques concernées'] = df['Statistiques concernées'].ffill()

competences = {}

for _, row in df.iterrows():
    nom = row['Compétence']
    niveau = str(row['Niveaux'])
    
    # Création de la structure sous forme de dictionnaire
    if nom not in competences:
        competences[nom] = {
            "nom": nom,
            "stats": row['Statistiques concernées'],
            "niveaux": {}
        }
    
    # On gère les cellules vides avec pd.notna() pour éviter les erreurs
    competences[nom]["niveaux"][niveau] = {
        "cout": int(row['Coûts']) if pd.notna(row['Coûts']) else 0,
        "description": row['Actions'] if pd.notna(row['Actions']) else "",
        "bonus": int(row['Bonus']) if pd.notna(row['Bonus']) else 0,
        "malus": int(row['Malus']) if pd.notna(row['Malus']) else 0
    }

# Sauvegarde en JSON (commencera par '{')
with open('competences.json', 'w', encoding='utf-8') as f:
    json.dump(competences, f, ensure_ascii=False, indent=4)

print("Fichier 'competences.json' généré avec succès en format dictionnaire.")
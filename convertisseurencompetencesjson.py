import pandas as pd
import json

# Le nom exact de ton fichier avec l'extension .xlsx
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
    
    if nom not in competences:
        competences[nom] = {
            "nom": nom,
            "stats": row['Statistiques concernées'],
            "niveaux": {}
        }
    
    # On gère les cellules vides avec fillna pour éviter les erreurs
    competences[nom]["niveaux"][niveau] = {
        "cout": row['Coûts'],
        "description": row['Actions'] if pd.notna(row['Actions']) else "",
        "bonus": row['Bonus'] if pd.notna(row['Bonus']) else 0,
        "malus": row['Malus'] if pd.notna(row['Malus']) else 0
    }

# Sauvegarde en JSON
with open('competences.json', 'w', encoding='utf-8') as f:
    json.dump(list(competences.values()), f, ensure_ascii=False, indent=2)

print("Succès ! 'competences.json' a été généré depuis ton fichier Excel.")
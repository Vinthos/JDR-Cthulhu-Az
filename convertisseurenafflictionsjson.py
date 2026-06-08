import pandas as pd
import json

# Le nom de ton fichier
fichier_excel = 'Liste Afflictions.xlsx'

# 1. Lecture du fichier Excel
df = pd.read_excel(fichier_excel, sheet_name='Feuille 1')

# 2. Nettoyage : Propager le nom de l'affliction sur les lignes vides
df['Affliction'] = df['Affliction'].ffill()

# On initialise un dictionnaire (comme pour tes compétences)
afflictions = {}

for _, row in df.iterrows():
    nom = row['Affliction']
    stade = str(row['Stade'])
    
    # Initialisation de l'objet dans le dictionnaire
    if nom not in afflictions:
        afflictions[nom] = {
            "nom": nom,
            "definition": row['Définition'] if pd.notna(row['Définition']) else "",
            "niveaux": {}
        }
    
    # Remplissage des données par stade
    afflictions[nom]["niveaux"][stade] = {
        "condition": row['Condition'] if pd.notna(row['Condition']) else "",
        "cout_ps": int(row['Coût (PS)']) if pd.notna(row['Coût (PS)']) else 0,
        "gain_pc": int(row['Gain (PC)']) if pd.notna(row['Gain (PC)']) else 0,
        "bonus_comp": int(row['Compétence supplémentaire (total max 5)']) if pd.notna(row['Compétence supplémentaire (total max 5)']) else 0
    }

# 3. Sauvegarde en JSON (ce format commencera par { "Addict aux médicaments": { ... } })
with open('afflictions.json', 'w', encoding='utf-8') as f:
    json.dump(afflictions, f, ensure_ascii=False, indent=4)

print("Fichier 'afflictions.json' généré sous forme de dictionnaire.")
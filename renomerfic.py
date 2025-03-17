import os

# Chemin du dossier
dossier = r"C:\Users\thinkpad\Desktop\Dossier db"

# Vérifier si le dossier existe
if not os.path.exists(dossier):
    print("Le dossier spécifié n'existe pas.")
    exit()

# Lister tous les fichiers dans le dossier
fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]

# Renommer les fichiers
for i, fichier in enumerate(fichiers, start=1):
    # Ancien chemin complet
    ancien_chemin = os.path.join(dossier, fichier)
    
    # Nouveau nom de fichier
    nouveau_nom = f"fichier{i}{os.path.splitext(fichier)[1]}"  # Conserve l'extension
    nouveau_chemin = os.path.join(dossier, nouveau_nom)
    
    # Renommer le fichier
    os.rename(ancien_chemin, nouveau_chemin)
    print(f"Renommé : {fichier} -> {nouveau_nom}")

print("Renommage terminé.")
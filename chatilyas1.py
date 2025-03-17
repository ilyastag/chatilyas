import tkinter as tk
from tkinter import scrolledtext

def submit_info():
    # Récupérer les entrées de l'utilisateur
    code = code_entry.get("1.0", tk.END).strip()
    description = description_entry.get().strip()
    errors = errors_entry.get().strip()
    expected_output = output_entry.get().strip()
    technical_specs = specs_entry.get().strip()
    performance_goals = goals_entry.get().strip()

    # Traitement (vous pourriez appeler ici votre API ou votre logique de chatbot)
    print("Code initial:", code)
    print("Description du problème:", description)
    print("Informations sur les erreurs:", errors)
    print("Exemple de sortie attendue:", expected_output)
    print("Spécifications techniques:", technical_specs)
    print("Objectifs de performance:", performance_goals)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Chatbot de Correction et Génération de Code")
root.geometry("700x600")
root.configure(bg="#f0f0f0")

# Créer des labels et des zones de texte
def create_label(text, row):
    label = tk.Label(root, text=text, bg="#f0f0f0", fg="#4b0082", font=("Helvetica", 12, "bold"))
    label.grid(row=row, column=0, sticky='w', padx=10, pady=5)

create_label("Code initial:", 0)
code_entry = scrolledtext.ScrolledText(root, width=70, height=10)
code_entry.grid(row=1, column=0, padx=10, pady=5)

create_label("Description du problème:", 2)
description_entry = tk.Entry(root, width=70)
description_entry.grid(row=3, column=0, padx=10, pady=5)

create_label("Informations sur les erreurs:", 4)
errors_entry = tk.Entry(root, width=70)
errors_entry.grid(row=5, column=0, padx=10, pady=5)

create_label("Exemple de sortie attendue:", 6)
output_entry = tk.Entry(root, width=70)
output_entry.grid(row=7, column=0, padx=10, pady=5)

create_label("Spécifications techniques:", 8)
specs_entry = tk.Entry(root, width=70)
specs_entry.grid(row=9, column=0, padx=10, pady=5)

create_label("Objectifs de performance ou de qualité:", 10)
goals_entry = tk.Entry(root, width=70)
goals_entry.grid(row=11, column=0, padx=10, pady=5)

# Bouton de soumission
submit_button = tk.Button(root, text="Soumettre", command=submit_info, bg="#4b0082", fg="white", font=("Helvetica", 12))
submit_button.grid(row=12, column=0, pady=20)

# Lancer la boucle principale
root.mainloop()
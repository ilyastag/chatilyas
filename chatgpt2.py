import tkinter as tk
from tkinter import scrolledtext
import requests

API_KEY = "4c3e9d45150059bf52a3ea96d2190ba05406a32cbe943056d261fdcc68f35f2f"  # Remplace par ta clé Together.ai
API_URL = "https://api.together.xyz/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def submit_info():
    # Récupérer les entrées de l'utilisateur
    code = code_entry.get("1.0", tk.END).strip()
    description = description_entry.get().strip()
    errors = errors_entry.get().strip()
    expected_output = output_entry.get().strip()
    technical_specs = specs_entry.get().strip()
    performance_goals = goals_entry.get().strip()

    # Préparer le message pour l'API
    user_input = f"Code: {code}\nDescription: {description}\nErreurs: {errors}\nSortie attendue: {expected_output}\nSpécifications: {technical_specs}\nObjectifs: {performance_goals}"

    # Appeler l'API
    data = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 1.00
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        output_text.delete("1.0", tk.END)  # Effacer le texte précédent
        output_text.insert(tk.END, result["choices"][0]["message"]["content"])  # Afficher le résultat dans le champ de texte
    else:
        output_text.delete("1.0", tk.END)  # Effacer le texte précédent
        output_text.insert(tk.END, "❌ Erreur : " + str(response.json()))  # Afficher l'erreur

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

# Label pour afficher le résultat
create_label("Résultat de la correction :", 12)
output_text = scrolledtext.ScrolledText(root, width=70, height=10)
output_text.grid(row=13, column=0, padx=10, pady=5)

# Bouton de soumission
submit_button = tk.Button(root, text="Soumettre", command=submit_info, bg="#4b0082", fg="white", font=("Helvetica", 12))
submit_button.grid(row=14, column=0, pady=20)

# Lancer la boucle principale
root.mainloop()
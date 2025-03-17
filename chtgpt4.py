import tkinter as tk
from tkinter import scrolledtext
import requests
from PIL import Image, ImageTk

API_KEY = "4c3e9d45150059bf52a3ea96d2190ba05406a32cbe943056d261fdcc68f35f2f "  # Remplace par ta clé Together.ai
API_URL = "https://api.together.xyz/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def submit_info():
    code = code_entry.get("1.0", tk.END).strip()
    errors = errors_entry.get("1.0", tk.END).strip()
    technical_specs = specs_entry.get("1.0", tk.END).strip()
    
    user_input = f"Code: {code}\nErreurs: {errors}\nSpécifications: {technical_specs}"
    
    data = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 0.7
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    output_text.delete("1.0", tk.END)
    if response.status_code == 200:
        result = response.json()
        output_text.insert(tk.END, result["choices"][0]["message"]["content"])
    else:
        output_text.insert(tk.END, "❌ Erreur : " + str(response.json()))

# Création de la fenêtre principale
root = tk.Tk()
root.title("TagChat - AI Code Assistant")
root.geometry("900x700")
root.configure(bg="#f7f7f7")  # Fond de page gris clair

# Cadre de gauche
left_frame = tk.Frame(root, bg="#34C759", width=300, height=700)  # Vert clair
left_frame.pack(side=tk.LEFT, fill=tk.Y)

# Sections de saisie
def create_section(parent, title):
    frame = tk.Frame(parent, bg="#8BC34A", bd=2, relief="groove")  # Vert moyen
    frame.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
    
    label = tk.Label(frame, text=title, bg="#8BC34A", font=("Helvetica", 12, "bold"), fg="#ffffff")  # Texte blanc
    label.pack(anchor='w', padx=5, pady=5)
    
    text_box = scrolledtext.ScrolledText(frame, width=30, height=5, bg="#f7f7f7", fg="#333333")  # Fond gris clair et texte gris foncé
    text_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
    
    return text_box

code_entry = create_section(left_frame, "Code initial :")
specs_entry = create_section(left_frame, "Spécification technique :")
errors_entry = create_section(left_frame, "INFORMATION SUR ERREUR :")

# Boutons
btn_frame = tk.Frame(left_frame, bg="#34C759")  # Vert clair
btn_frame.pack(fill=tk.X)

tk.Button(btn_frame, text="New Chat", command=submit_info, bg="#3e8e41", fg="white").pack(fill=tk.X, pady=5)  # Vert foncé
tk.Button(btn_frame, text="Recent Chats", bg="#3e8e41", fg="white").pack(fill=tk.X, pady=5)  # Vert foncé

# Zone de chat principale
chat_frame = tk.Frame(root, bg="#ffffff")
chat_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

output_text = scrolledtext.ScrolledText(chat_frame, width=90, height=10, bg="#f7f7f7", fg="#333333")  # Fond gris clair et texte gris foncé
output_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Champ de saisie pour le chat
entry_frame = tk.Frame(chat_frame, bg="#8BC34A")  # Vert moyen
entry_frame.pack(fill=tk.X, padx=10, pady=10)

entry_box = tk.Entry(entry_frame, width=80, bg="#f7f7f7", fg="#333333")  # Fond gris clair et texte gris foncé
entry_box.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

tk.Button(entry_frame, text="Send", command=submit_info, bg="#3e8e41", fg="white").pack(side=tk.RIGHT, padx=5)  # Vert foncé

root.mainloop()
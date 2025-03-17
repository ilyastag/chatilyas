import tkinter as tk
from tkinter import scrolledtext
import requests
from PIL import Image, ImageTk

API_KEY = "api key"  # Remplace par ta clé Together.ai
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
root.configure(bg="#f0f0f0")

# Cadre de gauche
left_frame = tk.Frame(root, bg="#000000", width=300, height=700)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

# Sections de saisie
def create_section(parent, title):
    frame = tk.Frame(parent, bg="#e0f7fa", bd=2, relief="groove")
    frame.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
    
    label = tk.Label(frame, text=title, bg="#e0f7fa", font=("Helvetica", 12, "bold"))
    label.pack(anchor='w', padx=5, pady=5)
    
    text_box = scrolledtext.ScrolledText(frame, width=30, height=5)
    text_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
    
    return text_box

code_entry = create_section(left_frame, "Code initial :")
specs_entry = create_section(left_frame, "Spécification technique :")
errors_entry = create_section(left_frame, "INFORMATION SUR ERREUR :")

# Boutons
btn_frame = tk.Frame(left_frame, bg="#000000")
btn_frame.pack(fill=tk.X)

tk.Button(btn_frame, text="New Chat", command=submit_info, bg="#4b0082", fg="white").pack(fill=tk.X, pady=5)
tk.Button(btn_frame, text="Recent Chats", bg="#4b0082", fg="white").pack(fill=tk.X, pady=5)

# Zone de chat principale
chat_frame = tk.Frame(root, bg="#ffffff")
chat_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

output_text = scrolledtext.ScrolledText(chat_frame, width=90, height=10)
output_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Champ de saisie pour le chat
entry_frame = tk.Frame(chat_frame, bg="#e0f7fa")
entry_frame.pack(fill=tk.X, padx=10, pady=10)

entry_box = tk.Entry(entry_frame, width=80)
entry_box.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

tk.Button(entry_frame, text="Send", command=submit_info, bg="#4b0082", fg="white").pack(side=tk.RIGHT, padx=5)

root.mainloop()

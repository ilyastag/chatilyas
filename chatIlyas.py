import requests

API_KEY = "Api key"  # Remplace par ta clé Together.ai
API_URL = "https://api.together.xyz/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

while True:  # 🔁 Boucle infinie pour interagir avec l'IA
    user_input = input("👤 Toi : ")  # Demander un texte à l'utilisateur
    
    if user_input.lower() in ["exit", "quit", "bye"]:  # Condition pour quitter
        print("👋 Fin du chat.")
        break  

    data = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",  
        "messages": [{"role": "user", "content": user_input}],  # ✅ Dynamique
        "temperature": 0.9  # ✅ Augmenté pour plus de diversité
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print("🤖 IA :", result["choices"][0]["message"]["content"])
    else:
        print("❌ Erreur :", response.json())

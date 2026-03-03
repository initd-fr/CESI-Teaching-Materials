# Importation des modules nécessaires
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import json

# Initialisation de l'API
app = FastAPI()

# Modèle Pydantic pour les données de la partie
class GameResult(BaseModel):
    player_name: str
    score: int

# Fonction pour enregistrer un résultat de partie dans un fichier JSON
def save_result_to_file(result):
    try:
        with open("data.json", "a") as file: # Ouverture du fichier en mode ajout
            json.dump(result.dict(), file) # Écriture du résultat dans le fichier
            file.write("\n") # Ajout d'un retour à la ligne
    except Exception as e: # Si une erreur se produit
        print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {str(e)}")


# Endpoint pour tester le fonctionnement de l'API 
@app.get("/api-info/")
async def get_api_info():
    try:
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        port = 8000 
        return {
            "hostname": hostname,
            "ip_address": ip_address,
            "port": port
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erreur lors de la récupération des informations de l'API")

# Endpoint pour enregistrer les résultats de la partie
@app.post("/save_result/")
async def save_game_result(result: GameResult):
    try:
        save_result_to_file(result)
        return {"message": "Résultat de la partie enregistré avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erreur lors de l'enregistrement du résultat de la partie")

# Endpoint pour récupérer tous les résultats des parties
@app.get("/get_results/")
async def get_game_results():
    try:
        results = []
        with open("data.json", "r") as file:
            for line in file:
                result = json.loads(line)
                results.append(result)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erreur lors de la récupération des résultats des parties")
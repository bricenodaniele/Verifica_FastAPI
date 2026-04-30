from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from github import Github

app = FastAPI()

# --- CONFIGURAZIONE GITHUB ---
GITHUB_TOKEN = "IL_TUO_TOKEN"
REPO_NAME = "tuo_username/nome_repo"
FILE_PATH = "IMC - Foglio1.csv" # Nome del file nella tua cartella GitHub

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/") 
def home():
    return FileResponse('static/home.html')

def salva_su_github(p, h, imc):
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
        # Formattazione riga basata sul tuo file 
        nuova_riga = f"{p},{h},{imc}\n"
        
        try:
            contents = repo.get_contents(FILE_PATH)
            nuovo_contenuto = contents.decoded_content.decode() + nuova_riga
            repo.update_file(FILE_PATH, "Nuovo inserimento IMC", nuovo_contenuto, contents.sha)
        except:
            # Crea il file se non esiste con le tue intestazioni 
            header = "peso,altezza,IMC\n"
            repo.create_file(FILE_PATH, "Inizializzazione file", header + nuova_riga)
    except Exception as e:
        print(f"Errore durante l'invio a GitHub: {e}")

@app.post("/imc2")
def calcola_e_invia(peso: float = Form(...), altezza: float = Form(...)):
    risultato = peso / (altezza ** 2)
    risultato_formattato = round(risultato, 2)
    return {"risultato": risultato_formattato}
    # Invia i dati a GitHub
    salva_su_github(peso, altezza, risultato_formattato)
    
    return {"risultato": risultato_formattato}
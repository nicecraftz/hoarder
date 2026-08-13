# 📦 Hoarder

> **Un sistema integrato di CDN e CMS basato su Python e FastAPI, progettato per la gestione e la distribuzione di materiale in rete**

---

## Cos'è Hoarder?

**Hoarder** è la spina dorsale di **Onlycam**, il portale dedicato alla condivisione di risorse, dispense e materiali didattici universitari. 

Nato con scopo didattico per affinare le mie competenze nell'ambito del **Full-Stack Software Development**, Hoarder unisce un'architettura di **Content Delivery Network (CDN)** per l'erogazione rapida ed efficiente di asset di grandi dimensioni a un **Content Management System (CMS)** flessibile per la categorizzazione e organizzazione dei contenuti.

---

## Tech Stack & Architettura

Il backend è interamente sviluppato in **Python** sfruttando l'ecosistema moderno offerto da **FastAPI**

* **Core Framework:** Python 3.10+ / FastAPI
* **Validazione Dati & Impostazioni:** Pydantic
* **Gestione Asset (CDN):** Servizio per upload, caching e streaming dei file (PDF, immagini, slide)
* **CMS Layer:** API RESTful per la gestione di corsi, materie, professori e metadati dei file
* **Documentazione API:** OpenAPI (Swagger UI) / ReDoc integrati direttamente tramite FastAPI

---

## Obiettivi Didattici

Questo progetto rappresenta un campo di prova per affrontare sfide concrete di ingegneria del software:

* **Sviluppo Asincrono con Python:** Sfruttare al massimo `async/await` in FastAPI per gestire I/O concorrente (stream di file e query al database).
* **Progettazione di API Pulite:** Design RESTful rigoroso, tipizzazione forte e validazione completa dei payload.
* **Best Practice Full-Stack:** Applicazione dei principi di clean architecture, separazione delle responsabilità e manutenzione del codice.

---

## Direttive sull'Utilizzo dell'Intelligenza Artificiale

In questo repository si applica una **politica rigorosa** sull'uso dell'IA generativa:

1. **Nessun Codice Generato:** L'intelligenza artificiale **non scriverà mai codice** per questo progetto. Ogni riga di codice presente è ideata e scritta a mano.
2. **Supporto Didattico e Documentazione:** L'IA viene impiegata esclusivamente come mentor e strumento di confronto per:
   * Revisione teorica del codice (code review, identificazione di code smell e colli di bottiglia).
   * Spiegazione di pattern architetturali, gestione dell'asincronia in Python e approcci alternativi.
   * Generazione e rifinitura della documentazione di progetto.

---

## Funzionalità Previste (Roadmap)

- [ ] **Core CDN:** Upload, memorizzazione e streaming di file didattici.
- [ ] **Core CMS:** Endpoints di amministrazione per la moderazione, indicizzazione e associazione dei file ai corsi.
- [ ] **Autenticazione & Permessi:** Autenticazione sicura (JWT / OAuth2) e gestione dei ruoli.
- [ ] **Caching & Performance:** Integrazione di middleware di caching per le rotte e gli asset più richiesti.
- [ ] **Documentazione API:** Specifica OpenAPI completa ed esempi di richiesta/risposta.

---

## Setup Locale e Sviluppo

```bash
# Clona il repository
git clone [https://github.com/tuo-username/hoarder.git](https://github.com/tuo-username/hoarder.git)
cd hoarder

# Crea e attiva l'ambiente virtuale
python -m venv .venv
source .venv/bin/activate  # Su Windows: .venv\Scripts\activate

# Installa le dipendenze
pip install -r requirements.txt

# Avvia il server di sviluppo
uvicorn app.main:app --reload
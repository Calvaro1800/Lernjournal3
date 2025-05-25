# 📊 Portfolio Optimizer — alvarchr — MDM FS2025

Ein Projekt gemacht für das Modul **Model Deployment & Maintenance** an der ZHAW (Frühsemester 2025).  
👤 Name: alvarchr  
📘 Modul: MDM FS2025  
🎓 Betreuer: Prof. Adrian Moser

---

Willkommen zu meinem Projekt **Portfolio Optimizer mit KI**, das ich im Rahmen des Moduls *Model Deployment & Maintenance (MDM)* an der ZHAW entwickelt habe.  
Dieses Projekt war eine echte Reise – mit vielen Herausforderungen, Frustmomenten, Lerneffekten und Stolz am Ende!

---

## 🎯 Ziel des Projekts

Ich wollte ein echtes **Finanz-Tool mit KI** bauen, das:

- echte **Aktien-Daten** holt und automatisch analysiert
- die Performance einzelner Titel prognostiziert
- das Portfolio bewertet (Sharpe Ratio)
- und sogar **Finanzempfehlungen im Stil eines Beraters** gibt

Mein Ziel war, eine Web-App zu bauen, die technisch anspruchsvoll, aber für Nutzer einfach zu bedienen ist – komplett automatisiert, interaktiv und mit künstlicher Intelligenz.

---

## 🧩 Funktionen (Übersicht)

| Kategorie                | Funktion                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| 📈 Scraping              | Holt automatisch Top Gainers von Yahoo Finance                           |
| 📰 News & Sentiment      | Scrapt Finanznachrichten + Sentimentanalyse mit Transformers-Modell      |
| 📉 Regression IA         | Regressionsmodell prognostiziert Performance von Aktien                  |
| 🧠 LLM Finanzberater     | GPT-2 gibt Empfehlungen wie ein virtueller Berater (Otto)                |
| 📊 Sharpe Ratio          | Bewertet Portfolio-Risiko vs. Rendite                                    |
| 🧑‍💻 Flask UI            | Web-App mit Suche, Buy/Sell, Charts, Upload & LLM-Fragen                  |
| 📅 Termin vereinbaren    | Berater wählen (Ray Dalio, Gekko…) mit Bild + Bestätigungsnachricht     |
| ⏰ Automatisierung        | CRON-Scheduling + GitHub Actions automatisieren Daten & Analyse         |
| 🧪 Unit Tests            | Testabdeckung für Modelle, LLM, Scraper und Sentiment                   |
| 🐳 Docker                | Lokales Docker-Image verfügbar (Azure-Deployment in Arbeit)             |

---

## 💥 Herausforderungen (technisch & persönlich)

Ich komme ursprünglich **nicht aus dem Python- oder DevOps-Bereich**.  
Deshalb war dieses Projekt für mich eine doppelte Herausforderung.

### 🔹 MongoDB
- IP-Ranges, DNS-Probleme, SSL Errors, `tlsAllowInvalidCertificates` – es war ein harter Einstieg
- Aber am Ende konnte ich über Compass, `pymongo` und `.env` alles stabil verbinden
<img width="946" alt="Screenshot 2025-05-25 at 23 15 22" src="https://github.com/user-attachments/assets/b3b6738c-ea70-49e7-9889-eb5450f1dfdb" />

### 🔹 Scraping
- Playwright hat anfangs nicht funktioniert → ich bin auf `requests + BeautifulSoup` umgestiegen
- Yahoo Finance ändert oft die HTML-Struktur → ich musste regelmäßig Debuggen
- Duplikate, Timeout-Fehler, Unicode-Fehler… ich hab alles gesehen

### 🔹 Modelle
- Ich musste lernen, wie man `transformers`, `sklearn` und lokale Modelle integriert
- Regression + Sentiment + GPT-2 mussten miteinander kommunizieren
- Ich habe alle Modelle **manuell getestet** und `test_models.py` geschrieben

### 🔹 Flask & Frontend
- Ich hatte keine Erfahrung mit Flask oder Jinja2
- Trotzdem habe ich eine App mit **Charts, Pie Diagrammen, Autocomplete und Forms** gebaut
- Ich habe Bootstrap, Chart.js und JS-Funktionen kombiniert – es war intensiv

Prototype:
  <img width="327" alt="Screenshot 2025-05-25 at 23 15 01" src="https://github.com/user-attachments/assets/2af5edb3-d786-46f1-9a58-b572df0d2f47" />
End Version:
<img width="769" alt="Screenshot 2025-05-25 at 23 21 07" src="https://github.com/user-attachments/assets/61e03d58-6d96-4d27-a178-d49f1fc68aa5" />

### 🔹 GitHub Actions
- Ich habe YAML-Dateien selbst geschrieben für automatisches Scraping, Build & Test
- Debugging war schwer, vor allem mit Secrets (Mongo URI, HF Token)
<img width="725" alt="Screenshot 2025-05-25 at 23 23 17" src="https://github.com/user-attachments/assets/f45ff99e-a12c-4344-8685-5a2e853201bc" />

### 🔹 Docker & macOS Probleme
- Nach einem **macOS Sequoia Update** konnte ich Docker Desktop **nicht mehr öffnen**
- Ich habe mit **Colima** gearbeitet, um mein Projekt trotzdem containerisieren zu können
- Ich konnte mein Image lokal bauen & ausführen (`port 5151`)
- Das **Azure Deployment** war leider am Tag des Screencasts noch nicht abgeschlossen
![Screenshot 2025-05-25 at 23 29 09](https://github.com/user-attachments/assets/2e3a7fe7-ef62-4a0e-887f-ed99f64f18c8)

---

## 🧠 Meine Learnings

Ich habe in diesem Projekt gelernt…

- wie man **Daten automatisiert sammelt und speichert**
- wie man **Modelle trainiert, verbindet und testet**
- wie man eine **echte Web-App mit Flask und MongoDB** baut
- wie man **Fehler systematisch debuggt**
- und vor allem: **dran bleiben**, auch wenn es schwer wird

Ich bin stolz, dass ich dieses Projekt mit null Vorwissen zu einem funktionierenden Prototypen gebracht habe.

---

## 🧪 Tests & Qualität

Ich habe eigene Tests geschrieben, z.B.:

- `test_models.py` → Sharpe Ratio, Klassifikation, Regression  
- `test_sentiment.py` → Korrektheit der Sentimentanalyse  
- `test_ask_model.py` → Antworten des LLM richtig formatiert  
- `test_update_all_stocks.py` → Kontrolle des Scraping-Outputs

Zusätzlich:

- `debug_llm.py` → zum manuellen Testen von Otto (GPT-2)  
- `compute_avg_sentiment.py` → berechnet täglichen Sentiment-Schnitt aus MongoDB  

---

## 📂 Projektstruktur (technisch)

```bash
projekt1-python/
│
├── app.py                     # Hauptserver (Flask)
├── core/                      # ML: regression_model.py, llm_advisor.py, sharpe_utils.py
├── static/, templates/        # Frontend: HTML, JS, CSS, Charts
├── update_gainers.py          # Scraping der Top Gainers
├── update_news.py             # Scraping der Finanznews
├── analyze_sentiment.py       # Sentimentanalyse (lokal)
├── compute_avg_sentiment.py   # Sentiment-Mittelwert aggregieren
├── uploads/                   # CSV-Upload Ordner
├── logs/, models/, images/    # Lokale Modelle, Logs, Beraterbilder
├── Dockerfile, .env           # Container + Secrets
└── requirements.txt           # Python-Abhängigkeiten


🚀 Deployment & Automation
Ich habe GitHub Actions erstellt, um:

Scraping zu automatisieren (2x täglich: 10:00 und 18:00)

Analyse-Skripte auszuführen (Sentiment, avg Score, etc.)

Tests automatisch zu starten (pytest)

Für Docker:

Ich habe ein funktionierendes Image gebaut (Dockerfile)

Das läuft lokal mit Port 5151

Das Azure Deployment ist vorbereitet (Secrets gesetzt), aber noch in Arbeit


🎓 Fazit
Dieses Projekt war mehr als nur ein Uni-Projekt.
Es war mein Einstieg in die Welt von Python, KI, Webentwicklung und DevOps.

Ich habe alles selbst gebaut – mit Unterstützung von ChatGPT, viel Trial & Error,
und vor allem: mit viel Geduld.

Ich bin stolz auf mein Ergebnis.
Und wer weiß – vielleicht wird Otto bald mein echter Berater 😉

Merci fürs Lesen – und danke an alle, die mich unterstützt haben.
Falls du dein Portfolio optimieren willst… frag einfach mein Modell 😄

## Persönliche Reflexion
Ich habe bei der Erstellung meines Projekts den Fehler gemacht, dass ich nie die Schritte des Einsatzes meines Projekts und die Ausgaben meines Templates in VSC für das Docking, den Einsatz usw. fotografiert habe. Dies war eine Strafe für mein Lernjournal. 

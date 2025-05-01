Klar! Hier ist dein vollständiger und sauber strukturierter README.md-Text als ein einzelner Markdown-Block – direkt bereit zum Einfügen in dein Repository:

⸻



# Lernjournal 1 Python

## Repository und Library

| | Bitte ausfüllen |
| -------- | ------- |
| Repository (URL)  | https://github.com/alvarchr/lernjournal1-python |
| Kurze Beschreibung der App-Funktion | Eine Web-App, die dem Nutzer nach Eingabe seines Namens eine zufällige motivierende Nachricht anzeigt. |
| Verwendete Library aus PyPi (Name) | Flask |
| Verwendete Library aus PyPi (URL) | https://pypi.org/project/Flask/ |
| Weitere Libraries | gunicorn |
| URL zur Web-App | http://motivationgenerator.azurewebsites.net |

## App, Funktionalität

* [✅] Die App verwendet **Flask**, um eine einfache Webseite bereitzustellen.
* [✅] Auf der Startseite kann der Nutzer seinen Namen eingeben.
* [✅] Nach dem Absenden wird zufällig eine **motivierende Nachricht** ausgewählt und personalisiert angezeigt.
* [✅] Die HTML-Oberfläche ist mit einem Template (`index.html`) gestaltet.
* [✅] Das Verhalten bei POST/GET wird im `app.py` korrekt gesteuert.

<img width="942" alt="Screenshot 2025-04-22 at 13 40 37" src="https://github.com/user-attachments/assets/555ab5fe-630d-4226-bae6-0e81956a3392" />

Dependency Management
	•	[✅] Die Datei requirements.txt enthält alle benötigten Abhängigkeiten:
	•	Flask
	•	gunicorn
	•	[✅] Die Installation erfolgt über:

pip install -r requirements.txt


	•	[✅] Die Anwendung kann lokal mit folgendem Befehl gestartet werden:

flask --app app run

<img width="1068" alt="Screenshot 2025-04-22 at 13 42 14" src="https://github.com/user-attachments/assets/cd88bd5e-adb4-4e4a-8c20-afb738880182" />

Deployment
	•	[✅] Die App wurde erfolgreich auf Azure App Service deployed.
	•	[✅] Deployment-Schritte:
	1.	Login via az login
	2.	Ressourcengruppe:

az group create --name mdm-gruppe --location westeurope

<img width="954" alt="Screenshot 2025-04-21 at 16 25 34" src="https://github.com/user-attachments/assets/4fe0a481-04b6-47ec-a4d6-abf8c0d4386f" />

	3.	App Service Plan:

az appservice plan create --name mdm-plan --resource-group mdm-gruppe --sku FREE --is-linux

<img width="1041" alt="Screenshot 2025-04-21 at 16 25 47" src="https://github.com/user-attachments/assets/ae101b89-48bf-4faa-86fb-cb2e1715cada" />

	4.	Webapp erstellen:

az webapp create --resource-group mdm-gruppe --plan mdm-plan --name MotivationGenerator --runtime "PYTHON|3.10"

<img width="1079" alt="Screenshot 2025-04-21 at 16 25 56" src="https://github.com/user-attachments/assets/4f2b873b-36b0-44f5-99e2-b05dc3ee3ab4" />

	5.	App als ZIP bereitstellen:

az webapp deploy --resource-group mdm-gruppe --name MotivationGenerator --src-path mon-app.zip --type zip

<img width="1020" alt="Screenshot 2025-04-22 at 14 00 25" src="https://github.com/user-attachments/assets/675726f2-fb07-493b-828d-6bdb62dcdc15" />


	6.	Startbefehl setzen:

az webapp config set --resource-group mdm-gruppe --name MotivationGenerator --startup-file "gunicorn --bind=0.0.0.0 lernjournal1-python.app:app"


	•	[✅] Live-Link zur App:
👉 http://motivationgenerator.azurewebsites.net

📸 Beispiel-Screenshot der Azure-CLI Deployment-Ausgabe:

![Azure Deployment Output](images/screenshot-deployment.png)

	•	[✅] Wichtige Erkenntnisse:
	•	Der Pfad im --startup-file muss exakt stimmen: lernjournal1-python.app:app
	•	Die Projektstruktur im ZIP muss korrekt sein (App-Root im Unterordner)
	•	Die Verwendung von gunicorn ist notwendig für Azure App Service (nicht flask run)

---

Wenn du möchtest, kann ich dir im Anschluss auch gleich das **Lernjournal** nach Bewertungsraster aufbereiten. Sag einfach Bescheid ✅

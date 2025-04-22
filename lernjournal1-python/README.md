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

📸 Beispiel-Screenshot der App im Browser:  
```markdown
![App im Browser](images/screenshot-app.png)

Dependency Management
	•	[✅] Die Datei requirements.txt enthält alle benötigten Abhängigkeiten:
	•	Flask
	•	gunicorn
	•	[✅] Die Installation erfolgt über:

pip install -r requirements.txt


	•	[✅] Die Anwendung kann lokal mit folgendem Befehl gestartet werden:

flask --app app run



📸 Beispiel-Terminalausgabe beim lokalen Start:

![Terminal Output - Local Run](images/screenshot-local-run.png)

Deployment
	•	[✅] Die App wurde erfolgreich auf Azure App Service deployed.
	•	[✅] Deployment-Schritte:
	1.	Login via az login
	2.	Ressourcengruppe:

az group create --name mdm-gruppe --location westeurope


	3.	App Service Plan:

az appservice plan create --name mdm-plan --resource-group mdm-gruppe --sku FREE --is-linux


	4.	Webapp erstellen:

az webapp create --resource-group mdm-gruppe --plan mdm-plan --name MotivationGenerator --runtime "PYTHON|3.10"


	5.	App als ZIP bereitstellen:

az webapp deploy --resource-group mdm-gruppe --name MotivationGenerator --src-path mon-app.zip --type zip


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
# Lernjournal 2 – Container

## Docker Web-Applikation

---

### Verwendete Docker Images

Die Web-Applikation basiert auf einem leichtgewichtigen Python-Container mit integriertem ONNX-Modell zur Bildklassifikation. Es wurden zwei Docker Images verwendet:

| Komponente        | Beschreibung                                                                                          |
|-------------------|-------------------------------------------------------------------------------------------------------|
| **Image 1**       | `python:3.13.0-slim` – Minimalistisches Python-Basisimage für schlanke ML-Anwendungen                |
| **Image 1 URL**   | [python:3.13.0-slim auf Docker Hub](https://hub.docker.com/_/python)                                  |
| **Image 2**       | `calvaro/car-color-classifier:latest` – Eigenes Image inkl. Flask-App und ONNX-Inferenz              |
| **Image 2 URL**   | [calvaro/car-color-classifier auf Docker Hub](https://hub.docker.com/r/calvaro/car-color-classifier) |
| **Docker Compose**| https://hub.docker.com/repository/docker/calvaro/car-color-classifier/general

---

### Dokumentation manuelles Deployment

#### 🛠 Erstellung des Dockerfiles

Ein eigenes `Dockerfile` wurde entwickelt, das:

- auf dem offiziellen Python Slim Image basiert
- systemnahe Pakete wie `libgl1` und `libglib2.0-0` installiert (wichtig für `cv2`)
- ONNX-Dateien (`EfficientNet-Lite4`) und Mapping-Dateien (`labels_map.txt`) in das Image kopiert
- über `flask run` die Anwendung in einem einfachen Webserver startet

<img width="1021" alt="Docker Build mit vollständigem Abhängigkeits-Download – ONNX-App ohne Cache erstellt" src="https://github.com/user-attachments/assets/4e7c7520-8fcf-478e-95af-aa8d6a236c7d" />

---

####  Build & Push des Containers

Der Container wurde lokal mit folgendem Befehl gebaut:

```bash
docker build -t calvaro/car-color-classifier:latest .

````
<img width="1216" alt="Kompletter Docker Build   mehrfacher Containertest der Bildklassifikations-App  " src="https://github.com/user-attachments/assets/567fd413-bb94-44b7-970a-731953c477cf" />



Anschließend wurde das Image auf Docker Hub veröffentlicht:

```bash
docker push calvaro/car-color-classifier:latest
```

<img width="920" alt="Docker Image Push – Upload der ONNX-App car-color-classifier auf Docker Hub  " src="https://github.com/user-attachments/assets/d5e904f0-2e08-4cb1-86f0-a75c6a1c7336" />

![dockerhub](https://github.com/user-attachments/assets/2db9c573-9f97-4f73-82cf-0ef76b9704f2)


---

#### 🧪 Lokales Testing des Containers

Die lokale Ausführung erfolgte mit:

```bash
docker run --rm -p 5050:5000 calvaro/car-color-classifier:latest
```
<img width="1182" alt="Docker Run, Tag   Push – Lokales Testen und Hochladen der ONNX-App" src="https://github.com/user-attachments/assets/dda2f64c-f34a-4c88-b333-cc85d8c80cae" />

<img width="890" alt="Lokaler Zugriff erfolgreich – HTTP-Response-Validierung der ONNX-App  " src="https://github.com/user-attachments/assets/9f4a0dcb-20af-444d-ad8b-8f58e56b74e4" />

Der Webserver war dann unter `http://127.0.0.1:5050` erreichbar.


![Lokale ONNX-Web-App – Erfolgreich gestartet auf Port 5050](https://github.com/user-attachments/assets/dcf198b7-c725-43a6-8c7e-48665d971217)

```

---
```
---

### Variante und Repository

| Gewähltes Beispiel        | Auswahl                                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| onnx-sentiment-analysis   | Nein ❌                                                                                              |
| onnx-image-classification | Ja ✅                                                                                                |
| Repo URL Fork             | [GitHub – ONNX-Image-Classification Fork](https://github.com/Calvaro1800/onnx-image-classification) |
| Docker Hub URL            | [Docker Hub – calvaro/car-color-classifier](https://hub.docker.com/r/calvaro/car-color-classifier)  |

---

### Dokumentation lokales Deployment

Nach dem lokalen Build wurde die ONNX-Klassifikation getestet mit Beispielbildern:

* Mutlipla.png

Die Applikation funktioniert korrekt und gibt Vorhersagen zurück.

<img width="816" alt="Screenshot 2025-05-25 at 21 26 55" src="https://github.com/user-attachments/assets/0b3a7c96-55d6-4a2c-aaef-db5b892aca01" />

---

### Dokumentation Deployment Azure Web App

Vorbereitung: Login & Subscription
Zuerst wurde die Anmeldung bei Azure über das CLI ausgeführt:

--az login

Die Auswahl der Subscription „Azure for Students“ (ZHAW) war erfolgreich.

<img width="1200" alt="Azure CLI Login – Verbindung zur ZHAW Subscription (Azure for Students) erfolgreich" src="https://github.com/user-attachments/assets/5dcd9663-d3ee-48e6-935a-5da2654e5ef4" />


```bash
az webapp create \
  --resource-group mdm-lj2-rg \
  --plan mdm-lj2-plan \
  --name calvaro-onnx-image-classifier \
  --deployment-container-image-name calvaro/car-color-classifier:latest
```
<img width="1221" alt="Azure Web App – Erfolgreiche Erstellung der App mit Container-Image  " src="https://github.com/user-attachments/assets/c9f2374d-8291-4c6d-8f63-e1230da736d2" />
<img width="1180" alt="53" src="https://github.com/user-attachments/assets/1c92ee8b-c7bd-4832-aad6-29e0993d50c3" />



#### Live-Loganzeige:

```bash
az webapp log tail --name calvaro-onnx-image-classifier --resource-group mdm-lj2-rg
```
<img width="962" alt="frontend test after deployment" src="https://github.com/user-attachments/assets/d08d09bc-f515-4a60-8ea7-ea4a07a71371" />



---

### Dokumentation Deployment ACA (Azure Container Apps)

#### Erstellung einer Resource Group

```bash
az group create --name mdm-aca-rg --location westeurope
```

Deployment der Web App
Die eigentliche Web App calvaro-onnx-image-classifier wurde erstellt und mit dem Container aus DockerHub verknüpft:


az webapp create \
  --resource-group mdm-lj2-rg \
  --plan mdm-lj2-plan \
  --name calvaro-onnx-image-classifier \
  --deployment-container-image-name calvaro/car-color-classifier:latest
<img width="1202" alt="Azure App Service Plan – Erstellung eines Linux-Free-Plans (mdm-lj2-plan)" src="https://github.com/user-attachments/assets/b18085c4-8fa4-4d25-9d38-e9b90b3c6f85" />

![calvaro onnx app services](https://github.com/user-attachments/assets/b69e85c0-748b-470e-9a4e-46d8dda74969)



#### Erstellung eines ACA-Environments

```bash
az containerapp env create \
  --name mdm-aca-env \
  --resource-group mdm-aca-rg \
  --location westeurope
```

<img width="1204" alt="Azure Container App – Erfolgreiche Erstellung mit öffentlichem Zugriff (FQDN)" src="https://github.com/user-attachments/assets/130910c2-3f99-4493-997c-d1e0ad56c5a5" />


#### Deployment der App in ACA

```bash
az containerapp create \
  --name calvaro-onnx-aca \
  --resource-group mdm-aca-rg \
  --environment mdm-aca-env \
  --image calvaro/car-color-classifier:latest \
  --target-port 80 \
  --ingress 'external'
```
<img width="1222" alt="Azure Container Apps Environment – Erfolgreiche Erstellung der ACA-Umgebung (mdm-aca-env)" src="https://github.com/user-attachments/assets/cd10b237-68bb-49e0-8690-930605cc2984" />


Zugriff auf App über:

📎 `https://calvaro-onnx-aca.agreeablefield-89d16092.westeurope.azurecontainerapps.io`

#### Prüfung der Logs:

```bash
az containerapp logs show \
  --name calvaro-onnx-aca \
  --resource-group mdm-aca-rg \
  --follow
```

<img width="1220" alt="Azure Container App – Live-Logs zeigen erfolgreichen Gunicorn-Start (ACA)  " src="https://github.com/user-attachments/assets/1cdee6db-c8ac-46d4-8799-7786a1c9562c" />


---

### Dokumentation Deployment ACI (Azure Container Instances)

#### Provider registrieren:

```bash
az provider register --namespace Microsoft.ContainerInstance --wait
```

#### Container Deployment via ACI:

```bash
az container create \
  --name calvaro-onnx-aci \
  --resource-group mdm-aca-rg \
  --image calvaro/car-color-classifier:latest \
  --dns-name-label calvaro-onnx-aci-$(date +%s) \
  --ports 80 \
  --os-type Linux \
  --cpu 1 \
  --memory 1.5 \
  --registry-login-server index.docker.io \
  --registry-username calvaro \
  --registry-password <dockerhub-password>
```


#### Logs anzeigen:

```bash
az container logs \
  --name calvaro-onnx-aci \
  --resource-group mdm-aca-rg
```

<img width="1023" alt="Container Logs ACI – Gunicorn erfolgreich gestartet" src="https://github.com/user-attachments/assets/0adde5b6-0d96-45f2-969d-e2b260023edc" />

Frontend-Test nach Deployment
Die Web App war erfolgreich erreichbar unter:
https://calvaro-onnx-image-classifier.azurewebsites.net

Eine Beispiel-Inferenz konnte durchgeführt werden. Die hochgeladene Datei (multiplia.png) wurde korrekt klassifiziert als minivan.
<img width="898" alt="frontend test" src="https://github.com/user-attachments/assets/b8de135a-7a7c-4724-b9ca-89ab532e836d" />
<img width="962" alt="frontend test after deployment" src="https://github.com/user-attachments/assets/fe3d04bf-efe6-44e1-9657-c95d3f05820f" />

## Lessons Learned 

* **Docker-Grundlagen** wie `build`, `tag`, `push`, `run` vollständig verstanden und getestet
* **Gunicorn & Flask-Konfiguration** im Container gelernt
* **Azure CLI Workflows** (Web App, ACA, ACI) inklusive Logzugriff und Umgebungsvariablen
* Verständnis der Unterschiede zwischen Azure Deployment-Varianten (Web App vs ACA vs ACI)
* Debugging realer Deployment-Probleme (Port 8181, inkompatibles .NET Core)
* Optimierung durch Wahl von ACA als stabilste Option für unsere Python-basierte ML-App
* GitHub & DockerHub Integration professionell eingerichtet

---

---

*Erstellt von Christopher Alvaro – FS2025 ZHAW MDM – Portfolio Containerisierung*



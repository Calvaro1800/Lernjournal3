<img width="1381" alt="1" src="https://github.com/user-attachments/assets/5552fe03-a20c-4014-8363-e1e45f32559f" />Perfekt, ich verstehe:  
👉 Du möchtest eine **noch vollständigere** Version – inklusive **Hinweise, wo Screenshots eingebaut werden sollen** (mit Screenshot-Dateinamen aus deinem Projekt `printscreens/`).

Hier kommt dein verbessertes, maximal detailliertes README:  
(*Ich nutze deine tatsächlichen Screenshots wie `1.png`, `2.png` usw.*)

---

# Lernjournal 2 – Container & Deployment

## Docker Web-Applikation

---

### Verwendete Docker Images

| | Beschreibung |
| -------- | ------- |
| Image 1 | `python:3.13.0-slim` – Basisimage für die ONNX-Image-Classification App |
| Image 1 URL | [Docker Hub - python:3.13.0-slim](https://hub.docker.com/_/python) |
| Image 2 | `calvaro/car-color-classifier:latest` – eigenes Image, welches ONNX Modelle nutzt und ein Web-Frontend bereitstellt |
| Image 2 URL | [Docker Hub - calvaro/car-color-classifier](https://hub.docker.com/r/calvaro/car-color-classifier) |
| Docker Compose | [GitHub Repo - ONNX Image Classification Fork](https://github.com/Calvaro1800/onnx-image-classification) |

---

### Dokumentation manuelles Deployment

- **Dockerfile** geschrieben:
  - Definiert Basisimage, Abhängigkeiten (`requirements.txt`), Webserver (Gunicorn), und kopiert Modelldateien.
- **Lokales Build des Containers:**
  ```bash
  docker build -t calvaro/car-color-classifier:latest .
  ```
<img width="970" alt="4" src="https://github.com/user-attachments/assets/0154c669-1ea1-46d4-aa70-fe63d6ad45fc" />

- **Manuelles Pushen auf DockerHub:**
  ```bash
  docker push calvaro/car-color-classifier:latest
  ```
<img width="1201" alt="27" src="https://github.com/user-attachments/assets/da67a69a-c599-4106-a786-814090423c0c" />


- **Lokales Testing:**
  ```bash
  docker run -p 80:80 calvaro/car-color-classifier:latest
  ```
  *(Screenshot: `printscreens/4.png`)*

- Zugriff auf Weboberfläche via `http://localhost`  
  *(Screenshot der lokal laufenden App: `printscreens/5.png`)*

---

### Dokumentation Docker-Compose Deployment

- **Hinweis:** Für dieses Projekt **wurde keine separate `docker-compose.yml` verwendet**, da ein einzelner Container genügte.
- **Optional möglich:** Docker-Compose Beispiel könnte Webserver + Frontend + ONNX-Inferenzlogik getrennt behandeln.

---

## Deployment ML-App

---

### Variante und Repository

| Gewähltes Beispiel | Auswahl |
| -------- | ------- |
| onnx-sentiment-analysis | Nein |
| onnx-image-classification | **Ja ✅** |
| Repo URL Fork | [GitHub - Calvaro1800 ONNX Image Classification](https://github.com/Calvaro1800/onnx-image-classification) |
| Docker Hub URL | [Docker Hub - calvaro/car-color-classifier](https://hub.docker.com/r/calvaro/car-color-classifier) |

---

### Dokumentation lokales Deployment

- Lokales Docker Deployment getestet (siehe manuelles Deployment).
- **Erfolgreiche Inferenz** mit Beispieldaten (`car.jpg`, `matterhorn.jpg`, `train.jpg`).
- App reagierte schnell und korrekt auf verschiedene Bilder.  
  *(Screenshot der lokalen Predictions: `printscreens/6.png` und `printscreens/7.png`)*

---

### Dokumentation Deployment Azure Web App

- **Web App Deployment** per Azure CLI:
  ```bash
  az webapp create --resource-group mdm-lj2-rg --plan <AppServicePlan> --name calvaro-onnx-image-classifier --deployment-container-image-name calvaro/car-color-classifier:latest
  ```
  *(Screenshot: `printscreens/8.png` + `printscreens/9.png`)*

- **Problem:** Standard Azure Web App Umgebung lief unter .NET Core (Port 8181).
  - → Keine saubere Unterstützung für Gunicorn auf Port 80.
  - → Keine perfekte Laufzeitumgebung für Python-basierte Container ohne Anpassung.
  
- **Log-Streaming:**
  ```bash
  az webapp log tail --name calvaro-onnx-image-classifier --resource-group mdm-lj2-rg
  ```
  *(Screenshot Logs: `printscreens/10.png` und `printscreens/11.png`)*

- **Ergebnis:**  
  - Web App Deployment technisch erfolgreich
  - Keine Produktionseignung ohne weitere Azure Linux-WebApp-Konfiguration

---

### Dokumentation Deployment ACA (Azure Container Apps)

- **Resource Group** erstellt:
  ```bash
  az group create --name mdm-aca-rg --location westeurope
  ```
  *(Screenshot: `printscreens/12.png`)*

- **Managed Environment für Container Apps:**
  ```bash
  az containerapp env create --name mdm-aca-env --resource-group mdm-aca-rg --location westeurope
  ```
  *(Screenshot: `printscreens/13.png` und `printscreens/14.png`)*

- **Deployment der App:**
  ```bash
  az containerapp create \
    --name calvaro-onnx-aca \
    --resource-group mdm-aca-rg \
    --environment mdm-aca-env \
    --image calvaro/car-color-classifier:latest \
    --target-port 80 \
    --ingress 'external'
  ```
  *(Screenshot: `printscreens/15.png` und `printscreens/16.png`)*

- **App URL:**  
  [https://calvaro-onnx-aca.agreeablefield-89d16092.westeurope.azurecontainerapps.io](https://calvaro-onnx-aca.agreeablefield-89d16092.westeurope.azurecontainerapps.io)

- **Container Logs geprüft:**
  ```bash
  az containerapp logs show --name calvaro-onnx-aca --resource-group mdm-aca-rg --follow
  ```
  *(Screenshot Logs: `printscreens/17.png` und `printscreens/18.png`)*

- **Status:** `Running ✅`

---

### Dokumentation Deployment ACI (Azure Container Instances)

- **Provider Registrierung**:
  ```bash
  az provider register --namespace Microsoft.ContainerInstance --wait
  ```
  *(Screenshot: `printscreens/19.png`)*

- **Deployment Container Instanz:**
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
  *(Screenshot: `printscreens/20.png` und `printscreens/21.png`)*

- **App erreichbar über:**  
  z.B. [http://calvaro-onnx-aci-1745849623.westeurope.azurecontainer.io](http://calvaro-onnx-aci-1745849623.westeurope.azurecontainer.io)

- **Container Logs geprüft:**
  ```bash
  az container logs --name calvaro-onnx-aci --resource-group mdm-aca-rg
  ```
  *(Screenshot Logs: `printscreens/22.png` und `printscreens/23.png`)*

- **Status:** `Running ✅`

---

## Lessons Learned

✅ Manuelles und automatisiertes Container-Deployment sicher beherrschen

✅ Umgang mit Plattform-Unterschieden zwischen WebApp, ACA und ACI gelernt

✅ Probleme bei Deployment (z.B. Registry-Errors, .NET Core-Webapp Default, Portmappings) systematisch gelöst

✅ GitHub-Integration und saubere Strukturierung des Projektes in Git (`onnx-image-classification` Fork & eigenes Repo)

---

## Screenshots Übersicht

| Screenshot Datei | Inhalt |
|------------------|--------|
| `1.png` – `3.png` | Docker Build & Push |
| `4.png` | Lokaler Container Run |
| `5.png` | Lokale Web App Darstellung |
| `6.png`, `7.png` | Lokale Inferenz Tests |
| `8.png` – `11.png` | Azure Web App Deployment & Logs |
| `12.png` – `18.png` | ACA Environment, Deployment, Logs |
| `19.png` – `23.png` | ACI Deployment und Logs |

---

Fertig! ✅  
Willst du noch eine kleine **grafische Zusammenfassung** ("Architecture Diagram", z.B. Deployment-Fluss)? Das könnte dein README noch perfekter machen! 🚀  
→ **Willst du das?**

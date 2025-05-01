# Lernjournal 3 – ONNX

## Übersicht

| Kategorie | Link/Info |
|----------|-----------|
| ONNX Modell für Analyse (Netron) | https://netron.app |
| Fork der App (EfficientNet-Lite) | https://github.com/Calvaro1800/Lernjournal3 |

---

## 1. ONNX Analyse

### Modell: EfficientNet-Lite4 (ursprünglich)
- **Top-1 Accuracy:** 80.4 %
- **Größe:** ca. 49 MB

Analyse mit Netron:
```bash
netron efficientnet-lite4-11.onnx
```
![efficientnet-lite4-11 onnx](https://github.com/user-attachments/assets/d4d0dbfa-1b6d-40a4-952e-317fa8af5335)


Beobachtungen:
- Input-Name: `images:0`
- Shape: `[1, 3, 224, 224]`
- Dtype: `float32`
- Output: Softmax Layer

Probleme bei Inferenz:
- falscher Dtype (`double` statt `float`)
- unerwartete Inputnamen

Entscheidung: Wechsel auf SqueezeNet zur Vereinfachung.

---

## 2. Projektstruktur & Setup

Initialisierung:
```bash
git clone https://github.com/Calvaro1800/Lernjournal3.git
cd Lernjournal3
```

Modelldownload:
```bash
curl -L -o squeezenet1.0-12.onnx https://github.com/onnx/models/raw/main/validated/vision/classification/squeezenet/model/squeezenet1.0-12.onnx
curl -o labels_map.txt https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json
```

Projektstruktur:
```text
├── app.py
├── squeezenet1.0-12.onnx
├── labels_map.txt
├── static/
├── templates/
└── screenshots/
```

---

## 3. Anpassung Backend (Flask)

Bildvorverarbeitung:
```python
def preprocess_image(img):
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32)
    img -= np.array([123.68, 116.779, 103.939], dtype=np.float32)
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)
    return img
```

ONNX Inferenz mit:
```python
ort_session = onnxruntime.InferenceSession("squeezenet1.0-12.onnx")
input_name = ort_session.get_inputs()[0].name
```

---

## 4. Frontend / JS-Logik

Upload und API-Aufruf:
```javascript
fetch('/analyze', {
  method: 'POST',
  body: formData
}).then(response => response.json())
  .then(data => {
    // Anzeige der Top-5-Klassen
  });
```

Ergebnisse werden als HTML-Tabelle dargestellt.

---

## 5. Vergleich der Modelle

| Bild       | EfficientNet-Lite4       | SqueezeNet            |
|------------|---------------------------|------------------------|
| Kirche     | church (98.78%)           | church (79.10%)       |
| Flugzeug   | airliner (99.62%)         | airliner (89.63%)     |
| Papagei    | grey parrot (100.00%)     | grey parrot (82.15%)  |

**Screenshots:**

### Kirche
<img width="815" alt="Screenshot 2025-04-30 at 23 16 14" src="https://github.com/user-attachments/assets/ce0bf7ee-a362-40ce-8126-fb4e61949937" />
<img width="1081" alt="Screenshot 2025-04-30 at 23 42 56" src="https://github.com/user-attachments/assets/56395650-aa83-43b1-bb61-b426bcf9d04d" />

### Flugzeug
<img width="1022" alt="Screenshot 2025-04-30 at 23 15 56" src="https://github.com/user-attachments/assets/ae658102-b10d-455b-9d6e-2563079b2392" />
<img width="1183" alt="Screenshot 2025-04-30 at 23 43 05" src="https://github.com/user-attachments/assets/27618cbb-0d73-48f2-adcc-ec3d59eaf882" />


### Papagei
<img width="1063" alt="Screenshot 2025-04-30 at 23 11 41" src="https://github.com/user-attachments/assets/9b77caf3-ec6e-4ecf-84c7-9d8f2676ab54" />
<img width="1174" alt="Screenshot 2025-04-30 at 23 43 14" src="https://github.com/user-attachments/assets/8d1c5ba8-9293-4fe4-944a-a6cac4190dc7" />


---

## 6. Lessons Learned

- Netron ist extrem hilfreich für Analyse und Fehlersuche
- Bildvorverarbeitung ist modellabhängig (z. B. Normalisierung)
- ONNX Runtime liefert gute Fehlermeldungen
- SqueezeNet ist ideal für Web-Demos durch geringe Größe
- Git-Submodul-Warnung beachten: keine Repos einbetten

---

## 7. Fazit

Dieses Lernjournal ermöglichte eine komplette Pipeline:
1. Auswahl und Analyse eines ONNX-Modells
2. Fehleranalyse mit Netron und ONNX Runtime
3. Integration in Flask + Frontend
4. Vergleich zweier Modelle

Die App funktioniert stabil lokal und kann erweitert oder online deployed werden.

👉 GitHub: https://github.com/Calvaro1800/Lernjournal3

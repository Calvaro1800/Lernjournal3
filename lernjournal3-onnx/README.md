## Lernjournal 3 – ONNX

### Übersicht
| Kategorie | Link/Info |
|----------|-----------|
| ONNX Modell für Analyse (Netron) | https://netron.app |
| onnx-image-classification Fork (EfficientNet-Lite) | https://github.com/Calvaro1800/Lernjournal3 |

---

### Dokumentation ONNX Analyse

Für dieses Lernjournal habe ich zunächst das Modell **EfficientNet-Lite4** aus dem ONNX Model Zoo verwendet. Dieses Modell ist bekannt für seine hohe Genauigkeit (ca. 80% Top-1 Accuracy) bei gleichzeitig moderatem Speicherbedarf (ca. 49 MB). Es eignet sich gut als Referenz für leistungsfähige Inferenzmodelle in produktiven Umgebungen, beispielsweise für Cloud- oder Edge-Einsatz.

#### Analyse mit Netron: EfficientNet-Lite4
Netron ist ein browserbasiertes Tool zur Analyse von ONNX-Modellen. Es zeigt die komplette Modellstruktur mit Layernamen, Shapes, Dtypes und Datenfluss.

```bash
netron efficientnet-lite4-11.onnx
```

**Beobachtungen:**
- Input: `images:0`, Shape `[1,3,224,224]`, Dtype `float32`
- Typische Layer: Conv2D, BatchNorm, Relu/Swish, Bottlenecks
- Output: Softmax-Schicht mit 1000 Klassen

Die Komplexität ist durch viele **Bottleneck-Blöcke** gekennzeichnet, die Depthwise Convolutions und Residualverbindungen kombinieren. Die finale Schicht ist ein FC-Layer nach GlobalAveragePooling.

📸 Beispielbild (Netron Ansicht):
```markdown
![efficientnet-lite4-11 onnx](https://github.com/user-attachments/assets/9cb7f7a6-9cfc-4d1d-a2d8-5b78e44bfc19)


```

#### Analyse mit Netron: SqueezeNet 1.0
Später wurde **SqueezeNet** als kompakteres Modell gewählt (ca. 4.8 MB). Auch dieses Modell wurde mit Netron analysiert:
```bash
netron onnx-image-classification/squeezenet1.0-12.onnx
```

SqueezeNet nutzt sogenannte **Fire-Module** als Kernelement der Architektur:
- Jedes Fire-Modul besteht aus einem **Squeeze-Layer** (1x1 Convolution), gefolgt von zwei parallelen **Expand-Layern** (1x1 und 3x3 Convolutions).
- Diese Ergebnisse werden konkateniert und an die nächste Stufe weitergegeben.

Netron zeigt für jedes Modul:
- Die **konkret verwendeten Kernelgrößen**
- Shapes der Ein- und Ausgaben
- Relu-Aktivierungen zwischen den Blöcken
- Optional: MaxPool zwischen den Gruppen zur Reduktion der räumlichen Dimension

📸 Visualisierung (siehe `screenshots/`):
```markdown

![onnx-image-classification_squeezenet1 0-12 onnx](https://github.com/user-attachments/assets/22b3b066-605d-4ee7-9dd2-632268bcd46d)

```

**Layer-Struktur im Überblick:**
1. Conv + Relu + MaxPool
2. Fire1 – Fire8 (bestehend aus Squeeze/Expand/Concat)
3. Dropout
4. Finaler Conv (1000 Klassen)
5. Global Average Pooling
6. Softmax

Die Vorteile der Netron-Analyse:
- Einfache visuelle Überprüfung der Architektur
- Exakte Kenntnis über Input-Namen und -Formate
- Hilfreich für das Debugging (z. B. bei falschen Inputtypen oder fehlenden Tensornamen)

Durch diese visuelle und strukturelle Analyse konnte ich die Inferenz-Pipeline gezielt anpassen – z. B. durch Korrektur der Preprocessing-Schritte oder Ermittlung des exakten Input-Namens mit:
```python
input_name = ort_session.get_inputs()[0].name
```

Diese Erkenntnisse waren essenziell, um sowohl EfficientNet als auch SqueezeNet erfolgreich lokal mit ONNX Runtime in Flask einzubinden.

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
<img width="815" alt="Screenshot 2025-04-30 at 23 16 14" src="https://github.com/user-attachments/assets/08ab327c-ca3a-4cc5-a1c8-c100e1dd607e" />
<img width="1081" alt="Screenshot 2025-04-30 at 23 42 56" src="https://github.com/user-attachments/assets/d22bbff4-4a9c-4c38-84de-f8f0c64f4fdf" />

### Flugzeug
<img width="1022" alt="Screenshot 2025-04-30 at 23 15 56" src="https://github.com/user-attachments/assets/2d455123-9adc-4ab5-8e19-4785b85e8bc7" />
<img width="1183" alt="Screenshot 2025-04-30 at 23 43 05" src="https://github.com/user-attachments/assets/e6e8e0a8-75e7-4ea6-8cf3-8047c55366a2" />

### Papagei
<img width="1063" alt="Screenshot 2025-04-30 at 23 11 41" src="https://github.com/user-attachments/assets/61fb27a8-ce23-42cf-84fe-7dd6997d3db7" />
<img width="1174" alt="Screenshot 2025-04-30 at 23 43 14" src="https://github.com/user-attachments/assets/4eaa5e3a-0754-42d1-b813-6fee4cc02399" />


---

## 6. Lessons Learned

- Netron ist extrem hilfreich für Analyse und Fehlersuche
- Bildvorverarbeitung ist modellabhängig (z. B. Normalisierung)
- ONNX Runtime liefert gute Fehlermeldungen
- SqueezeNet ist ideal für Web-Demos durch geringe Größe
- Git-Submodul-Warnung beachten: keine Repos einbetten

---

## 7. Fazit

Durch dieses Lernjournal konnte ich ein umfassendes Verständnis für die Struktur und Funktionsweise von ONNX-Modellen entwickeln. Besonders wertvoll war der direkte Vergleich zwischen EfficientNet-Lite4 und SqueezeNet – zwei Modellen mit unterschiedlicher Komplexität und Größe. Die Analyse mit Netron hat mir geholfen, den Datenfluss im Modell zu verstehen und die erforderlichen Preprocessing-Schritte im Backend korrekt umzusetzen. Zudem zeigte sich, wie entscheidend die richtige Wahl der Normalisierung, das Input-Format und der Input-Name für eine erfolgreiche Inferenz sind. Die ONNX Runtime erwies sich als robust und verständlich in ihrer Fehlerkommunikation. Insgesamt hat mir dieses Projekt praxisnah gezeigt, wie Modelle in Webanwendungen integriert und evaluiert werden können. Besonders der Wechsel zu einem kleineren Modell wie SqueezeNet hat deutlich gemacht, wie Modellwahl und Performance im Deployment-Kontext zusammenspielen. Dieses Wissen wird mir bei zukünftigen ML-Projekten, insbesondere im Bereich Modellbereitstellung, sehr nützlich sein.

Die App funktioniert stabil lokal und kann erweitert oder online deployed werden.

👉 GitHub: https://github.com/Calvaro1800/Lernjournal3

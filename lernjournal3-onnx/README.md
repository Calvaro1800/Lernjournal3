# Lernjournal 3 – ONNX

## Übersicht

|                               | Link/Info                                                  |
|-------------------------------|------------------------------------------------------------|
| **ONNX Modell (Netron)**      | https://netron.app                                         |
| **Verwendetes Modell**        | SqueezeNet 1.0 (Version 12)                                |
| **GitHub Repository (Fork)**  | https://github.com/Calvaro1800/Lernjournal3               |

---

## Dokumentation – ONNX Analyse

Für dieses Lernjournal wurde das Modell **SqueezeNet v1.0** gewählt. Es gehört zu den leichtgewichtigsten CNN-Architekturen und eignet sich daher besonders für Edge- und Webanwendungen. Es besteht aus sogenannten Fire-Modulen, die eine `squeeze`- (1x1-Convolution) und eine `expand`-Schicht (1x1 und 3x3-Convolutions) kombinieren. Diese Architektur reduziert die Anzahl an Parametern deutlich.

Zur Analyse der Modellstruktur wurde **Netron** verwendet. Dabei konnte das Modell visuell untersucht werden. Wichtig war zu erkennen, wie der Datenfluss aufgebaut ist, wie die Layer benannt sind und welche Formate die Inputs und Outputs haben.

📷 *[Screenshot Netron mit geöffnetem SqueezeNet-Modell hier einfügen]*

---

## Dokumentation – onnx-image-classification Anwendung

### 1. Projektinitialisierung

Das offizielle Repository `onnx-image-classification` wurde geforkt und lokal auf dem Rechner geklont:

```bash
git clone https://github.com/Calvaro1800/Lernjournal3.git
cd Lernjournal3
Anschließend wurde das ursprüngliche Modell entfernt und durch squeezenet1.0-12.onnx ersetzt. Die Datei wurde aus dem ONNX Model Zoo heruntergeladen:

bash
Copy
Edit
curl -L -o squeezenet1.0-12.onnx https://github.com/onnx/models/raw/main/vision/classification/squeezenet/model/squeezenet1.0-12.onnx
Auch die Label-Datei labels_map.txt wurde aus einer öffentlichen Quelle ergänzt:

bash
Copy
Edit
curl -o labels_map.txt https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json
📷 [Screenshot Verzeichnisstruktur mit .onnx-File und labels_map.txt einfügen]

2. Modellintegration im Backend (app.py)
Der Python-Server basiert auf Flask und wurde so angepasst, dass das neue Modell verwendet werden kann. Der Modellname in der InferenceSession() wurde auf SqueezeNet gesetzt. Außerdem wurde die Bildvorverarbeitung angepasst:

Resize auf 224x224

RGB-Konvertierung

ImageNet-Normalisierung (Mittelwerte je Kanal)

Numpy-Array → Tensor → Batch

Hier ist ein Ausschnitt des Codes zur Vorverarbeitung:

python
Copy
Edit
def preprocess_image(img):
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32)
    img -= np.array([123.68, 116.779, 103.939], dtype=np.float32)
    img = np.transpose(img, (2, 0, 1))  # HWC -> CHW
    img = np.expand_dims(img, axis=0)
    return img
📷 [Screenshot vom Codeabschnitt app.py in VSCode einfügen]

Fehler wie z. B. „Expected tensor(float), got tensor(double)” wurden durch korrektes astype(np.float32) behoben.

3. Upload-Logik und Ergebnisanzeige (JavaScript)
Die Frontend-Logik wurde mit dem bestehenden script.js beibehalten. Es wird geprüft, ob genau eine Bilddatei hochgeladen wurde. Dann wird das Bild via fetch an /analyze gesendet und die JSON-Antwort in eine Tabelle mit Top-5-Ergebnissen umgewandelt.

Die wichtigsten Stellen:

javascript
Copy
Edit
fetch('/analyze', {
    method: 'POST',
    body: formData
}).then(response => response.json())
  .then(data => {
    // Daten in HTML-Tabelle darstellen
  });
📷 [Screenshot der Weboberfläche mit eingefügtem Bild und Ergebnistabelle einfügen]

4. Tests mit realen Bildern
Zur Verifikation wurde das System mit mehreren Testbildern geprüft (Papagei, Kirche, etc.). Je nach Qualität und Ausschnitt war das Ergebnis plausibel. Das Modell ist besonders sensitiv auf helle Farben, klare Kontraste und typisches ImageNet-Material.

📷 [Screenshots von verschiedenen Klassifikationsergebnissen einfügen – z. B. prediction auf Papagei]

5. Lessons Learned
Das Projekt ermöglichte einen praxisnahen Einblick in die ONNX-Inferenz im Webkontext. Wichtige Erkenntnisse:

Die Bildvorverarbeitung muss exakt zur Trainingskonfiguration des Modells passen

Die Inputnamen (input_name = ort_session.get_inputs()[0].name) variieren je nach Modell

Die Modellstruktur kann mit Netron einfach analysiert und verstanden werden

Fehler wie falsche Dtype oder Shape führen zu klaren ONNXRuntime-Exceptions – hilfreich für Debugging

Fazit
Mit SqueezeNet wurde erfolgreich ein leichtgewichtiges ONNX-Modell in eine Flask-basierte Webanwendung integriert. Die Ausgabe funktionierte im Frontend zuverlässig, die Klassifikationsergebnisse wurden verständlich dargestellt. Die Kombination aus Modellanalyse (Netron), Modelldownload, Python-Inferenz und Webintegration war didaktisch sinnvoll und hat mein Verständnis für Modellbereitstellung und -nutzung deutlich vertieft.

📷 [Finaler Screenshot der funktionierenden App mit Vorhersage und Bild einfügen]

Repository
👉 https://github.com/Calvaro1800/Lernjournal3

yaml
Copy
Edit

---

### 📸 Screenshot-Tipps:

Du kannst Screenshots in einem Ordner `screenshots/` ablegen und im README z. B. so referenzieren:

```markdown
![Netron Ansicht](screenshots/netron-squeezenet.png)
✅ Terminal-Kommandos zum Push
bash
Copy
Edit
git add .
git commit -m "README und Screenshots ergänzt"
git push

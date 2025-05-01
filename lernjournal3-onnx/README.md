Lernjournal 3 – ONNX

Übersicht

Kategorie

Link/Info

ONNX Modell für Analyse (Netron)

https://netron.app

onnx-image-classification Fork (EfficientNet-Lite)

https://github.com/Calvaro1800/Lernjournal3

Dokumentation ONNX Analyse

Für dieses Lernjournal habe ich zunächst das Modell EfficientNet-Lite4 aus dem ONNX Model Zoo verwendet. Dieses Modell ist bekannt für seine hohe Genauigkeit (ca. 80% Top-1 Accuracy) bei gleichzeitig moderatem Speicherbedarf (ca. 49 MB). Es eignet sich gut als Referenz für leistungsfähige Inferenzmodelle in produktiven Umgebungen, beispielsweise für Cloud- oder Edge-Einsatz.

Zur Analyse habe ich das Modell mit Netron geöffnet. Netron ist ein browserbasiertes Tool, das ONNX-Modelle visuell darstellen kann. Besonders hilfreich war, dass ich die gesamte Struktur inklusive Layernamen, Verbindungslogik und Shape der Tensoren sehen konnte.

Beispielsweise wird bei EfficientNet der Input unter dem Namen images:0 erwartet, mit einer Form von [1, 3, 224, 224] und dem Dtype float32. Der Output liegt typischerweise in einem Softmax-Layer vor, z. B. Softmax_156.

Netron wurde lokal mit folgendem Befehl gestartet:

netron efficientnet-lite4-11.onnx

Das Modell war danach über http://localhost:8080 visualisierbar.

📸 Tipp: Du kannst den Screenshot von Netron direkt ins screenshots/-Verzeichnis legen und so im README einbinden:

![Netron Ansicht EfficientNet](screenshots/netron-efficientnet-lite4.png)



Allerdings traten bei der Integration von EfficientNet-Lite4 in die Flask-Anwendung einige Probleme auf:

Fehlermeldung zu falschem Dtype: tensor(double) statt tensor(float)

Abweichende Inputnamen, was zu Required inputs are missing-Fehlern führte

Schwierigkeiten beim Shape Matching, z. B. [1,3,224,224] vs. [224,224,3]

Nach mehreren Debugging-Schritten (u. a. Nutzung von ort_session.get_inputs()) habe ich mich dazu entschieden, auf das kompaktere Modell SqueezeNet 1.0 zu wechseln, um die Entwicklung zu vereinfachen.

Dokumentation onnx-image-classification

1. Projektinitialisierung

Ich habe das offizielle Template-Repository onnx-image-classification geforkt und lokal geklont:

git clone https://github.com/Calvaro1800/Lernjournal3.git
cd Lernjournal3

Zuerst wurde das Modell efficientnet-lite4-11.onnx heruntergeladen:

curl -L -o efficientnet-lite4-11.onnx https://github.com/onnx/models/raw/main/validated/vision/classification/efficientnet-lite4/model/efficientnet-lite4-11.onnx

Nachdem jedoch mehrere Fehler auftraten, habe ich das Modell durch squeezenet1.0-12.onnx ersetzt:

curl -L -o squeezenet1.0-12.onnx https://github.com/onnx/models/raw/main/validated/vision/classification/squeezenet/model/squeezenet1.0-12.onnx

Zusätzlich wurde die Label-Map heruntergeladen:

curl -o labels_map.txt https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json

Die lokale Verzeichnisstruktur sieht danach z. B. so aus:

├── app.py
├── squeezenet1.0-12.onnx
├── labels_map.txt
├── static/
├── templates/
└── screenshots/

📸 Screenshot-Idee:

![Projektstruktur](screenshots/verzeichnis.png)

2. Anpassung der app.py

Die Flask-Anwendung musste entsprechend angepasst werden:

Lade des ONNX-Modells squeezenet1.0-12.onnx

Bildvorverarbeitung angepasst an die erwartete Eingabe:

Ausgabe des Outputs auf Basis der Top-5 Wahrscheinlichkeiten

def preprocess_image(img):
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32)
    img -= np.array([123.68, 116.779, 103.939], dtype=np.float32)
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)
    return img

Fehler wie z. B. tensor(double) wurden durch die explizite Umwandlung in np.float32 gelöst.

Zur Ausgabe wurde der Top-5 Softmax-Output sortiert und mit den Klassenlabels gemappt. Die Labels stammen aus der Datei imagenet-simple-labels.json.



3. Web-Oberfläche und Upload-Logik

Die bestehende HTML- und JS-Struktur wurde beibehalten. Nach dem Bildupload wird dieses per fetch an /analyze gesendet, und die Top-5-Ergebnisse werden in einer HTML-Tabelle dargestellt:

fetch('/analyze', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => {
  // Tabelle aktualisieren
});

📸 Beispiel:

![Prediction Kirche](screenshots/prediction-kirche-squeezenet.png)

4. Vergleich der Ergebnisse

Hier wurden drei Bilder mit EfficientNet-Lite4 und SqueezeNet analysiert:

Bild

EfficientNet-Lite4 (Top-1)

SqueezeNet (Top-1)

Kirche

church (98.78%)

church (79.10%)

Flugzeug

airliner (99.62%)

airliner (89.63%)

Papagei

grey parrot (100%)

grey parrot (82.15%)

EfficientNet war bei allen Beispielen deutlich sicherer, SqueezeNet lieferte aber ebenfalls sinnvolle und konsistente Vorhersagen.










5. Lessons Learned

Die Modellstruktur lässt sich mit Netron effizient visualisieren und verstehen.

Die Bildvorverarbeitung muss exakt zum Modellinput passen (z. B. float32, RGB, Normalisierung).

ONNX Runtime-Fehler sind klar und hilfreich bei Debugging (z. B. falscher Inputname, Dtype).

Kleinere Modelle können ähnliche Ergebnisse liefern, aber mit geringerer Konfidenz.

Git-Fehler (Submodul-Warnung) sollten frühzeitig erkannt und ggf. vermieden werden.

Das Modellverhalten ist je nach Eingabebild deutlich unterschiedlich – was die Wichtigkeit der Vorverarbeitung und Bildqualität unterstreicht.

Der Wechsel vom komplexeren Modell zu einem kleineren war strategisch sinnvoll, da er das Debugging deutlich vereinfachte und trotzdem gute Resultate lieferte.

Netron ist nicht nur für Visualisierung hilfreich, sondern auch zur schnellen Prüfung von Input-/Output-Spezifikationen.

Fazit

Mit diesem Lernjournal konnte ich ein ONNX-Modell erfolgreich in eine eigene Webanwendung integrieren, analysieren und anpassen. Die Kombination aus Modellwahl, Inferenzlogik, Fehleranalyse und Ergebnisvergleich war sehr lehrreich und praxisnah.

Besonders hilfreich war die visuelle Analyse mit Netron sowie die zahlreichen Rückmeldungen der ONNX Runtime während der Entwicklung. Ich konnte wichtige Erfahrungen in der Modellintegration, Formatkonvertierung, Label-Mapping und Fehlersuche sammeln.

Die finale Version wurde auf GitHub veröffentlicht:
👉 https://github.com/Calvaro1800/Lernjournal3

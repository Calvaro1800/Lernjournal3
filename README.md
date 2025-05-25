# MDM-Lernjournal Alvarchr

## Inhalt

* [Lernjournal 1 Python](lernjournal1-python/README.md)
* [Lernjournal 2 Container](lernjournal2-container/README.md)
* [Lernjournal 3 ONNX](lernjournal3-onnx/README.md)
* [Lernjournal 4 UI](lernjournal4-ui/README.md)
* [Projekt 1 Python](projekt1-python/README.md)
* [Projekt 2 Java](projekt2-java/README.md)
* [Review 1 Python](review1-python/README.md)
* [Review 2 Java](review2-java/README.md)

## Schlussteil

### Reflexion, Zusammenfassung

* Die Bearbeitung dieses Moduls war für mich persönlich ebenso bereichernd wie herausfordernd. Als jemand, der ursprünglich nicht aus der Informatik stammt, war es besonders anspruchsvoll, sich in die Vielzahl an Technologien, Tools und Konzepten einzuarbeiten, die in den vier Lernjournalen und den zwei Projekten gefordert wurden. Vor allem zu Beginn fiel es mir schwer, die genauen Erwartungen des Moduls sowie die inhaltliche Tiefe richtig einzuschätzen. Dennoch habe ich mich bewusst dazu entschieden, nicht nur zu bestehen, sondern die Aufgaben als Gelegenheit zu nutzen, echtes technisches Verständnis aufzubauen – und das bedeutet, viel Zeit zu investieren.

Ich habe zahlreiche Abende – und auch mehrere Nächte – damit verbracht, mich „learning by doing“ durch neue Technologien zu arbeiten. Besonders das zweite Lernjournal zur Containerisierung und Deployment via Docker und Azure war inhaltlich extrem dicht. Hier war es nötig, sich mit Dockerfiles, Azure CLI, Container-Registrierung, App Services, Container Apps und ACI gleichzeitig auseinanderzusetzen. Dass ich es geschafft habe, meine Applikation erfolgreich über Azure bereitzustellen (inkl. Debugging der Logs via az webapp log tail), betrachte ich als persönlichen Meilenstein.

Ein weiteres Beispiel war die Implementierung der ONNX-Inferenz in Lernjournal 3, bei dem ich es geschafft habe, ein ONNX-Modell (EfficientNet-Lite4) zu integrieren und lokal wie auch in der Cloud über eine Flask-Webapplikation nutzbar zu machen. Allein der Weg dahin – vom Deployment über Docker Hub, das Troubleshooting von Portkonflikten in Azure Web App bis hin zur funktionierenden ACA-Instanz – war mit etlichen Stunden Selbststudium verbunden. Die Analyse der Logs, das korrekte Mapping von Ports und das Testing der Anwendung über die Browser-URL waren echte Aha-Momente.

Was ich aus dieser intensiven Auseinandersetzung mitgenommen habe, geht weit über die Inhalte hinaus: Ich habe gelernt, komplexe Probleme systematisch zu analysieren, Dokumentationen effizient zu nutzen, und technische Fehler nicht als Rückschläge, sondern als Teil des Lernprozesses zu begreifen. Mein Vertrauen in meine Fähigkeiten, auch ohne Vorkenntnisse neue technologische Felder zu erschließen, ist stark gewachsen.

### Feedback zur Vorlesung (optional)

* Das Modul „Model Deployment & Maintenance“ war inhaltlich eines der spannendsten und relevantesten meines bisherigen Studiums. Es hat mir gezeigt, wie man moderne ML-Anwendungen nicht nur lokal testet, sondern produktionsnah in Containern entwickelt und in die Cloud bringt. Gleichzeitig muss ich ehrlich sagen: Der zeitliche Aufwand war extrem hoch – ich schätze, dass ich insgesamt über 80 Stunden aufgewendet habe. Das entspricht dem Aufwand eines Moduls mit 6 ECTS.

In Zukunft würde ich daher empfehlen, den Umfang dieses Moduls realistisch anzupassen – sei es durch eine Reduktion der verpflichtenden Projekte oder durch eine offizielle Hochstufung auf 6 Kreditpunkte. Die Themen sind zu wichtig, um sie nur oberflächlich zu behandeln, aber der aktuelle Rahmen ist mit anderen Modulen im Semester schwer vereinbar. Nichtsdestotrotz bin ich sehr dankbar für das, was ich in diesem Modul lernen durfte – sowohl technisch als auch über mich selbst.

## Regeln Lernjournal

### Repository
* Eigenes *privates* Haupt-Repository basierend auf dieser Vorlage erstellen
* Weitere *private* Repositories je nach Aufgabenstellung erstellen
* Alle Repositories müssen an [mosazhaw] (https://www.github.com/mosazhaw) freigegeben sein

### Struktur
* Kapitelstruktur inkl. Nummerierung einhalten (die Reihenfolge, Struktur und Bezeichnung der Titel und Untertitel darf nicht verändert werden)
* Es dürfen weitere Untertitel (4. Ebene mit ####) ergänzt werden

### Inhalt
* Deutsch, Markdown
* Inhaltsverzeichnis und URL zu Repositories und Webseiten müssen klickbar sein (Links)
* [ ] TODO bezeichnet Stellen, wo Text und/oder Grafiken/Screenshots ergänzt werden sollen
* Vorgegebene Tabellen zu Beginn der jeweiligen Kapitel müssen belassen werden

### Bilder, Grafiken und Screenshots
* Es dürfen keine externen Bilder, Grafiken oder Screenshots verknüpft werden
* Bilder, Grafiken und Screenshots müssen alle im jeweiligen Unterordner "images" abgelegt *und im Bericht sichtbar verknüpft* werden, ein Beispiel:

<img src="images/mdm.png" alt="DevOpsLogo" width="100" height="100">

### Nachvollziehbarkeit Eigenständigkeit

* Verwendung des eigenen Kürzels/Namen/Accounts in Projektnamen, Datei-Pfaden, Repositories, Docker-Images, Docker-Containern und weiteren wählbaren Bezeichnungen
* Sichtbarkeit des eigenen Kürzels/Name/Accounts auf Screenshots
* Screenshots passend zu aktuellem Datum, verwendeter Hard-/Software, Versionen
* Inhalte Projektbericht passend zu Screencast



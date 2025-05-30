﻿# Review 1 Python

## Beurteiltes Projekt

|       | Bitte ausfüllen |
|-------|-----------------|
| Review von (ZHAW-Kürzel) |   Donajad     |
| Review durch (ZHAW-Kürzel) |    Alvarchr        |
| Datum Review, von/bis |      |

## Review

| Thema                                                                      | Skala | Mängel*                                                                                   | Verbesserungsmöglichkeiten*                                         |
|----------------------------------------------------------------------------|-------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Datenquelle klar definiert (Projekt 2: zusätzlich Abgrenzung zu Projekt 1) | 1     | Es gibt nur eine grobe Idee zur Datenquelle, aber keine klare Spezifikation oder Abgrenzung | Datenquelle konkretisieren (URL, API, CSV, etc.) und schriftlich dokumentieren |
| Scraping vorhanden                                                         | 0     | Kein Scraping-Skript vorhanden                                                             | Scraping mit `requests` + `BeautifulSoup` oder API-Zugriff implementieren       |
| Scraping automatisiert                                                     | 0     | Keine Cronjobs, keine Automatisierung geplant                                              | z.B. Skript mit Zeittrigger (`schedule`, `cron`, GitHub Actions) versehen       |
| Datensatz vorhanden                                                        | 1     | Erste Samples lokal gespeichert, aber nicht strukturiert                                  | Einheitliche Struktur im CSV/JSON erstellen                                     |
| Erstellung Datensatz automatisiert, Verwendung Datenbank                   | 0     | Keine Verbindung zu MongoDB oder SQLite                                                    | DB-Anbindung mit `pymongo` oder ORM planen                                     |
| Datensatz-Grösse ausreichend, Aufteilung Train/Test, Kennzahlen vorhanden  | 0     | Keine Evaluation oder Split vorhanden                                                      | z.B. `train_test_split()` aus `sklearn` verwenden, einfache Kennzahlen ausgeben |
| Modell vorhanden                                                           | 0     | Kein Modell implementiert                                                                  | Modellkonzept auswählen (z.B. Klassifikation, Regression), Baseline implementieren |
| Modell-Versionierung vorhanden (ModelOps)                                  | 0     | Kein Modell gespeichert oder versioniert                                                   | `joblib`, `pickle` oder MLflow einsetzen                                       |
| App: auf lokalem Rechner gestartet und funktional                          | 1     | Frontend teilweise vorhanden, funktioniert nur teilweise                                   | Flask-/SpringBoot-Projekt zum Laufen bringen                                  |
| App: mehrere unterschiedliche Testcases durch Reviewer ausführbar          | 0     | Keine Testfälle vorbereitet oder dokumentiert                                              | Zwei bis drei Testbeispiele implementieren und dokumentieren                    |
| Deployment: Falls bereits vorhanden, funktional und automatisiert          | 0     | Kein Deployment vorhanden, keine Infrastruktur vorbereitet                                 | Dockerfile + Azure CLI oder Render/Heroku Deployment vorbereiten                |
| Code: Git-Repository vorhanden, Arbeiten mit Branches / Commits            | 1     | Git vorhanden, aber kaum Commits, keine Struktur oder Branches                            | Strukturierte README, Commits pro Feature, Branch für neue Komponenten          |
| Code: Dependency Management, Dockerfile, Build funktional                  | 1     | `requirements.txt` vorhanden, Dockerfile teilweise fehlerhaft                             | Lokalen Build testen, Versionen fixieren, Build testen                          |

\* wenn fehlend: mögliche Schwierigkeiten und Lösungen besprechen

## Skala

| Skala |                 |
|-------|-----------------|
| 0     | fehlt           |
| 1     | mit Lücken      |
| 2     | alles vorhanden |
| 3     | übertroffen     |

## Hinweise

Das Projekt befindet sich in einem sehr frühen Stadium. Bisher wurde nur ein Teil der App lokal vorbereitet. Wichtige Schritte wie Scraping, Datenaufbereitung, Modellierung, Evaluation und Deployment fehlen oder sind nicht ausreichend dokumentiert.  
⚠️ **Risikoeinschätzung:** Ohne klare Fokussierung und kontinuierliche Weiterentwicklung wird das Projekt bis zur Deadline kaum fertig.  
→ **Empfehlung:** Nächstes Ziel sollte sein:  
1. Scraping **funktional** machen  
2. Daten in einer Datenbank **strukturieren**  
3. Einfaches **ML-Modell** mit Tests implementieren  
4. App **stabil** lokal starten  
5. Danach schrittweise Deployment und Dokumentation verbessern.

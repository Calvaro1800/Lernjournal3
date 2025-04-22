
from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    name = None
    if request.method == "POST":
        name = request.form.get("name", "Freund")
        messages = [
            "Gib niemals auf – der Anfang ist immer der schwerste!",
            "Du bist stärker, als du denkst.",
            "Vertraue dem Prozess – großartige Dinge brauchen Zeit.",
            "Jeder Tag ist eine neue Chance, dein Bestes zu geben.",
            "Auch der längste Weg beginnt mit dem ersten Schritt.",
            "Fehler sind der Beweis, dass du es versuchst.",
            "Dein Potenzial ist grenzenlos.",
            "Mach weiter – dein zukünftiges Ich wird es dir danken.",
            "Erfolg ist kein Zufall, sondern harte Arbeit.",
            "Bleib dran – auch kleine Fortschritte sind Fortschritt.",
            "Heute ist ein guter Tag, um neu zu beginnen.",
            "Du hast schon so viel geschafft – glaube an dich!",
            "Deine Einstellung bestimmt deine Richtung.",
            "Wenn du fällst, steh stärker wieder auf.",
            "Hindernisse sind Gelegenheiten, zu wachsen.",
            "Die einzige Grenze bist du selbst.",
            "Jede Herausforderung macht dich erfahrener.",
            "Verliere nie dein Ziel aus den Augen.",
            "Träume groß und handle mutig.",
            "Selbst kleine Schritte bringen dich ans Ziel."
        ]
        message = random.choice(messages)
    return render_template("index.html", name=name, message=message)

if __name__ == "__main__":
    app.run(debug=True)
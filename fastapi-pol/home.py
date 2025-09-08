

from flask import Flask, send_file

app = Flask(__name__,
            static_folder="frontend-kriter-manel/src",
            static_url_path="",
            template_folder="frontend-kriter-manel/src"
            )

@app.route("/")
def home():
    return send_file("frontend-kriter-manel/src/index.html")

@app.route("/note")
def note():
    return "null"

if __name__== "__main__":
    app.run(debug=True)
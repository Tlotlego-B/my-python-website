from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",
                           name="Tlotlego Edmund Baitsiwi",
                           phone="0767216063",
                           email="tebaitsiwi@gmail.com")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
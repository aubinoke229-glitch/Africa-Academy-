from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Africa Academy Certification Platform</h1><p>Site en ligne ✔</p>"

@app.route("/admin")
def admin():
    return "<h2>Admin Panel</h2><p>Connexion fonctionnelle ✔</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

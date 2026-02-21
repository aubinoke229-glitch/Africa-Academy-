           app.run(host="0.0.0.0", port=port)from flask import Flask
           import os

           app = Flask(__name__)

           @app.route("/")
           def home():
               return "<h1>Africa Academy Certification</h1>"

               @app.route("/admin")
               def admin():
                   return "<h2>Admin Panel</h2>"

                   if __name__ == "__main__":
                       port = int(os.environ.get("PORT", 10000))
                           app.run(host="0.0.0.0", port=port)
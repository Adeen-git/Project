
import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key")

PASSWORD = "letmein"  # Change this to your desired password

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        entered = request.form.get("password")
        if entered == PASSWORD:
            return render_template('index.html')
        else:
            return render_template('login.html', error=True)
    return render_template('login.html', error=False)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('index.html'), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

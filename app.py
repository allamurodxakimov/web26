from flask import Flask

app = Flask(__name__)
@app.route('/')
def home_page():
    return "Bosh sahifaga xush kelibsiz"
@app.route('/about')
def about():
    return "About sahifaga xush kelibsiz"

@app.route('/contact')
def contact():
    return "Contact sahifaga xush kelibsiz"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

app.debug = True

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/demo")
def demo():
    return render_template("demo.html")
    
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

app.debug = True

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/demo", methods=["GET"])
def demo():
    return render_template("demo.html")

@app.route("/demo_result", methods=["POST"])
def demo_result():
    return render_template("demo_result.html")
    
if __name__ == "__main__":
    app.run(debug=True)

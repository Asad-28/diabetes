import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)

# routing to homw page template from webapp/templates/index.html
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
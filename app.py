from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    model_features = model.feature_names_in_
    return render_template("index.html", model_features=model_features)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(request.form[f]) for f in model.feature_names_in_]
        prediction = model.predict([features])[0]
        return render_template("index.html", prediction_text=f"Estimated House Price: ${prediction:,.2f}")
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)

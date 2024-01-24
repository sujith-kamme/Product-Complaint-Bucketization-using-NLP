from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
from src.code.pipeline.prediction import PredictionPipeline

app = Flask(__name__,static_url_path="/static")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        complaint = str(request.form['complaint'])
        
        obj = PredictionPipeline()
        prob, label = obj.transform_and_predict(complaint)
        prediction_text=f"{label}:{round(prob*100,2)}%"
        print(prediction_text)
        return jsonify({'prediction_text': prediction_text})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True,port=8080)

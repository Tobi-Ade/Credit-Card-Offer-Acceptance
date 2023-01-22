import pickle
import pandas as pd
from flask import Flask, request, jsonify

input_file = 'model.bin'

with open(input_file, 'rb') as file:
    dv, model = pickle.load(file)

app = Flask("credit")

@app.route('/', methods=["POST"])

def predict():
    card_info = request.get_json()

    X = pd.DataFrame([card_info])

    X = dv.transform(card_info)

    y_pred = model.predict_proba(X)[0, 1]

    decision = (y_pred >= 0.5)

    result = {
        'acceptance_probability': float(y_pred), 
        'accept_offer': bool(decision)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)




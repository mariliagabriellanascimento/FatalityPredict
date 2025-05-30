from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})

# Carregar modelo e encoders
modelo = joblib.load("modelo_severidade.pkl")
target_encoder = joblib.load("label_encoder_target.pkl")
feature_encoders = joblib.load("label_encoders_features.pkl")

# Definir a ordem das features exatamente como no treino
FEATURES_ORDER = ['condutor', 'sexo', 'cinto_seguranca', 'Embreagues', 'Idade', 
                  'categoria_habilitacao', 'especie_veiculo', 'pedestre', 'passageiro']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    try:
        # Pré-processamento dos inputs
        processed_data = {}
        for feature in FEATURES_ORDER:
            value = data.get(feature)
            
            if value is None:
                return jsonify({'erro': f'Missing required field: {feature}'}), 400
            
            if feature == 'Idade':
                try:
                    processed_data[feature] = int(value)
                except ValueError:
                    return jsonify({'erro': 'Age must be an integer number'}), 400
            elif feature in feature_encoders:
                try:
                    value_clean = str(value).strip().upper()
                    processed_data[feature] = feature_encoders[feature].transform([value_clean])[0]
                except ValueError:
                    valid_values = list(feature_encoders[feature].classes_)
                    return jsonify({
                        'erro': f'Invalid value for {feature}: {value}',
                        'valid_values': [str(v) for v in valid_values]
                    }), 400

        # Criar DataFrame mantendo a ordem das features
        X_pred = pd.DataFrame([processed_data], columns=FEATURES_ORDER)
        
        # Fazer predição e calcular probabilidade
        pred = modelo.predict(X_pred)[0]
        proba = modelo.predict_proba(X_pred)[0]
        prob_pred = np.max(proba)  # Pega a maior probabilidade

        severidade = target_encoder.inverse_transform([pred])[0]

        return jsonify({
            'severidade_predita': severidade,
            'probabilidade': f"{prob_pred * 100:.2f}%"
        })

    except Exception as e:
        return jsonify({'erro': f'Internal error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

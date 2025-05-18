from flask import Flask, request, jsonify
from utils.preprocess import clean_text
from utils.analyze import analyze_news
import joblib

app = Flask(__name__)
model = joblib.load('models/nlp_model.pkl')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = clean_text(data['text'])
    result = analyze_news(text, model)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

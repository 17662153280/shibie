from flask import Flask, request, jsonify, render_template
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.datasets import imdb

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained model
model = load_model('D:\dev\project\shibie\shibie\sentiment_analysis_model.h5')

# Define maximum length of the input sequences and the vocabulary size
maxlen = 200
num_words = 10000

# Load IMDB word index
word_index = imdb.get_word_index()

# Prepare a reverse word index mapping
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def preprocess_text(text):
    """Preprocess text to be used by the model."""
    # Convert the text to a list of indices
    tokens = text.lower().split()
    sequences = [word_index.get(token, 0) for token in tokens]
    # Pad sequences to the maximum length
    padded_sequences = pad_sequences([sequences], maxlen=maxlen)
    return padded_sequences

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text field provided'}), 400

    text = data['text']
    processed_text = preprocess_text(text)
    prediction = model.predict(processed_text)
    sentiment = 'positive' if prediction[0][0] > 0.5 else 'negative'

    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)

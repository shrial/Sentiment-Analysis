from flask import Flask, request, jsonify
import joblib

app=Flask(__name__)
model = joblib.load('sentiment_analysis_model.joblib')

@app.route('/')
def home():
    # Return a simple JSON response indicating the API is online
    return jsonify({
        'status': 'online',
        'message': 'Sentiment Analysis API is running.'
    })

@app.route('/predict',methods=['POST'])
def predict():
  data = request.get_json(force=True)
  review_text = data['review']
  prediction = model.predict([review_text])
  # The prediction is a numpy array so we get the first item
  output = int(prediction[0])
  if output ==1:
    sentiment='Positive'
  else:
    sentiment='Negative'
  return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
# Sentiment-Analysis
A full-stack web application that classifies the sentiment of a movie review as positive or negative using a machine learning model trained with Scikit-learn.<br>
User enters a movie review on the webpage for analysis. The review is sent to the custom made api which comprises of a machine learning model(Linear SVM) trained to classify the sentiment of a movie review. The sentiment is sent to the frontend and then displayed on the webpage.

## Building and Training the model:
Created Multinomial Naive Bayes model first then worked with Linear Support Vector Machine to get better results.
1. Dataset: Used the 50,000 review IMDB dataset  [Link to the dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
2. Multinomial Naive Bayes model: Made a pipeline and for vectorization, used TF-IDF instead of Count vectorizer. Got an accuracy of 86.35% and size of dataset here was all the 50,000 reviews.
3. Linear Support Vector Machine: Used LinearSVC with ngrams and tfidf on 20,000 reviews to get accuracy of 90.74%.

## Frontend and Building API:
A lightweight Flask API was built to serve the trained model. It accepts review text and returns the predicted sentiment in JSON format.<br>
[Link for the webpage](https://shrial.github.io/Sentiment-Analysis/) <br>
[Link for api created](https://sentiment-analysis-shrika.onrender.com) (Note: this link is for homepage, for model to access endpoint is /predict)

## Tech Stack:
1. ML:
   - Scikit-learn, pandas, NumPy, joblib: for preprocessing data,training and testing the model, and exporting it
   - Matplotlib and seaborn : for visualizing confusion matrix
2. Frontend: HTML, tailwind CSSS, javascript
3. Backend: Python, Flask


Images:
### Confusion Matrix for Multinomial Naive Bayes model
<img width="737" height="611" alt="Screenshot 2025-08-10 203347" src="https://github.com/user-attachments/assets/5181f15d-c026-4118-a404-523ea7403128" />

### Confusion Matrix for Linear SVM (using 50k reviews)
<img width="742" height="618" alt="Screenshot 2025-08-11 002435" src="https://github.com/user-attachments/assets/7eb0435a-36a7-430e-ae74-10e485c8a31b" />

### Confusion Matrix for Linear SVM (using 20k reviews, which is used in the backend of the website)
<img width="742" height="621" alt="Screenshot 2025-08-11 124516" src="https://github.com/user-attachments/assets/f1fde7aa-dc3f-4bc7-80bc-69be5841bfb9" />

### Model prediction when user gave positive feedback 
<img width="740" height="655" alt="Screenshot 2025-08-11 140013" src="https://github.com/user-attachments/assets/7d0fe691-1ad6-4859-b4f4-51f9cc8d4c1d" />

### Model prediction when user gave negative feedback 
<img width="736" height="657" alt="Screenshot 2025-08-11 140042" src="https://github.com/user-attachments/assets/2e80dfb2-cfd0-46b0-8151-109a06137035" />

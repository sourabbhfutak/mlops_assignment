MLOps Assignment - Sentiment Analysis

This project provides an end-to-end pipeline for sentiment analysis on movie reviews, using Scikit-learn, MLflow for experiment tracking, and Flask for creating a REST API. The trained model is deployed using Docker, making it easy to share and run across any system.


Project Structure

mlops_assignment/
│
├── main.py                		# Flask app with prediction endpoint
├── requirements.txt       		# Python dependencies
├── Dockerfile             		# Instructions to build Docker image
├── README.md              		# Project documentation
├── Notebooks/
	├── mlruns/        		# MLflow experiment & model folder (your own model)
	├── ML_teams_Assignment.ipynb 	# Model building file



Features

- Preprocessing using TF-IDF (Unigram + Bigram)
- Classification using Multinomial Naive Bayes
- Model tuning with GridSearchCV
- Experiment logging and model saving using MLflow
- Fully working REST API using Flask
- Packaged and containerized using Docker
- Testable using Postman or curl




API Usage

Endpoint: POST /predict

- URL: http://127.0.0.1:8001/predict
- Headers: Content-Type: application/json
- Body:

{
  "review": "The movie was absolutely amazing!"
}

- Response:

{
  "review": "The movie was absolutely amazing!",
  "sentiment": "positive"
}




Docker Hub

To run the project, following would be required:
Repo name: sourabhfutak/mlops_assignment
docker pull sourabhfutak/mlops_assignment
docker run -p 8001:8001 sourabhfutak/mlops_assignment
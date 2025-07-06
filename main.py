from flask import Flask, request, jsonify
import mlflow.pyfunc
import os

app = Flask(__name__)

# model = mlflow.pyfunc.load_model("final_model/artifacts/04d3b931939a46d5b627c9afd818528b")

# run_model_path = os.path.abspath(r"D:\MTech\Sem2\MLOPs\Assignments\Assignment No. 02\mlops_assignment\Notebooks\mlruns\933201530939966551\04d3b931939a46d5b627c9afd818528b\artifacts\model")
# model = mlflow.pyfunc.load_model(f"file://{run_model_path}")
run_model_path = "Notebooks/mlruns/933201530939966551/04d3b931939a46d5b627c9afd818528b/artifacts/model"
model = mlflow.pyfunc.load_model(run_model_path)

@app.route('/')
def home():
    return "Sentiment Analysis API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print(f"Received data: {data}")
        review = data.get("review", "")

        if not review:
            return jsonify({"error": "Review text is required."}), 400

        prediction = model.predict([review])[0]
        sentiment = "positive" if prediction == 1 else "negative"

        return jsonify({
            "review": review,
            "sentiment": sentiment
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001)

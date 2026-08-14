# Customer Churn Prediction

A machine-learning project that predicts whether a telecom customer is likely to leave the service. It includes a training pipeline, a Streamlit web application, and a FastAPI prediction API.

## Features

- Splits the prepared customer dataset into training and test data.
- Preprocesses numeric and categorical features with imputation, scaling, and one-hot encoding.
- Evaluates several classifiers using recall as the selection metric.
- Saves the selected model and preprocessing pipeline for reuse.
- Provides predictions through Streamlit and FastAPI.

## Project structure

```text
Customer-Churn-prediction/
├── artifact/                         # Generated model, preprocessor, and CSV artifacts
├── notebook/data/pre_process_data.csv # Prepared training dataset
├── schema/user_input.py              # FastAPI input validation schema
├── src/
│   ├── components/                   # Ingestion, transformation, and model training
│   └── pipeline/predict_pipeline.py  # Reusable prediction pipeline
├── main.py                           # Streamlit application
├── model_api.py                      # FastAPI application
├── requirements.txt
└── setup.py
```

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows activation is:

```bash
venv\Scripts\activate
```

## Train the model

From the project root, run:

```bash
python -m src.components.data_ingestion
```

The command reads `notebook/data/pre_process_data.csv`, preprocesses the data, evaluates candidate models, and creates:

```text
artifact/model.pkl
artifact/preprocessor.pkl
```

Run training before starting either application.

## Run the Streamlit application

```bash
streamlit run main.py
```

Open the local URL shown in the terminal, usually `http://localhost:8501`. Enter a customer's information and select **Predict Churn**.

The interface reports one of these results:

- **High churn risk** — the customer is likely to leave the service.
- **Low churn risk** — the customer is likely to stay with the service.

## Run the FastAPI application

```bash
uvicorn model_api:app --reload
```

Open interactive API documentation at `http://127.0.0.1:8000/docs`.

The prediction endpoint is:

```text
POST /predict
```

## Input features

The model uses customer demographics, account details, subscription services, billing details, and charges, including:

`gender`, `SeniorCitizen`, `tenure`, `Contract`, `InternetService`, `PaymentMethod`, `MonthlyCharges`, and `TotalCharges`.

## Notes

- Run all commands from the project root directory.
- Keep `artifact/model.pkl` and `artifact/preprocessor.pkl` together; both are required for prediction.
- The model output depends on the quality and representativeness of the training data and should support, rather than replace, business decisions.

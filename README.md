# AI Prediction Platform

A Streamlit web application developed for an academic project. It brings together two machine-learning tasks in one interface:

1. **Vegetable image classification** — classify images from the first four selected classes of the Kaggle Vegetable Image Dataset.
2. **Tesla stock forecasting** — explore a 20-trading-day ahead forecast of TSLA closing prices using a GRU-based sequence model.

> **Project status:** In development. Models, evaluation results, and app features will be documented as they are implemented and tested.

## Project objectives

- Build and evaluate an image-classification model.
- Build a time-series forecasting model and compare it with a simple baseline.
- Integrate both models into an accessible Streamlit application.
- Document methodology, results, assumptions, and limitations.

## Dataset & data sources

- **Vegetable Image Dataset (Kaggle):** https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset
- **Tesla (TSLA) stock data:** Source and data retrieval approach will be documented when implemented.

The image dataset contains multiple vegetable categories. This project will use only four classes, with the exact classes and split structure confirmed during dataset inspection.

## Planned app modules

### 1. Vegetable image classification
Upload an image and receive a predicted class with model confidence/probabilities. Model performance will be evaluated on held-out data.

### 2. Tesla stock forecasting
Display recent TSLA closing-price history and a forecast for the next 20 **trading days**. Forecasts are experimental and are not financial advice.

## Technology stack

- Python
- TensorFlow / Keras
- Streamlit
- NumPy, Pandas, Matplotlib, scikit-learn

## Run locally

Installation and run instructions will be finalized as the project environment is established.

```bash
streamlit run app.py
```

## Repository structure

The structure will evolve as the models and app are developed. Data and trained model files may be kept locally and excluded from Git when they are large.

## Limitations

- The image model is limited to the four selected dataset classes and may not generalize to images outside the dataset domain.
- Stock forecasts are uncertain; historical prices do not guarantee future performance.
- Model performance and limitations will be reported based on evaluation results, not assumed in advance.

## Author

RosAI-27

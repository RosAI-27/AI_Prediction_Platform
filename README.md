# AI Prediction Platform

An academic Streamlit project bringing together two deep-learning experiments:

1. **Vegetable image classification** — four-class image classification using MobileNetV2 transfer learning.
2. **Tesla (TSLA) stock forecasting** — a 20-trading-day univariate GRU forecasting experiment, evaluated against a persistence baseline.

The repository preserves the experiments and their evaluation records. The Streamlit interface is a work in progress; model integration and deployment are not yet complete.

## 1. Vegetable image classification

**Dataset:** [Kaggle Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)

Four classes were selected: Bean, Bitter_Gourd, Bottle_Gourd, and Brinjal.

| Split | Images per class | Total |
|---|---:|---:|
| Training | 1,000 | 4,000 |
| Validation | 200 | 800 |
| Test | 200 | 800 |
| **Total** | **1,400** | **5,600** |

The selected model uses an ImageNet-pretrained MobileNetV2 backbone with a custom four-class classification head. The pretrained backbone was frozen during the reported training.

**Held-out test results**

| Metric | Result |
|---|---:|
| Accuracy | **99.875% (799/800)** |
| Macro precision | 99.88% |
| Macro recall | 99.88% |
| Macro F1-score | 99.87% |

These results apply to this dataset split; they do not establish near-perfect performance on arbitrary real-world photographs. Dataset-specific patterns and domain shift remain important limitations. See [the detailed evaluation record](docs/vegetable_classifier_evaluation.md).

## 2. Tesla stock forecasting

The notebook downloads daily TSLA OHLCV source data with yfinance using adjusted prices. The evaluated baseline model itself uses only the adjusted Close series.

- Observations: 2,993
- Data period: 2015-01-02 to 2026-11-25
- Lookback: 60 trading days
- Forecast horizon: 20 trading days
- Chronological split: 70% training, 15% validation, 15% test
- Model: GRU with 64 units, Dropout 0.2, and a 20-value output layer

**Held-out test comparison**

| Model | MAE | RMSE |
|---|---:|---:|
| GRU | $27.35 | $35.99 |
| Naive persistence baseline | **$24.94** | **$33.75** |

The GRU did not outperform the simple persistence baseline on this test split. This is an important result: the neural model is an experiment, not a demonstrated improvement over the baseline.

A separate calibration experiment produced 85.37% pooled test coverage for a nominal 90% prediction interval. It therefore did not meet its nominal target. Do not present those intervals as guaranteed uncertainty bounds or transfer its calibration quantiles to the original model. See [the forecasting evaluation record](docs/stock_forecasting_evaluation.md).

Forecasts are experimental and are not financial advice.

## Repository contents

- app.py — Streamlit application entry point.
- pages/ — Streamlit pages; integration is still in progress.
- src/image_classification/ — reusable image data-loading code and class mapping.
- notebooks/ — experiment notebooks and their outputs.
- docs/ — methodology and evaluation records.
- models/ — local model-artifact directory; generated model files are excluded from Git by default.
- data/ — local datasets; raw data is excluded from Git.
- Root-level PNG files — experiment figures awaiting reorganization.

See the [notebook guide](notebooks/README.md) before running the experiments.

## Run locally

Install dependencies in a Python environment:

```bash
pip install -r requirements.txt
```

Launch the current Streamlit entry point:

```bash
streamlit run app.py
```

The current application shell provides the project introduction. Classification and forecasting pages, model loading, and end-to-end inference workflows still need to be implemented and tested.

## Data and model artifacts

Download or generate the datasets locally and place them in the paths expected by the notebooks:

- Vegetable images: data/Vegetables/Vegetable_Images/
- Tesla daily data: data/stock/TSLA_daily.csv
- Model artifacts: models/

Do not commit private data, credentials, or large generated artifacts without deciding how they will be distributed. See .gitignore and models/README.md.

## Limitations

- The classifier supports only four known classes and does not currently reject unknown objects.
- The image test score is dataset-specific; independent external photographs are needed to assess real-world generalization.
- The tested GRU did not beat the naive persistence baseline.
- Financial forecasts are uncertain and should not be used as investment advice.

## Author

RosAI-27

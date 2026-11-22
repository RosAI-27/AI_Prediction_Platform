# AI Prediction Platform

A Streamlit application for two academic machine-learning tasks:

1. **Vegetable image classification** using MobileNetV2 transfer learning.
2. **Tesla (TSLA) stock forecasting** for the next 20 trading days using a GRU-based time-series model.

> **Project status:** Image-classification model trained and evaluated. Tesla forecasting and Streamlit integration are still in progress.

## Project objectives

- Develop and evaluate an image classifier for four selected vegetable classes.
- Build a time-series forecasting model and compare it with a simple baseline.
- Integrate both models into one Streamlit application.
- Document methodology, results, assumptions, and limitations.

## 1. Vegetable image classification

### Dataset

Source: [Kaggle Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)

This project uses the first four classes in the dataset's alphabetical folder order:

- Bean
- Bitter_Gourd
- Bottle_Gourd
- Brinjal

| Split | Images per class | Total images |
|---|---:|---:|
| Training | 1,000 | 4,000 |
| Validation | 200 | 800 |
| Test | 200 | 800 |
| **Total** | **1,400** | **5,600** |

Images are resized to 224 × 224 pixels and represented as RGB tensors. The data loader preserves pixel values in the 0–255 range; MobileNetV2 preprocessing is applied inside the model.

### Model and methodology

The selected model is **MobileNetV2 pretrained on ImageNet**, used through transfer learning:

1. Load MobileNetV2 with ImageNet weights and `include_top=False`.
2. Freeze the pretrained convolutional base.
3. Add Global Average Pooling, a 128-unit ReLU dense layer, Dropout (0.3), and a four-unit Softmax output.
4. Train the classification head using Adam and sparse categorical cross-entropy.
5. Select the checkpoint with the lowest validation loss using ModelCheckpoint and EarlyStopping.

The model contains 2,422,468 parameters: 164,484 trainable and 2,257,986 frozen during the initial transfer-learning stage. Fine-tuning was not required for the reported result.

### Evaluation results

The following results were obtained from the held-out test split:

| Metric | Result |
|---|---:|
| Test accuracy | **99.875%** (799/800) |
| Macro precision | 99.88% |
| Macro recall | 99.88% |
| Macro F1-score | 99.87% |

Per-class test metrics:

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bean | 0.9950 | 1.0000 | 0.9975 | 200 |
| Bitter_Gourd | 1.0000 | 0.9950 | 0.9975 | 200 |
| Bottle_Gourd | 1.0000 | 1.0000 | 1.0000 | 200 |
| Brinjal | 1.0000 | 1.0000 | 1.0000 | 200 |

These metrics describe performance on this particular dataset split; they do not guarantee equivalent performance on arbitrary real-world images. The unusually high score should be interpreted with appropriate caution. An exact-file duplicate audit found no duplicate images across train, validation, and test splits, but that check does not rule out visually near-duplicate images or other dataset-specific biases.

### Model artifacts

The trained model is saved locally as:

`models/best_vegetable_mobilenetv2.keras`

The model weights are not committed to this repository by default. The class-index mapping is maintained in `src/image_classification/class_names.json`.

## 2. Tesla stock forecasting

The planned second module forecasts TSLA closing prices over the next **20 trading days** using a GRU sequence model.

Forecasting methodology, data source, temporal validation, baseline comparison, and evaluation metrics will be documented after implementation. Forecasts are experimental and are not financial advice.

## Technology stack

- Python 3.11
- TensorFlow / Keras
- Streamlit
- NumPy, Pandas, Matplotlib, scikit-learn

## Run locally

Install dependencies in the project environment:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application pages and model-loading code are being completed.

## Repository structure

```text
AI_Prediction_Platform/
├── app.py
├── pages/
├── src/
│   ├── image_classification/
│   └── stock_forecasting/
├── notebooks/
├── data/
├── models/
├── requirements.txt
└── README.md
```

Dataset files and large trained model artifacts should remain local and be excluded from Git where appropriate. See `.gitignore`.

## Limitations

- The image classifier recognizes only the four selected classes; it is not an open-set classifier and may force unfamiliar images into one of those classes.
- Evaluation results depend on the supplied dataset and split. Real-world images may differ in lighting, backgrounds, camera quality, and vegetable varieties.
- Stock forecasts are uncertain; historical prices do not guarantee future performance.

## Author

RosAI-27

# Experiment notebooks

These notebooks are the experiment record for the two project modules. Run them from the repository root unless a notebook explicitly says otherwise, so relative paths such as `data/`, `models/`, and `src/` resolve correctly.

## Image classification

| Notebook | Purpose |
|---|---|
| `01_image_data_preparation.ipynb` | Dataset inspection, selected classes, integrity checks, and input-pipeline validation. |
| `02_cnn_model_development.ipynb` | Initial custom CNN baseline experiment. This is an exploratory record; do not confuse its checkpoint with the selected MobileNetV2 model. |
| `02_mobilenetv2_transfer_learning.ipynb` | MobileNetV2 transfer learning, checkpoint selection, and held-out test evaluation. This produced the currently documented best classifier. |

The selected class order is Bean, Bitter_Gourd, Bottle_Gourd, Brinjal. Keep this order consistent between the data loader, class-index mapping, and model output interpretation.

## Stock forecasting

| Notebook | Purpose |
|---|---|
| `03_tsla_stock_forecasting.ipynb` | TSLA data download and exploration, univariate GRU training, chronological evaluation, naive-baseline comparison, final refit, and a separate calibration experiment. |

The tested GRU did not outperform the persistence baseline. Keep that result visible when presenting the project; do not describe the GRU as a superior forecasting model.

## Notebook hygiene

- Run experiments from a clean, documented environment.
- Preserve chronological ordering in time-series experiments.
- Fit preprocessing transformations on training data only when evaluating models.
- Keep test data out of model selection and calibration decisions.
- Record random seeds, data dates, package versions, and model checkpoints.
- Move stable, reusable code into `src/` only after validating it independently.
- Clear irrelevant temporary outputs before publishing, but preserve outputs that provide evidence for reported results.

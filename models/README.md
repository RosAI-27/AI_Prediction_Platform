# Model artifacts

Generated model files are kept locally and are excluded from Git by default. This avoids committing large binary artifacts or accidentally mixing checkpoints from different experiments.

## Expected local artifacts

### Image classification

- `models/best_vegetable_mobilenetv2.keras` — selected MobileNetV2 classifier used for the reported 99.875% test accuracy.
- `models/best_vegetable_cnn.keras` — separate custom-CNN experiment checkpoint, if retained locally.

### Stock forecasting

- `models/best_tesla_gru.keras` — best checkpoint selected during the original chronological train/validation experiment.
- `models/tesla_gru_final.keras` — final refit model used to generate the 20-session forecast.
- `models/tesla_scaler.pkl` — scaler fitted for that final refit model; it must be loaded with the matching model.
- `models/tesla_gru_calibration_experiment.keras` — separate experimental checkpoint from the calibration experiment. It must not be mixed with the final model or its scaler.

## Reproducibility rules

1. Keep each model paired with the preprocessing objects and class mapping used to train it.
2. Record the source data period, split boundaries, random seed, architecture, training configuration, and evaluation results.
3. Do not overwrite a validated checkpoint with an experimental one.
4. If model binaries need to be distributed, choose an explicit method such as Git LFS or a release asset and document how to retrieve them.
5. Never claim that a saved final-refit model has independent test performance unless it was evaluated on a genuinely held-out test set.

The notebook-only CNN checkpoint currently tracked under `notebooks/models/` is an exploratory artifact, not the selected MobileNetV2 classifier.

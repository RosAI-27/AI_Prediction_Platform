# Model artifacts

Generated model files are kept locally and are excluded from Git by default. This avoids committing large binary artifacts or accidentally mixing checkpoints from different experiments.

## Expected local artifacts

### Image classification

- `models/best_vegetable_mobilenetv2.keras` — selected MobileNetV2 classifier used for the reported 99.875% test accuracy.
- `models/best_vegetable_cnn.keras` — historical custom-CNN experiment checkpoint. Treat it as exploratory, not as the selected classifier.

The separately uploaded `notebooks/models/best_vegetable_cnn.keras` is a distinct file from the local root-level CNN checkpoint (their SHA-256 hashes differ). The CNN notebook's saved-model evaluation output reports 25% test accuracy, so this checkpoint must not be presented as a successful or production-ready classifier without further investigation. Keep the two files separate until their provenance and preprocessing/class-index assumptions are verified.

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

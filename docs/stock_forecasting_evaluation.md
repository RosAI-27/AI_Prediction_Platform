# Tesla stock forecasting — evaluation record

## Data and target

The experiment uses daily TSLA OHLCV data downloaded with yfinance using adjusted prices (`auto_adjust=True`). The original univariate model uses only the adjusted `Close` series.

- Observations: 2,993
- Date range: 2015-01-02 to 2026-11-25
- Lookback: 60 trading days
- Forecast horizon: 20 trading days
- Chronological partitions: 70% training, 15% validation, 15% test
- Scaler: MinMaxScaler fitted on the training partition for the evaluation experiment

The final refit model and its scaler are a matched pair. The final refit was trained using all available historical observations and is not the model used to calculate the independent test metrics below.

## Baseline model

The GRU architecture is:

- Input: (60, 1)
- GRU: 64 units
- Dropout: 0.2
- Dense output: 20 forecast values
- Optimizer: Adam, learning rate 0.001
- Loss: mean squared error

## Held-out test comparison

| Model | MAE | RMSE |
|---|---:|---:|
| GRU | $27.35 | $35.99 |
| Naive persistence | **$24.94** | **$33.75** |

The GRU was approximately 9.7% worse on MAE and 6.6% worse on RMSE than the naive persistence baseline. Therefore, this experiment does not demonstrate that the GRU adds predictive value over simply carrying the last observed closing price forward.

This negative result should remain part of the project narrative. A more complex neural model is not automatically a better forecasting model.

## Final forecast

The final refit uses the complete historical series to produce a 20-trading-session forecast. The forecast dates are derived from the NYSE trading calendar rather than calendar-day offsets.

The final refit's forecast is an illustration of model output, not an independently validated future-performance claim.

## Calibration experiment

A separate experiment used chronological partitions of 60% training, 10% validation, 15% calibration, and 15% test. It generated empirical prediction intervals from calibration residuals.

Reported pooled test coverage was 85.37% for a nominal 90% interval, with a mean interval width of approximately $101.78. The experiment also showed underprediction bias. The observed coverage is below target and should not be described as a guaranteed 90% interval.

Do not transfer calibration quantiles from this separate experimental model to the original GRU or its scaler. The models and preprocessing objects are not interchangeable.

## Limitations and next steps

- The univariate target discards potentially useful OHLCV information.
- The persistence baseline outperformed the GRU on the held-out period.
- Financial time series are non-stationary; historical error distributions may not remain stable.
- Overlapping multi-step forecast windows make pooled residuals dependent.
- A future multivariate experiment should compare OHLCV-only and OHLCV-plus-engineered-feature inputs against the same chronological partitions and simple statistical baselines.
- All preprocessing must be fitted on training data only, with features constructed using information available at each forecast origin.

This is an academic experiment, not financial advice.

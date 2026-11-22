# Vegetable classifier — experiment record

## Objective

Classify images into four selected classes from the Kaggle Vegetable Image Dataset: Bean, Bitter_Gourd, Bottle_Gourd, and Brinjal.

## Data

| Split | Images per class | Total |
|---|---:|---:|
| Train | 1,000 | 4,000 |
| Validation | 200 | 800 |
| Test | 200 | 800 |

Input shape: 224 × 224 × 3, RGB. The input pipeline emits float32 pixel values in [0, 255]. MobileNetV2 preprocessing maps these values to the range expected by its pretrained weights.

An exact SHA-256 duplicate audit found 21,000 images and 20,996 unique files across the full 15-class dataset. Four duplicate pairs were found within the training split, all outside the four selected classes. No exact duplicates were found across the train, validation, and test splits. This does not detect visually similar files with different encodings.

## Model

- Backbone: MobileNetV2, ImageNet pretrained weights.
- Original ImageNet classification head excluded.
- Pretrained backbone frozen during initial training.
- Classification head: GlobalAveragePooling2D → Dense(128, ReLU) → Dropout(0.3) → Dense(4, Softmax).
- Total parameters: 2,422,468.
- Trainable parameters: 164,484.
- Frozen parameters: 2,257,986.
- Optimizer: Adam, initial learning rate 0.001.
- Loss: sparse categorical cross-entropy.
- Callbacks: ModelCheckpoint (best validation loss), EarlyStopping (patience 3, restore best weights), ReduceLROnPlateau.

Training used batch size 8. The best validation-loss checkpoint was selected at epoch 5; training stopped at epoch 8.

## Held-out test results

Test accuracy: **99.875% (799/800)**.

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bean | 0.9950 | 1.0000 | 0.9975 | 200 |
| Bitter_Gourd | 1.0000 | 0.9950 | 0.9975 | 200 |
| Bottle_Gourd | 1.0000 | 1.0000 | 1.0000 | 200 |
| Brinjal | 1.0000 | 1.0000 | 1.0000 | 200 |
| Macro average | 0.9988 | 0.9988 | 0.9987 | 800 |
| Weighted average | 0.9988 | 0.9988 | 0.9987 | 800 |

There was one false negative for Bitter_Gourd and one false positive for Bean. These are the two sides of the same single misclassified sample.

## Interpretation and limitations

The results are excellent on this held-out split, but they should not be interpreted as proof of near-perfect performance on arbitrary images. The dataset is balanced and uses a fixed split; near-duplicates, source-specific patterns, and domain shift may still affect generalization. The exact-duplicate audit does not rule out perceptual duplicates. Before deployment, test the model on independent photographs taken outside the Kaggle dataset and consider an explicit rejection/unknown-class strategy.

The saved model artifact is expected at `models/best_vegetable_mobilenetv2.keras` locally. Large model weights are not stored in this experiment record.

"""Dataset loading utilities for the four-class vegetable image experiment."""

from pathlib import Path

import tensorflow as tf


CLASSES = [
    "Bean",
    "Bitter_Gourd",
    "Bottle_Gourd",
    "Brinjal",
]

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 8
SEED = 42


def load_datasets(data_dir):
    """Load train, validation, and test datasets from class subdirectories."""
    data_dir = Path(data_dir)

    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir / "train",
        class_names=CLASSES,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        label_mode="int",
        shuffle=True,
        seed=SEED,
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir / "validation",
        class_names=CLASSES,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        label_mode="int",
        shuffle=False,
    )

    test_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir / "test",
        class_names=CLASSES,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        label_mode="int",
        shuffle=False,
    )

    autotune = tf.data.AUTOTUNE
    train_ds = train_ds.prefetch(autotune)
    val_ds = val_ds.prefetch(autotune)
    test_ds = test_ds.prefetch(autotune)

    return train_ds, val_ds, test_ds

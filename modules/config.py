from pathlib import Path


class Config:
  RANDOM_SEED = 27
  ASSETS_PATH = Path("../")
  REPO = "~/Users/Gezahegne/10-Accademy/Week-3/pharma_sales_pridiction"
  STORE_PATH = ASSETS_PATH / "data/store.csv"
  TRAIN_PATH = ASSETS_PATH / "data/train.csv"
  TEST_PATH = ASSETS_PATH / "data/test.csv"
  DATASET_PATH = ASSETS_PATH / "data"
  FEATURES_PATH = ASSETS_PATH / "features"
  MODELS_PATH = ASSETS_PATH / "models"
  METRICS_FILE_PATH = ASSETS_PATH / "metrics"
  IMAGE_PATH = ASSETS_PATH / "img"

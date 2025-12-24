import os
from pathlib import Path

# Automatically detect the project root folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings:
    PROJECT_NAME: str = "EcoFish Predictor (Local MVP)"
    
    # Static Assets
    ASSETS_DIR = BASE_DIR / "assets"
    MODEL_PATH = ASSETS_DIR / "model.sav"
    SHAPEFILE_PATH = ASSETS_DIR / "shapefiles" / "MarCNoWA_dissolved.shp"
    
    # Local Data Storage
    DATA_DIR = BASE_DIR / "local_data"
    INPUT_DIR = DATA_DIR / "inputs"
    OUTPUT_DIR = DATA_DIR / "outputs"
    
    # --- THE MISSING LINE WAS HERE ---
    TEMP_DIR = DATA_DIR / "temp"
    # ---------------------------------

    def __init__(self):
        # Auto-create these folders if they don't exist
        os.makedirs(self.INPUT_DIR, exist_ok=True)
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)
        os.makedirs(self.TEMP_DIR, exist_ok=True) # Create temp folder too
        os.makedirs(self.ASSETS_DIR, exist_ok=True)

settings = Settings()
import shutil
import os
import datetime
from app.core.config import settings

class DataManager:
    """
    Manages files locally on the PC. 
    Instead of SFTP, it organizes processed maps into the 'outputs' folder.
    """
    
    def save_prediction(self, source_image_path: str):
        """
        Takes a generated map and archives it into the local_data/outputs folder
        with a timestamp.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"PFZ_Map_{timestamp}.png"
        
        destination_path = os.path.join(settings.OUTPUT_DIR, filename)
        
        try:
            # Move/Copy the file to the permanent output folder
            shutil.copy2(source_image_path, destination_path)
            print(f"✅ Map archived locally at: {destination_path}")
            return destination_path
        except Exception as e:
            print(f"❌ Error archiving map: {e}")
            return None
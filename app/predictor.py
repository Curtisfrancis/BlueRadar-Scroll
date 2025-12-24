import torch
import torch.nn as nn
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import os

# Define the Neural Network Architecture (Must match your saved model)
class FishModel(nn.Module):
    def __init__(self):
        super(FishModel, self).__init__()
        self.fc1 = nn.Linear(5, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.sigmoid(self.fc3(x))
        return x

class Predictor:
    def __init__(self, model_path):
        self.model = FishModel()
        
        # Load the saved weights
        # map_location ensures it loads on CPU even if trained on GPU
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        self.model.eval()

    def generate_prediction(self, input_nc_path, output_image_path):
        # 1. Load Data
        ds = xr.open_dataset(input_nc_path)
        
        # Extract features (adjust variable names if your .nc file is different)
        # We use .get() to avoid crashing if a variable name differs slightly
        sst = ds.get('sst', ds.get('analysed_sst', None))
        chl = ds.get('chl', ds.get('chlor_a', None))
        
        if sst is None: raise ValueError("Could not find SST variable in file")
        
        # Create dummy data for missing features to match 5 inputs
        # (SST, Chl, Salinity, Oxygen, Current) -> We only have SST/Chl usually
        # We flatten the arrays for processing
        data_flat = np.stack([
            sst.values.flatten(),
            chl.values.flatten() if chl is not None else np.zeros_like(sst.values.flatten()),
            np.zeros_like(sst.values.flatten()), # Dummy Salinity
            np.zeros_like(sst.values.flatten()), # Dummy Oxygen
            np.zeros_like(sst.values.flatten())  # Dummy Current
        ], axis=1)

        # 2. Predict
        input_tensor = torch.tensor(data_flat, dtype=torch.float32)
        with torch.no_grad():
            predictions = self.model(input_tensor).numpy()

        # 3. Reshape back to map
        pred_map = predictions.reshape(sst.shape)

        # 4. Generate Image
        plt.figure(figsize=(10, 6))
        plt.imshow(pred_map, cmap='jet', origin='lower')
        plt.colorbar(label='Fishing Potential (0-1)')
        plt.title('Predicted Potential Fishing Zones (PFZ)')
        plt.axis('off')
        
        # Save
        plt.savefig(output_image_path, bbox_inches='tight')
        plt.close()
        
        return output_image_path
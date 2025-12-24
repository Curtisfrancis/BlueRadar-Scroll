import xarray as xr
import os

# Point to your specific file
filename = "local_data/inputs/sample.nc" 

if os.path.exists(filename):
    try:
        ds = xr.open_dataset(filename)
        print("\n✅ FILE FOUND!")
        print("-" * 30)
        print("Variables in this file:")
        for var in ds.data_vars:
            print(f"• {var}")
        print("-" * 30)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
else:
    print(f"❌ File not found at: {filename}")
    print("Please check if 'sample.nc' is inside 'local_data/inputs/'")
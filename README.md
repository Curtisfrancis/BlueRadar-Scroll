
# BlueRadar | Ocean Intelligence on Scroll

> **Decentralized AI fishing zone prediction for the Blue Economy.**

![Scroll](https://img.shields.io/badge/Built%20On-Scroll%20Testnet-blue?style=for-the-badge&logo=ethereum)
![Python](https://img.shields.io/badge/AI%20Engine-Python%203.10-yellow?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-MVP%20Live-success?style=for-the-badge)

##  The Problem
Small-scale artisanal fishermen in West Africa spend up to **60% of their income on fuel** searching blindly for fish. Scientific oceanographic data (Satellite SST & Chlorophyll) exists but is locked behind expensive enterprise subscriptions and complex formats that are inaccessible to the average fisherman.

##  The Solution
**BlueRadar** is a mobile-first "Ocean Intelligence" Dapp that bridges the gap between Marine Earth Observation (EO) data and the artisanal workforce.

1.  **AI-Powered:** Uses Computer Vision to analyze thermal fronts (SST) and predict high-yield Potential Fishing Zones (PFZ).
2.  **Blockchain-Verified:** Built on the **Scroll Testnet**, allowing for transparent, affordable micro-payments (Pay-as-you-Scan) instead of expensive monthly contracts.
3.  **Mobile-First:** Designed as a Progressive Web App (PWA) for low-bandwidth coastal environments.

---

##  Features (MVP)

### 1.  Decentralized Authentication
* Wallet connection via **MetaMask** (Scroll Sepolia Testnet).
* No username/password required; identity is on-chain.

### 2. 🛰️ AI Prediction Engine
* **Input:** Users upload local NetCDF (`.nc`) ocean scan files.
* **Processing:** Python backend reads `thetao` (Sea Water Potential Temperature) and `chl` (Chlorophyll) variables.
* **Output:** Generates a visual Heatmap of high-probability catch zones.

### 3. 💳 Smart Subscriptions
* Users pay a micro-fee in **ETH** to access the AI engine.
* Smart contract validates "Pro Tier" status before processing data.

### 4.  Scan History
* Local browser storage of previous successful scans for offline reference at sea.

---

##  Tech Stack

### **Frontend**
* **HTML5 / Tailwind CSS:** Responsive, mobile-optimized "Deep Ocean" UI.
* **Ethers.js:** Web3 interaction and Smart Contract communication.

### **Backend**
* **Python (FastAPI):** High-performance API server.
* **Xarray / NumPy:** Scientific data processing for NetCDF files.
* **PyTorch / Matplotlib:** AI model inference and heatmap rendering.

### **Blockchain**
* **Network:** Scroll Sepolia Testnet.
* **Contract:** Custom Solidity contract for subscription management.

---

##  Installation & Setup

If you want to run the AI Engine locally, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/BlueRadar-Scroll-Hackathon.git](https://github.com/YOUR_USERNAME/BlueRadar-Scroll-Hackathon.git)
cd BlueRadar-Scroll-Hackathon

2. Set Up Virtual Environment
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Server
uvicorn app.main:app --reload

The app will be live at: http://127.0.0.1:8000




How to Test (Demo Flow)
Connect Wallet: Click the button in the top right. Ensure you are on Scroll Sepolia.

Check Subscription: Go to the "Wallet" tab to see your ETH balance and Tier status.

Upload Data: Go to the "Dashboard", click Select File, and choose a valid .nc file (or use sample.nc in the assets folder).

Run Prediction: Click "Run Prediction" and wait for the AI to render the heatmap.

👥 The Team
We are a multidisciplinary team bridging Marine Science and Software Engineering.

Lead Scientist: Geospatial Data Scientist & Marine EO Expert (GMES & Africa).

Engineering: Full-Stack Web & Embedded Systems Developers.

License
This project is submitted for the Scroll Build Week Hackathon 2025.

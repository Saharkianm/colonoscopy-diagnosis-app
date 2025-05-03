
# Colonoscopy Diagnosis App

This is an AI-powered web application that analyzes colonoscopy images and predicts medical conditions using a pretrained ResNet-18 model.

Built with *Streamlit, **PyTorch, and **FastAPI (optional backend)*, this project demonstrates deep learning in medical image analysis.

---

## Features

- Upload colonoscopy images directly from your browser
- Predicts diagnosis using a trained CNN model (ResNet-18)
- Simple, fast, and interactive UI (Streamlit)
- Optional REST API for integration via FastAPI

---

## Demo

Coming soon — or deploy via Streamlit Share / Hugging Face Spaces / Render.

---

## Folder Structure

colonoscopy-diagnosis-app/
├── app.py # Streamlit frontend
├── main.py # FastAPI backend (optional)
├── model/
│ ├── best_resnet18_colonoscopy.pth
│ └── label2idx.json
├── utils/
│ └── predict.py # Shared model loader and predictor
├── requirements.txt
├── .gitignore
└── README.md


---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Saharkianm/colonoscopy-diagnosis-app.git
cd colonoscopy-diagnosis-app
2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
Usage

Option 1: Run the Streamlit App
streamlit run app.py
Then open in browser: http://localhost:8501

Option 2: Run the FastAPI Backend (Optional)
uvicorn main:app --reload
Visit Swagger UI: http://127.0.0.1:8000/docs

Model Info

Architecture: ResNet-18 (PyTorch)
Input Size: 64×64 RGB images
Classes: [anatomical-landmarks, lower-gi-tract , pathological-findings]
Model is stored in /model/best_resnet18_colonoscopy.pth.

Future Work

Add support for video frames
Improve model accuracy with larger datasets
Deploy to Hugging Face 
Add Docker support
License

MIT License

Acknowledgements

Dataset from hyperkvasir_sampel Dataset for Colonoscopy Image Segmentation
ResNet from torchvision models

---


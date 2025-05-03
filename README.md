# Colonoscopy Diagnosis Web App (FastAPI)

This is a medical image diagnosis web app built with FastAPI. It uses a ResNet-18 model trained on colonoscopy images to classify conditions.

## Features

- Upload colonoscopy images via API
- Model predicts the diagnosis using a pretrained ResNet-18
- REST API with Swagger docs

## Technologies

- Python
- FastAPI
- PyTorch (ResNet18)
- PIL (Pillow)
- Uvicorn (for serving)
- Virtualenv (optional)

## How to Run

1. *Clone the repo:*
   ```bash
   git clone https://github.com/Saharkianm/colonoscopy-diagnosis-app.git
   cd colonoscopy-app
Create & activate virtual environment:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies:
pip install -r requirements.txt
Run the app:
uvicorn main:app --reload
Access the API: Open http://127.0.0.1:8000/docs in your browser.
Model

Architecture: ResNet-18
Format: model/best_resnet18_colonoscopy.pth
Labels: stored in model/label2idx.json
Folder Structure

colonoscopy_app/
├── main.py
├── model/
│   ├── best_resnet18_colonoscopy.pth
│   └── label2idx.json
├── utils/
│   └── predict.py
├── requirements.txt
├── README.md
└── venv/ 

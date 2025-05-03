
import torch
from torchvision import transforms, models
from PIL import Image
import json
from pathlib import Path

# Set base path relative to this file
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "model"

# Load label mapping
with open(MODEL_DIR / "label2idx.json") as f:
    label2idx = json.load(f)
idx2label = {v: k for k, v in label2idx.items()}

# Load model
model = models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, len(label2idx))
model.load_state_dict(torch.load(MODEL_DIR / "best_resnet18_colonoscopy.pth", map_location="cpu"))
model.eval()

# Image transform
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

def predict_image(image: Image.Image) -> str:
    img = transform(image).unsqueeze(0)  # batch dimension
    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs, 1)
        return idx2label[predicted.item()]
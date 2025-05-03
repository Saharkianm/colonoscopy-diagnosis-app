
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from utils.predict import predict_image
from PIL import Image
import io

app = FastAPI(title="Colonoscopy Diagnosis API")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # Predict
        prediction = predict_image(image)
        return {"prediction": prediction}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
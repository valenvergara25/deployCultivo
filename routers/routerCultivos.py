import pickle
from fastapi import APIRouter
from schemas import schemas
import numpy as np

router = APIRouter()

pkl_filename = "RFCultivo.pkl"
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)

labels = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans',
        'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes',
        'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton',
        'jute', 'coffee']

@router.get("/")
async def root():
    return{
        "message": "AI Service Crop - Gabriela Sarria, Valentina Vergara, Farid Melenje"
    }

@router.post("/predict")
def predict_cultivo(data:schemas.Cultivodata):
    data = data.model_dump()
    N = data['N']
    P = data['P']
    K = data['K']
    temperature = data['temperature']
    humidity = data['humidity']
    ph = data['ph']
    rainfall = data['rainfall']

    xin = np.array([N,P,K,temperature,humidity,ph,rainfall]).reshape(1,7)

    prediction = model.predict(xin)

    return {
        'prediction': prediction[0]
    }
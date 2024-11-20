# Точка входа приложения

from fastapi import FastAPI, HTTPException
from ai_integration import generate_sci_bio
from database import create_record, get_record
from schemas import ScientistInput, ScientistOutput

app = FastAPI()

@app.post("/generate", response_model=ScientistOutput)
async def generate_scientist(data: ScientistInput):
    try:
        # Генерация через OpenAI
        bio, image_url = await generate_sci_bio(data)
        # Сохранение в БД
        record_id = create_record(data, bio, image_url)
        return {"id": record_id, "biography": bio, "image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/result/{id}", response_model=ScientistOutput)
def get_scientist_result(id: int):
    record = get_record(id)
    if not record:
        raise HTTPException(status_code=404, detail="Result not found")
    return record

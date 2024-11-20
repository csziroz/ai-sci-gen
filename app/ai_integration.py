# Логика работы с OpenAI API

import openai

openai.api_key = "your-openai-api-key"

async def generate_sci_bio(input_data):
    # Генерация текста через GPT
    bio_prompt = (
        f"Create a short biography of a futuristic scientist:\n"
        f"Gender: {input_data.gender}\n"
        f"Age: {input_data.age}\n"
        f"Field: {input_data.field}\n"
        f"Personality: {input_data.personality}\n"
        f"Appearance: {input_data.appearance}\n"
    )
    bio_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=bio_prompt,
        max_tokens=150,
    )
    biography = bio_response["choices"][0]["text"].strip()

    # Генерация изображения через DALL-E
    image_prompt = (
        f"A portrait of a futuristic scientist: "
        f"{input_data.gender}, age {input_data.age}, working in {input_data.field}, "
        f"characterized as {input_data.personality}, appearance: {input_data.appearance}."
    )
    image_response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="1024x1024",
    )
    image_url = image_response["data"][0]["url"]

    return biography, image_url

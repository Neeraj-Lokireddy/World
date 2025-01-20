from fastapi import FastAPI
# from googletrans import Translator
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
# translator = Translator()
hello_world_translations = [
    {"language": "English", "language_code": "en", "translation": "Hello, World!"},
    {"language": "Spanish", "language_code": "es", "translation": "Hola, Mundo"},
    {"language": "French", "language_code": "fr", "translation": "Bonjour le Monde"},
    {"language": "German", "language_code": "de", "translation": "Hallo, Welt"},
    {"language": "Italian", "language_code": "it", "translation": "Ciao, Mondo"},
    {"language": "Portuguese", "language_code": "pt", "translation": "Olá, Mundo"},
    {"language": "Russian", "language_code": "ru", "translation": "Привет, мир"},
    {"language": "Chinese (Simplified)", "language_code": "zh-cn", "translation": "你好，世界"},
    {"language": "Arabic", "language_code": "ar", "translation": "مرحبًا بالعالم"},
    {"language": "Japanese", "language_code": "ja", "translation": "こんにちは、世界"},
    {"language": "Korean", "language_code": "ko", "translation": "안녕하세요, 세계"}
]

@app.get("/translate/")
async def translate_text(target_lang: str):
    for i in hello_world_translations:
        print(i["language_code"])
        if(i["language_code"]==target_lang):
            return {"trans": i["translation"]}
    return {"trans": "No possible translation found"}

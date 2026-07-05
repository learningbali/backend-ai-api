from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Mencegah error CORS dari browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. RUTE TESTING: Untuk mengecek apakah Vercel Anda hidup
@app.get("/")
def read_root():
    return {"status": "BERHASIL! Backend Vercel Menyala 🚀"}

# 2. RUTE UTAMA: Untuk memproses video
@app.post("/api/process-video")
async def process_video(
    youtube_url: str = Form("Kosong"),
    style_preference: str = Form("dokumenter")
):
    base = "Ultra-Realistic Cinematic ASMR Commercial. Photorealistic, 8K quality, Editorial product photography. "
    neg = "No music. No dialogue. No face visible."
    
    # Kita kembalikan format JSON murni
    return [
        {
            "timecode": "0:00 - 0:02", 
            "prompt": f"{base} [{style_preference}] Macro close-up of a precision screwdriver tightening a screw into a diecast sports car. {neg}"
        },
        {
            "timecode": "0:03 - 0:04", 
            "prompt": f"{base} [{style_preference}] Extreme close-up of vintage metal model train wheels locking onto tracks. {neg}"
        }
    ]

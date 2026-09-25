import os
import shutil
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Universal Python File Organizer API")

os.makedirs("uploads", exist_ok=True)

# Universal category mapping covering hundreds of extensions
EXTENSIONS_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods", ".json", ".xml"],
    "Presentations": [".ppt", ".pptx", ".key"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".ts", ".go", ".rs", ".sql"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Video": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg", ".deb"]
}

def get_category(filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()
    for cat, exts in EXTENSIONS_MAP.items():
        if ext in exts:
            return cat
    return "Others"

class LocalPathRequest(BaseModel):
    path: str

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/api/organize-local")
def organize_local(req: LocalPathRequest):
    if not os.path.exists(req.path):
        raise HTTPException(status_code=400, detail="Invalid directory path.")
    moved, results = 0, []
    for filename in os.listdir(req.path):
        file_path = os.path.join(req.path, filename)
        if os.path.isdir(file_path): continue
        cat = get_category(filename)
        cat_dir = os.path.join(req.path, cat)
        os.makedirs(cat_dir, exist_ok=True)
        dest = os.path.join(cat_dir, filename)
        if not os.path.exists(dest):
            shutil.move(file_path, dest)
            moved += 1
            results.append({"file": filename, "category": cat})
    return {"status": "success", "moved_count": moved, "details": results}

@app.post("/api/organize-upload")
async def organize_upload(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        cat = get_category(file.filename)
        cat_folder = os.path.join("uploads", cat)
        os.makedirs(cat_folder, exist_ok=True)
        with open(os.path.join(cat_folder, file.filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        results.append({"file": file.filename, "category": cat})
    return {"status": "success", "moved_count": len(files), "details": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
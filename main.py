import os
import shutil

# change this to your pathname
os.chdir('D:/Downloads')

if not os.path.exists("PDF"):
    os.mkdir("PDF")

if not os.path.exists("WORD"):
    os.mkdir("WORD")

if not os.path.exists("EXE"):
    os.mkdir("EXE")

if not os.path.exists("ZIP"):
    os.mkdir("ZIP")

if not os.path.exists("MEDIA"):
    os.mkdir("MEDIA")
media_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff", ".webp", ".webm", ".mp4", ".avi", ".m4v", ".wmv", ".mov")


for file in os.listdir():

    if file.lower().endswith(".pdf"):
        shutil.move(file, "PDF")

    elif file.lower().endswith(".docx"):
        shutil.move(file, "WORD")

    elif file.lower().endswith(".exe"):
        shutil.move(file, "EXE")

    elif file.lower().endswith(".zip"):
        shutil.move(file, "ZIP")
    
    elif file.lower().endswith(media_extensions):
        shutil.move(file, "MEDIA")

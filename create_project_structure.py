import os

# Root directory
root_dir = "shl-assessment-recommender"

# Folder structure and files
structure = {
    "app": [
        "scraper.py",
        "recommender.py",
        "embedding_model.py",
        "utils.py"
    ],
    "api": [
        "main.py"
    ],
    "data": [],
    "": [
        "streamlit_app.py",
        "requirements.txt",
        "README.md",
        "approach.pdf"
    ]
}

# Create folders and files
for folder, files in structure.items():
    folder_path = os.path.join(root_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, "w") as f:
            pass

print(f"Project structure for '{root_dir}' created successfully!")
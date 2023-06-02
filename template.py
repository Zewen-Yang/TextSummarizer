import os
from pathlib import Path
import logging


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

    project_name = "TextSummarizer"

    list_files = [
        ".github/workflows/.gitkeep",  # to prevent git from deleting the folder
        "src/__init__.py",
        "src/components/__init__.py",
        "src/utils/__init__.py",
        "src/utils/common.py",
        "src/logging/__init__.py",
        "src/config/__init__.py",
        "src/config/configuration.py",
        "src/pipeline/__init__.py",
        "src/entity/__init__.py",
        "src/constants/__init__.py",
        "config/config.yaml",
        "params.yaml",
        "app.py",
        "main.py",
        "Dockerfile",
        "requirements.txt",
        "setup.py",
        "notebook/trial.ipynb",
    ]

    for file_path in list_files:
        file_path = Path(file_path)
        file_dir, file_name = os.path.split(file_path)

        if file_dir != "":
            os.makedirs(file_dir, exist_ok=True)
            logging.info(f"Creating directory:{file_dir} for the file {file_name}")

        
        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path,'w') as f:
                pass
                logging.info(f"Creating empty file: {file_path}")
        else:
            logging.info(f"{file_name} is already exists")
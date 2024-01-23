import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s: %(message)s:]')

files=[
    ".github/workflows/.gitkeep",
    f"src/code/__init__.py",
    f"src/code/components/__init__.py",
    f"src/code/utils/__init__.py",
    f"src/code/utils/common.py",
    f"src/code/logging/__init__.py",
    f"src/code/config/__init__.py",
    f"src/code/config/config.py",
    f"src/code/pipeline/__init__.py",
    f"src/code/entity/__init__.py",
    f"src/code/constants/__init__.py",
    "configs/config.yaml",
    "param.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "experiments/trails.ipynb",
    "templates/index.html",
    "dvc.yaml"
]

for file in files:
    file_path=Path(file)
    fdir,fname=os.path.split(file_path)

    if fdir!="":
        os.makedirs(fdir,exist_ok=True)
        logging.info(f"Creating directory: {fdir} for the file {fname}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{fname} already exists!!")
    

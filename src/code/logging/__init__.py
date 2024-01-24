import os
import sys
import logging

log="[%(asctime)s: %(levelname)s: %(module)s] %(message)s"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= log,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

LogTool = logging.getLogger("PCBLogger")
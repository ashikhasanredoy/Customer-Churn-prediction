import logging
import os
from datetime import datetime

log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.logs"
logs_folders=os.path.join(os.getcwd(),"logs")

os.makedirs(logs_folders, exist_ok=True)

log_file_path=os.path.join(logs_folders, log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logging.info("Logger initialized successfully")
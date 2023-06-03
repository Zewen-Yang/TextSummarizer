import os
import sys
import logging
from datetime import datetime


log_dir = "logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"
logging_str = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(module)s: %(message)s"  # modify this later
# logging_str = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"

#os.getcwd(): get the current working directory of a process
log_filepath = os.path.join(os.getcwd(), log_dir, LOG_FILE)
os.makedirs(log_filepath, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_filepath, LOG_FILE)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("TextSummarizerLogger")  # give the logger a name
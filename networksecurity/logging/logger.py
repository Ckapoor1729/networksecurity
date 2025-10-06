import os
import logging
from datetime import datetime

# Create logs directory if not present
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name with timestamp
LOG_FILE = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logger
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

# Create logger instance
logger = logging.getLogger("mlproject")



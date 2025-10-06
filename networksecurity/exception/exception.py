import sys
from networksecurity.logging.logger import logger

def error_message_detail(error, error_detail: sys):
    """Return detailed error message with file and line number."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error in '{file_name}', line {line_number}: {str(error)}"
    return error_message

class CustomException(Exception):
    """Custom exception class that logs the error automatically."""
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
        logger.error(self.error_message)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        logger.info("Testing custom exception")
        a = 1 / 0
        logger.info("tested")
    except Exception as e:
        raise CustomException(e, sys)   
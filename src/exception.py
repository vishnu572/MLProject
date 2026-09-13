import sys
import logging


def error_message_details(error_message, error_details: sys):
    _, _, exc_tab = error_details.exc_info()
    file_name = exc_tab.tb_frame.f_code.co_filename
    return (
        f"Error occurred in python script name [{file_name}] line number [{exc_tab.tb_lineno}] "
        f"error message [{error_message}]"
    )


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details=error_detail)

    def __str__(self):
        return self.error_message
    
    
if __name__ == "__main__":
    try:
        a = 5/0
        
    except Exception as e:
        logging.info("zero division error")
        raise CustomException(e,sys)
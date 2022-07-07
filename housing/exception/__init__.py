import os,sys

class ExceptionHendler(Exception):
    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message = ExceptionHendler.get_detailed_error_message(error_message=error_message,error_detail=error_detail)

    @staticmethod

    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:

        _,_,exec_tb = error_detail.exc_info()

        error_occured_in_file =exec_tb.tb_frame.f_code.co_filename
        try_block_file_number = exec_tb.tb_lineno
        Exception_block_line_number = exec_tb.tb_frame.f_lineno

        error_message = f"""error occure in file : [{error_occured_in_file}]
        at Try block line Number : [{try_block_file_number}] and
        Exception_block_line_number : [{Exception_block_line_number}]
          Error_message is : [{error_message}]        
        """
        return error_message

    def __str__(self)->str:
        return self.error_message

    def __repr__(self)->str:
        return ExceptionHendler.__name__.str()
        
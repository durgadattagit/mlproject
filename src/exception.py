import sys
import logging

def error_masage_detail(error,error_detail:sys): 
    _,_,exc_tb=error_detail.exc_info()
    # for execption handling documentetion
    file_name =exc_tb.tb_frame.f_code.co_filename
    error_masage="Error occured in python script name [{0}] linenumber [{0}] error masage[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_masage

    


class Customexception(Exception):
    def __inir__(self,error_masage,error_detail:sys):
        super().__init__(error_masage)
        self.error_masage = error_masage_detail(error_masage,error_detail = error_detail)

    def __str__(self):
        return self.error_masage
    

# # just cheak for it run or nut
#     if __name__ =="__main__":
#         try:
#             a=1/0
#         except Exception as e:
#              logging.info("Devide by Zero")
#              raise CustomException(e,sys)
        
            
       
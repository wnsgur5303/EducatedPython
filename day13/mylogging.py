import logging
from day11.myFlask01 import param

if __name__ == '__main__':
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    mylogger.addHandler(stream_hander)
    
    

    file_handler = logging.FileHandler('my.log')
    file_handler.setFormatter(stream_hander)
    
    mylogger.addHandler(file_handler)
    mylogger.debug("^^")
    mylogger.info("server start!!!")
    mylogger.warning("w")
    mylogger.error("e")
    mylogger.fatal("\[T]/")
    
    
    #오늘 숙제 플라스크 2에서 들어올 때마다 로그로 남겨주기
#     /param
#     log/param
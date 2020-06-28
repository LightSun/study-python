# coding:utf-8
import logging  

# logging.debug('debug message')  
# logging.info('info message')  
# logging.warning('warning message')  # 默认日志级别warn
# logging.error('error message')  
# logging.critical('critical message')  

print "============== start config =============="

logging.basicConfig(level=logging.DEBUG
                    ,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='test.log',  
                    filemode='w'
                    )  
  
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message')  
# coding:utf-8

# 日志相关
import logging as lg;

LEVEL_DEBUG    = 1;
LEVEL_INFO     = 2;
LEVEL_WRAN     = 3;
LEVEL_ERROR    = 4;
LEVEL_CRITICAL = 5; # 危险


# def logTMS(tag, method, msg, logLevel = LEVEL_DEBUG):
#     Logger(tag).logTMS(method, msg, logLevel);

def _getExactLevel(argument):
    switcher = {
        LEVEL_DEBUG: lg.DEBUG,
        LEVEL_INFO: lg.INFO,
        LEVEL_WRAN: lg.WARN,
        LEVEL_ERROR: lg.ERROR,
        LEVEL_CRITICAL: lg.CRITICAL,
    }
    return switcher.get(argument, lg.WARN)   

def _logImpl(level, msg):
    msg = _getIndention(level) + msg;
    if(level == LEVEL_DEBUG):
        lg.debug(msg);
    elif(level == LEVEL_INFO):
        lg.info(msg);
    elif(level == LEVEL_WRAN):
        lg.warn(msg);
    elif(level == LEVEL_ERROR):
        lg.error(msg);
    elif(level == LEVEL_CRITICAL):
        lg.critical(msg);
    else:    
        lg.warn("unknow log level = %s" % level); 

def _getIndention(level):
    switcher = {
        LEVEL_DEBUG: "   ",
        LEVEL_INFO: "    ",
        LEVEL_WRAN: " ",
        LEVEL_ERROR: "   ",
        LEVEL_CRITICAL: "",
    } 
    return switcher.get(level, "");          


class Logger:
    
    def __init__(self, tag):  # 重载构造函数
        self.__tag = tag;     # 创建成员变量并赋初始值
        self.__logLevel = LEVEL_DEBUG;

    def setLogLevel(self, level1, syncSysLog = False):
        self.__logLevel = level1;  
        if syncSysLog:
            lg.basicConfig(level=_getExactLevel(level1)); 
            
    def isLogEnable(self,logLevel):    
        return logLevel >= self.__logLevel;
    
    def logTS(self, msg, logLevel = LEVEL_INFO):
        message = " == IN %s ==, %s" % (self.__tag, msg);  
        self.__logInternal(message, logLevel);
        
    def logTMS(self, method, msg, logLevel = LEVEL_INFO):
        message = " == IN %s ==, called [ %s() ]:\n     %s" % (self.__tag, method, msg);  
        self.__logInternal(message, logLevel);
            
    # =============== start internal method =======================
            
    def __logInternal(self, message, logLevel):
        if( self.isLogEnable(logLevel)):
            _logImpl(logLevel, message);
            
class _EmptyLog(Logger):         
    def logTS(self, msg, logLevel = LEVEL_INFO):
        type(msg)
  
    def logTMS(self, method, msg, logLevel = LEVEL_INFO): 
        type(msg)     
        
EMPTY_LOG = _EmptyLog("Empty");     
DEFAULT_LOG = Logger("default");    
            
"""
 def logTS(self, msg, logLevel = LEVEL_DEBUG):
        if( logLevel >= self.__logLevel):
            message = "== IN %s ==, %s" % (self.__tag, msg);  
            lg.log(_getExactLevel(logLevel), message) ;
            
"""
""" === test case ========
log = Logger("Tag1")
log.setLogLevel(LEVEL_DEBUG, True);
log.logTS("msg_debug", LEVEL_DEBUG);
log.logTS("msg_info", LEVEL_INFO);
log.logTS("msg_warn", LEVEL_WRAN);
log.logTS("msg_error", LEVEL_ERROR);
log.logTS("msg_debug", LEVEL_CRITICAL);
"""

import os
import yaml
import logging
import logging.config
import time

TRACE_LEVELV_NUM = 9
# DB_TRACE_LEVELV_NUM =11
# DB_MATRIX_LEVELV_NUM =12
# CONF_RESPONSES_LEVEL_NUM = 13
# CONTROL_RESPONSE_LEVEL_NUM = 15
# DEBUG_CONTROLLING_LEVEL_NUM = 16
logging.addLevelName(TRACE_LEVELV_NUM, "TRACE")
# logging.addLevelName(DB_TRACE_LEVELV_NUM, "DB_TRACE")
# logging.addLevelName(DB_MATRIX_LEVELV_NUM, "DB_MATRIX")
# logging.addLevelName(CONF_RESPONSES_LEVEL_NUM, "CONF_RESPONSES")
# logging.addLevelName(CONTROL_RESPONSE_LEVEL_NUM, "CONTROL_RESPONSES")
# logging.addLevelName(DEBUG_CONTROLLING_LEVEL_NUM, "DEBUG_CONTROLLING")


def trace(self, message, *args, **kws):
    self._log(TRACE_LEVELV_NUM, message, args, **kws) 
logging.Logger.trace = trace

# def db_trace(self, message, *args, **kws):
#     self._log(DB_TRACE_LEVELV_NUM, message, args, **kws) 
# logging.Logger.db_trace = db_trace   

# def db_matrix(self, message, *args, **kws):
#     self._log(DB_MATRIX_LEVELV_NUM, message, args, **kws) 
# logging.Logger.db_matrix = db_matrix   

# def conf_responses(self, message, *args, **kws):
#     self._log(CONF_RESPONSES_LEVEL_NUM, message, args, **kws) 
# logging.Logger.conf_responses = conf_responses

# def control_responses(self, message, *args, **kws):
#     self._log(CONTROL_RESPONSE_LEVEL_NUM, message, args, **kws) 
# logging.Logger.control_responses = control_responses

# def debug_controlling(self, message, *args, **kws):
#     self._log(DEBUG_CONTROLLING_LEVEL_NUM, message, args, **kws) 
# logging.Logger.debug_controlling = debug_controlling

def setup_logging():
    path = os.path.join('utils', 'logging.yaml')
    print(f"Looking for logging configuration file at: {path}")
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                logging.Formatter.converter = time.gmtime
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
    else:
        print('Failed to load configuration file. Using default configs')

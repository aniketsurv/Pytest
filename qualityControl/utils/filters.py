import logging

class info_filter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.INFO

class debug_filter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.DEBUG

# class warn_filter(logging.Filter):
#     def filter(self, rec):
#         return rec.levelno == logging.WARN

class error_filter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.ERROR

# class critical_filter(logging.Filter):
#     def filter(self, rec):
#         return rec.levelno == logging.CRITICAL
    
class trace_filter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == 9
# class db_trace_filter(logging.Filter):
#     def filter(self, rec):
#         return rec.levelno == 11
# class db_matrix_filter(logging.Filter):
#     def filter(self, rec):
#         return rec.levelno == 12
# class conf_response_filter(logging.Filter):
#     def filter(self, rec):
#         return rec.levelno == 13
# class control_response_filter(logging.Filter):
#     def filter(self, rec):
#         return rec.levelno == 15
# class debug_controlling_filter(logging.Filter):
#     def filter(self, rec):
#         return rec.levelno == 16
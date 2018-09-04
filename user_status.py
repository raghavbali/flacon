from flask_table import Table, Col

class USER_STATUS(Table):
    classes = ['table table-striped','table-hover','table-responsive-md']
    thead_classes = ["thead-dark"]
    USER = Col('USER')
    PID = Col('PID')
    CPU_UTILIZATION = Col('CPU_UTILIZATION')
    MEMORY_UTILIZATION = Col('MEMORY_UTILIZATION')
    VSZ = Col('VSZ')
    RSS = Col('RSS')
    TTY = Col('TTY')
    STAT = Col('STAT')
    START = Col('START')
    TIME = Col('TIME')
    COMMAND = Col('COMMAND')

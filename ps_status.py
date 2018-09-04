from flask_table import Table, Col, LinkCol

class PS_STATUS(Table):
    classes = ['table table-striped','table-hover','table-responsive-md']
    thead_classes = ["thead-dark"]
    USER = Col('USER')
    CPU_UTILIZATION = Col('CPU_UTILIZATION')
    MEMORY_UTILIZATION = Col('MEMORY_UTILIZATION')
    VSZ = Col('VSZ')
    RSS = Col('RSS')
    DETAILS = LinkCol('Details', 'get_user_status',
                      url_kwargs=dict(user='USER'))

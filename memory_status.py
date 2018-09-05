from flask_table import Table, Col

class MEMORY_STATUS(Table):
    classes = ['table table-striped','table-hover','table-responsive-sm']
    thead_classes = ["thead-dark"]
    TOTAL = Col('TOTAL')
    USED = Col('USED')
    FREE = Col('FREE')
    SHARED = Col('SHARED')
    CACHE = Col('CACHE')
    AVAILABLE = Col('AVAILABLE')

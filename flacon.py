################################
# import
################################


import json
import platform as pl
#import datetime

import pandas as pd
from flask import Flask, render_template

from ps_status import PS_STATUS
from user_status import USER_STATUS
from memory_status import MEMORY_STATUS

#from utils import get_overall_stats,get_memory_stats,get_user_stats


################################
# SETUP
################################
app = Flask(__name__,
            static_folder='static',
            static_url_path='')

with open(r'config.json') as f:
    config = json.load(f)

config['OS'] = pl.platform()
config['Processor'] = pl.processor()

#today_value = str(datetime.date.today())
#today_value = today_value.replace('-','_')


################################
# SERVER ENDPOINTS
################################

@app.route('/', methods=['GET'])
def get_home():
    return render_template(
            'index.html',
            config_details = config,
            )

@app.route('/ps_status', methods=['GET'])
def get_ps_status():
    temp_table_data = pd.DataFrame(data=[{'USER':'rbali2',
                                          'CPU_UTILIZATION':'10%',
                                          'MEMORY_UTILIZATION':'40%',
                                          'VSZ':100,
                                          'RSS':200}])
    return render_template(
            'ps_tables.html',
            table=PS_STATUS(temp_table_data.to_dict(orient='records')),#get_overall_stats().to_dict(orient='records')),
            config_details = config,
            )

@app.route('/<string:user>', methods=['GET'])
def get_user_status(user):
    temp_table_data = pd.DataFrame(data=[{'USER':'rbali2',
                                          'CPU_UTILIZATION':'10%',
                                          'MEMORY_UTILIZATION':'40%',
                                          'PID':123,
                                          'VSZ':100,
                                          'RSS':200,
                                          'TTY':'pts/1',
                                          'STAT':'S',
                                          'START':'10:20',
                                          'TIME':10,
                                          'COMMAND':'TEST_COMMAND'}])
    return render_template(
            'ps_tables.html',
            table=USER_STATUS(temp_table_data.to_dict(orient='records')),#get_user_stats().to_dict(orient='records')),
            config_details = config,
            )

@app.route('/memory_status', methods=['GET'])
def get_memory_status():

    temp_table_data = pd.DataFrame(data=[{'TOTAL':400,
                                          'USED':160,
                                          'FREE': 40,
                                          'CACHE':123,
                                          'SHARED':100,
                                          'AVAILABLE':200}])
    return render_template(
            'ps_tables.html',
            table=MEMORY_STATUS(temp_table_data.to_dict(orient='records')),#get_memory_stats().to_dict(orient='records')),
            config_details = config,
            )


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6190,debug=True)

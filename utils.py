import gc
import re
import subprocess
import pandas as pd

################################
# UTILS
################################

def get_overall_stats():
    cmd=["ps","aux"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    list_df=[]
    header = proc.stdout.readline().decode('utf-8')
    regex_header=re.sub(pattern='[ ]+',string=header,repl='||')
    size=len(regex_header.split("||"))
    for line in proc.stdout.readlines():
        regex_row=re.sub(pattern='[ ]+',string=line.decode('utf-8'),repl='||',count=(size-1))
        list_df.append(regex_row.split("||"))

    df_ps=pd.DataFrame(columns=regex_header.split('||'),data=list_df)
    df_ps = df_ps[['USER','%CPU','%MEM','VSZ','RSS']]

    for col in df_ps.columns:
        try:
            df_ps[col]=df_ps[col].astype('float64',copy=False)
        except:
            None
    df_ps=df_ps.groupby('USER').agg('sum').reset_index()

    return df_ps

def get_user_stats(user):
    gc.collect()
    cmd=["ps","aux"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    list_df=[]
    header = proc.stdout.readline().decode('utf-8')
    regex_header=re.sub(pattern='[ ]+',string=header,repl='||')
    size=len(regex_header.split("||"))
    for line in proc.stdout.readlines():
        regex_row=re.sub(pattern='[ ]+',string=line.decode('utf-8'),repl='||',count=(size-1))
        list_df.append(regex_row.split("||"))

    df_ps=pd.DataFrame(columns=regex_header.split('||'),data=list_df)
    df_ps=df_ps[df_ps.USER==user]
    for col in df_ps.columns:
        try:
            df_ps[col]=df_ps[col].astype('float64',copy=False)
        except:
            None
    return df_ps

def get_memory_stats():
    gc.collect()
    cmd=["free","-h"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    list_df=[]
    header = proc.stdout.readline().decode('utf-8')
    regex_header=re.sub(pattern='[ ]+',string=header,repl='||')
    size=len(regex_header.split("||"))
    for line in proc.stdout.readlines():
        regex_row=re.sub(pattern='[ ]+',string=line.decode('utf-8'),repl='||',count=(size-1))
        list_df.append(regex_row.split("||"))

    return pd.DataFrame(columns=regex_header.split('||'),data=list_df)

import os
import pandas as pd
import shutil
from datetime import datetime
import glob
import time
from pandas.core.arrays.categorical import contains
from pandas.io.pytables import IndexCol

import urllib.parse
root=os.environ['HomePath'] + "\\source\\repos\\legal"
# single function to initialize the state
source_path=root + "\\inbox"
target_path=root + "\\files"
files_to_copy=os.listdir(source_path)

def inspect_files(folder_path):
    files=listdir(folder_path)
    for f in files:
        print(path)

def move_or_copy_files(source,target):
    for f in files_to_copy:
        new_file=shutil.move(source_path + "\\" + f,target_path)
        print(f)

def get_list_of_files(dir_name,search_for='*'):
   
    execution_time=datetime.utcnow()
    
    file_names=[]
    last_modifieds=[]
    last_accessed=[]
    file_sizes=[]
    urls=[]
    absolute_url=r'https://github.com/mconsulting/legal/blob/main/files/'
    for file_name in os.listdir(dir_name):
        last_modifieds.append(time.strftime(  '%Y-%m-%d %H:%M:%S',
                                    time.gmtime(os.path.getmtime(dir_name + "\\" + file_name))) )
        last_accessed.append(time.strftime(  '%Y-%m-%d %H:%M:%S',
                                    time.gmtime (os.path.getatime(dir_name + "\\" + file_name))) )
        modified_time=os.path.getmtime(dir_name + "\\" + file_name)
        changed_time=os.path.getctime(dir_name + "\\" + file_name)
        accessed_time=os.path.getatime(dir_name + "\\" + file_name)
        file_sizes.append(os.path.getsize(dir_name + "\\" + file_name))
        file_names.append(file_name)
        urls.append(absolute_url + urllib.parse.quote(file_name))
    file_info={'file_name':file_names,'last_modified':last_modifieds,'last_accessed':last_accessed,'file_size':file_sizes,'url':urls}

    df=pd.DataFrame(file_info)
    df.to_csv(root + '\\files.csv')
    print(df)
        
    return df

def add_links(list_of_files):
    # This is a dataframe not a list.  
    # That will enable 
    df=list_of_files
    print
    f=open(root + "\\links.md","w")
    i=0
    f.write("## Links")
    f.write('\n\n')

    f.write(str(datetime.utcnow()))
    f.write('\n\n')
    for i in range(1,len(df)):
        link=df.iloc[i]["url"]
        fn=df.iloc[i]["file_name"]
        newline=str.format('[{}]({})',fn,link)
        f.write(newline +'\n')
        f.write('\n')
       
    f.close()


move_or_copy_files(source_path,target_path)

files_to_link= get_list_of_files(target_path)

add_links(files_to_link)



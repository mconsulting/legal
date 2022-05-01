import os
import pandas as pd
import shutil
from datetime import datetime
import glob
import time
from pandas.io.pytables import IndexCol


# single function to initialize the state
source_path=os.getcwd() + "\\inbox"
target_path=os.getcwd() + "\\files"
files_to_copy=os.listdir(source_path)

def inspect_files(folder_path):
    files=listdir(folder_path)
    for f in files:
        print(pathf)

def move_or_copy_files(source,target):
    for f in files_to_copy:
      #  new_file=shutil.move(source_path + "\\" + f,target_path)
        print(f)

def get_list_of_files(dir_name,search_for='*'):
   
    execution_time=datetime.utcnow()
    # Get list of all files only in the given directory
    list_of_files = filter( os.path.isfile,
                            glob.glob(dir_name) )
    # Sort list of files based on last modification time in ascending order
    list_of_files = sorted( list_of_files,
                            key = os.path.getmtime)
    # Iterate over sorted list of files and print file path 
    # along with last modification time of file 

    file_names=[]
    last_modifieds=[]
    file_sizes=[]

    
    for file_name in os.listdir(target_path):
        last_modifieds.append(time.strftime(  '%Y-%m-%d_%H%M%S',
                                    time.gmtime(os.path.getmtime(target_path + "\\" + file_name))) )
        modified_time=os.path.getmtime(target_path + "\\" + file_name)
        changed_time=os.path.getctime(target_path + "\\" + file_name)
        accessed_time=os.path.getatime(target_path + "\\" + file_name)
        file_sizes.append(os.path.getsize(target_path + "\\" + file_name))
        file_names.append(file_name)
    
    file_info={'file_name':file_names,'last_modified':last_modifieds,'file_size':file_sizes}

    df=pd.DataFrame(file_info)
    df.to_csv('resources.csv')
    print(df)
        
    return list_of_files

dlist=get_list_of_files(target_path)

file_dictionary={'file_name':dlist}


df=pd.DataFrame(data=file_dictionary)
print(df)
move_or_copy_files(source_path,target_path)

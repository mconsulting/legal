import os
import pandas as pd
import shutil


source_path=r"C:\Users\mason\Mason Consulting\Mason Prepaid - Documents\civil rights\wip"
target_path=os.getcwd() + "\\files"
files_to_copy=os.listdir(source_path)



for f in files_to_copy:
    print(f)
    new_file=shutil.copy(source_path + "\\" + f,target_path)
    print(new_file)

from tkinter import Tk
from tkinter.filedialog import askdirectory

import win32com.client
import sqlite3
import html

import re
import fnmatch
import os
from datetime import datetime
import logging




def main():

    # Setup logger -- output to txt file and console
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG, 
                        handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()])
    
    # Connect to Outlook by MAPI
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    # Show dialog box and return folder path
    Tk().withdraw()
    folder_path = os.path.normpath(askdirectory(title='Select Folder'))

    # Init & populate list of emails
    email_list = [file for file in os.listdir(folder_path) if file.endswith(".msg")]

    # Get total emails by filtering for files in directory with the .msg extension
    email_total = len(fnmatch.filter(os.listdir(folder_path), '*.msg'))
    logging.info(f"Number of emails in directory = {email_total}")
    for i, _ in enumerate(email_list):

        logging.info(email_list[i])

        # Create variable storing info from current email being parsed
        msg = outlook.OpenSharedItem(os.path.join(folder_path, email_list[i]))
        
        # Search email HTML for body text
        
        body = msg.Body
        html_body=msg.HTMLBody
        msg.SaveAs (folder_path + "\\" + email_list[i].replace(".msg",".txt"), 0)
        
        print(body)
        print(str(i))
        print('/n')
main()
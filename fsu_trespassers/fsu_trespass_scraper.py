from bs4 import BeautifulSoup
from pandas.io import html
import requests
import pandas as pd
import os
import csv
from datetime import datetime
import shutil

def Scrape():
    target_path=r"C:\Users\mason\Mason Consulting\Mason Prepaid - Documents\tools\FSU Scraper"
    d=datetime.now()

    date_string=str(d.year) + "-" + str(d.month).zfill(2) + "-" + str(d.day).zfill(2)
    records=[]
    fn= target_path + "\\" + date_string + "_trespass_scrape.csv"

    headers=['name', 'picture','date_of_birth', 'date_issued','area','case_number','imagename']
    #csv_writer.writerow(headers)

    
  
    base_url='https://police.fsu.edu'
    sess=requests.Session()
    sess.headers['User-Agent']=''
    for pagenum in range(20):   # a total hack.  there are 12 pages and i didn't see them doubling the number
        #  this is just for me to get a quick list from the website and to make sure I am not on it
        #  Also, when I do stuff like this, i demonstrate that I'm not a tinfoil hat wearing nut-case to people
        #  that have listened to to my opponents.  this is all they have, so code demos counter that as to recordings
        #  of me thinking out loud
        try:
            url='https://police.fsu.edu/campus-trespass-warning?page=' + str(pagenum)

            source = sess.get(url)
            print("page " + str(pagenum))
            soup = BeautifulSoup(source.content)
            for rownum in range(10):
                print("  row " + str(rownum + 1))
                row=soup.find("div",class_="views-row clearfix row-" + str(rownum+1))
                for colnum in range(3):
                    
                    cell=row.find("div",class_="views-col col-" + str(colnum+1))
                    name=cell.find("div",class_="views-field views-field-nothing").text
                    picture=base_url + cell.find("div",class_="views-field views-field-field-picture").img["src"]
                    date_of_birth=cell.find("div",class_="views-field views-field-field-dob").time.text
                    date_issued=cell.find("div",class_="views-field views-field-field-date-issued").time.text
                    area=cell.find("div",class_="views-field views-field-field-trespass-tpw-vicinity").strong.text
                    case_number=cell.find("div",class_="views-field views-field-title").strong.text
                    r = requests.get(picture, stream=True) #Get request on full_url
                    if r.status_code == 200:  
                       imagename=name.replace(",","_").replace(" ","") + ".jpg" #200 status code = OK
                       with open(target_path + "\\images\\" + imagename, 'wb') as f: 
                          r.raw.decode_content = True
                          shutil.copyfileobj(r.raw, f)
                    current_row=[name, picture,date_of_birth, date_issued,area,case_number,target_path + "\\images\\" + imagename]
                    print(current_row)
                    records.append(current_row)
                   # df.append(current_row)
                    #csv_writer.writerow()

      
        except Exception as e:
            print(e)
            continue
    date_now=datetime.utcnow()
    df=pd.DataFrame(data=records,columns=headers)
    df.to_csv(fn)
    #csv_file.close()


def download():


    for x in range(0,12):
        print(x)
   
        fn="campus-trespass" + str(x) + ".html"
        url=str.format("https://police.fsu.edu/campus-trespass-warning?page={}",str(x))
        res=requests.get(url)
        if res.ok:
            soup=BeautifulSoup(res.content)
            with open(fn,"wb") as file:
                file.write(res.content)
    
                print(len(soup))

        else:
            print(str(x) +  " failed with " + str(res.status_code))
            break


# def GetIDs():
#     import matplotlib.pyplot as plt
#     import matplotlib.image as mpimg
#     from IPython.display import Image, HTML
#     df=pd.read_csv(r"C:\lm\mppcr\Mason Consulting\Mason Prepaid - Documents\tools\FSU Scraper\2022-03-16_trespass_scrape.csv")
#     df.to_html(escape=False)
#     img = mpimg.imread('Adams_Marcus.jpg')
#     imgplot = plt.imshow(img)
#     plt.show()




Scrape()
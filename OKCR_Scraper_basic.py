# %%
import pandas as pd
import os
import requests

# %%
companyname='TIMBERWOLF MINERALS LLC'

# %%


class HTML_Collector(object):
    """this will wrap a lot of the functionality of scraping the OKCountyRecords.com site
   The availability of the consideration paid is extremely useful, but not available on the
   API"""

    def __init__(self):
        self.session=requests.session()
       
        self.session.headers["User-Agent"]=""

    def SearchWebsite(self,company):

        
        dfs=[]
        i=1
        url="https://okcountyrecords.com/results/omni=" + str(company).replace(" ","+") + "/recorded_date=asc:site_id=asc:instrument_link=asc/page-" + str(i)
        res=self.session.get(url)

        dfList=pd.read_html(res.content)
        df=dfList[0]
        df["company"]=company
        df["source"]=url
        df["url"]= "https://okcountyrecords.com/detail/" + df["County"] + "/" + df["Instrument"]
       # df["InstrumentID"]=df["County"] + "-" + df["Instrument"]
        df.set_index("url",inplace=True)
        df.to_csv(company + str(i) + ".csv")
        dfs.append(df)
    
        while res.ok:
            try:
                i=i+1
                url="https://okcountyrecords.com/results/omni=" + str(company).replace(" ","+") + "/recorded_date=asc:site_id=asc:instrument_link=asc/page-" + str(i)
                res=self.session.get(url)
                dfList=pd.read_html(res.content)
                df=dfList[0]
                df["company"]=company
                df["source"]=url
                df["url"]= "https://okcountyrecords.com/detail/" + df["County"] + "/" + df["Instrument"]
            
                df.set_index("url",inplace=True)
               
                df.to_csv(company + str(i).zfill(3) + ".csv")
                dfs.append(df)
       
                print(url)
            except ValueError as e:
                print(e)
                print("combining ")
                dfAll=pd.concat(dfs,ignore_index=True)
                dfAll.drop_duplicates()
                print("saving ")
                
                dfAll.to_csv(company + "-ALL.csv")

                break
   
   


# %%




# %%
try:
    scraper=HTML_Collector()
    print("executing..")
    scraper.SearchWebsite(companyname)
    print("done")
except:
    print('err')

# %%
def Combine(file_list,company):
        dfs=[]

        #df2=pd.DataFrame()
    # df=pd.read_excel("Combined.xlsx")
        
        intRowsBefore=0
        #dfs.append(df)
        for fn in file_list:
        
            #print("reading " + fn)
            df=pd.read_csv(fn)

            columns_to_include=[col for col in df.columns][1:]
            df2=df[columns_to_include]
            df["url"]= "https://okcountyrecords.com/detail/" + df["County"] + "/" + df["Instrument"]       
                
            #df2.set_index("url",inplace=True)
            
            print("appending " + fn)
            dfs.append(df2)
            os.remove(fn)
            #dfs.append(pd.read_excel()
        print("concatenating " + str(len(dfs)) + " dataframes")
        dfAll=pd.concat(dfs,ignore_index=True)
        intRowsAfter=len(dfAll)
        intNewRows=intRowsAfter-intRowsBefore
        
        dfAll.to_excel(company + ".xlsx")
        print(str(intNewRows)+ " added for "+ company)

# %%
file_list=[x for x in os.listdir() if x.endswith('csv')]

# %%

Combine(file_list,companyname)

# %%




import pandas as pd
import numpy as np
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from requests import get

def my_scraper():
    link = input("What is the craigslist link you would like to scrape? ")
    city = input("What is the city? ")
    region = input("What is the region? ")
    income = input("What is the income amount? ")
    income_level = input("What is the income level? ")
    poverty_rate = input("What is the poverty rate? ")
    city_dataframe = input("What is the city dataframe name (city_dataframe)? ")





    #Convert Elements into String Function
    def element_converter(i):
        new_str = str(i)
        return new_str

    test = link
    #Pull listings from Craigslist
    my_craig = get(test)
    html_soup = BeautifulSoup(my_craig.text, 'html.parser')
    a = (my_craig)
    my_body = html_soup.body.prettify
    b = html_soup.find_all(class_="result-title hdrlnk")

    #Convert stringed list
    convert_list = []
    for i in b:
        new_var = str(i)
        convert_list.append(new_var)


    #Clean string list
    clean_list = []
    for i in convert_list:
        one_find = i.find(">")
        two_find = i.find("a>")
        new_var = i[one_find + 1:two_find - 2]
        clean_list.append(new_var)
   

    #Making the Dictionary
    craig_dict = {"Craigslist Post":[], "City":[], "Region":[], "Income":[], "Income Level":[], "Poverty Rate":[]

    }

    for i in clean_list:
        craig_dict["Craigslist Post"].append(i)
        craig_dict["City"].append(city)
        craig_dict["Region"].append(region)
        craig_dict["Income"].append(income)
        craig_dict["Income Level"].append(income_level)
        craig_dict["Poverty Rate"].append(poverty_rate)



    transfer_df = pd.DataFrame(craig_dict, columns = ["Craigslist Post", "City", "Region", "Income", "Income Level","Poverty Rate"])

    #Create a master df ***Do this one time
    

    return transfer_df

"""
#How to launch the script
test4 = (my_scraper())
frames.append(test4)
final_master_frame = pd.concat(frames)




    #Make CSV Backup
    #indianapolis1_df.to_csv(r'/Users/dewaynewhitfield/documents/coding/capstone/indianapolis1.csv')

    #Merge Dataframe


    #Concat
    #my_frames = [transfer_df,template_df]
    #master_df = pd.concat(my_frames)
    #template_dict.append(master_df)
    

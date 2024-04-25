#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 13:46:02 2021

@author: jeong-wonlyeol
"""



from selenium import webdriver
import time
import pandas as pd 

driver = webdriver.Chrome("/Users/jeong-wonlyeol/Desktop/chromedriver")
driver.get("https://apps.apple.com/kr/app/%EC%9C%8C%EB%9D%BC-%EC%98%A4%EB%94%94%EC%98%A4%EB%B6%81/id1250319483#see-all/reviews")
title_start = 0;
num = 111;
cnt = 0 ;

dic = {"score": [] , "content" : [] , 'date':[]}
data = pd.DataFrame(dic)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(1) 
time_sec = time.gmtime(time.time()).tm_sec

content_num  = 111
while True:
    
    try:
        time.sleep(0.2)
        cnt +=1
    
        if time_sec - time.gmtime(time.time()).tm_sec > 600:
            break;
            
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        
    
        dic = {}
        
        
        content_num  +=1
        
        score = driver.find_element_by_xpath('//*[@id="ember'+str(content_num)+'"]/div[2]/figure/span').get_attribute('class')     ##fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > div.ZfcPIb > div > div > main > div > div.W4P4ne > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > div > span.nt2C1d > div > div
                                                    ##fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > div.ZfcPIb > div > div > main > div > div.W4P4ne > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > div > span.nt2C1d > div > div
        
                                        #
        content = driver.find_element_by_xpath('//*[@id="ember'+str(content_num)+'"]/div[2]/blockquote[1]/div/p').text
                                                #//*[@id="ember113"]/div[2]/blockquote/div/p
                         
        date = driver.find_element_by_xpath('//*[@id="ember'+str(content_num)+'"]/div[2]/div/time').text
        
        
        dic['score'] = [score]
      
        dic['content'] = [content]
        dic['date'] = [date]
        data_for_concat = pd.DataFrame(dic)
            
        data = pd.concat([data,data_for_concat],ignore_index = True)
        
        
        print(data_for_concat)
        print("count : ",cnt )
        data.to_csv("../output/appstore.csv")
        
        
    except Exception as e:
        print(e)
        pass
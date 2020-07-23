# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:35:55 2020

@author: User
"""

import pandas as pd 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException, TimeoutException,StaleElementReferenceException
import urllib.request
import requests
from datetime import datetime 
import time as time
from selenium.common.exceptions import UnexpectedAlertPresentException

def croller():
    
    dic = {"title" : [] , "tag" : [] ,"time" : [] ,"keyword": [],"explain":[] ,"columns" : [],"number of columns" : [] }
    df1 = pd.DataFrame(dic)
    
    chrome_options = webdriver.ChromeOptions()
   # chrome_options.add_argument('--headless') # gui 없이 돌아갈 수 있게 도와줌 
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome('C:/Users/User/Desktop/chromedriver.exe', chrome_options = chrome_options)
#//*[@id="conditionBtn"]
    driver.get("https://www.data.go.kr/tcs/dss/selectDataSetList.do") 
    
    driver.find_element_by_xpath('//*[@id="dTypeFILE"]/a').click()
    
    
    driver.find_element_by_xpath('//*[@id="conditionBtn"]').click()
    
    
    
    driver.find_element_by_xpath('//*[@id="chk_brm_group_01_08"]').click()
    driver.find_element_by_xpath('//*[@id="chk_brm_group_01_09"]').click()
    driver.find_element_by_xpath('//*[@id="chk_brm_group_01_011"]').click()
    
    
    
    time.sleep(30)
            
    
    
    count = 1
    page = 2
    while True:
        
        try:
        # 게시판 !!!
            
            time.sleep(2)
            
            
            # 제목 , tag 뽑기 
            
            tag = driver.find_element_by_xpath('//*[@id="fileDataList"]/div[2]/ul/li['+str(count)+']/p/span[1]')
                
                
            
            
            
                    
                                                      
            tag_text = tag.text
           
                
            title = driver.find_element_by_xpath('//*[@id="fileDataList"]/div[2]/ul/li['+str(count)+']/dl/dt/a/span[2]')
            title_text = title.text 
            
            driver.find_element_by_xpath('//*[@id="fileDataList"]/div[2]/ul/li['+str(count)+']/dl/dt/a').send_keys(Keys.CONTROL +"\n")  
            
            
            
            T1 = driver.find_element_by_xpath('//*[@id="fileDataList"]/div[2]/ul/li['+str(count)+']/div[1]/p[1]/span[2]').text
            #                                   //*[@id="fileDataList"]/div[2]/ul/li[2]/div[1]/p[1]/span[2]
            '''새창 띄우기''' 
            
            
            
            #title.send_keys(Keys.CONTROL +"\n")  
            
            
            
            driver.switch_to.window(driver.window_handles[1])
            
            
            time.sleep(2)
           
            # column 뽑기
            lst = ""
            
            span_turn = 1
            number_col = 0 
            
            try:
                
                keyword = driver.find_element_by_xpath('//*[@id="fileDetailTableArea"]/tbody/tr[8]/td[2]/div/div/div[2]').text
                
                explain = driver.find_element_by_xpath('//*[@id="fileDetailTableArea"]/tbody/tr[11]/td/div/div/div[2]').text
                
            except : 
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                count = count+1
                continue
            while True:
                
                
                try:
                    
                    span = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td['+ str(span_turn) +']/span')
                    number_col = number_col+1
                    lst = lst+"  \ "+span.text
                    
                    span_turn = span_turn+1
                    
                    
                except NoSuchElementException:
                    break
             
            #데이터프레임에 넣어야 함
            print(lst)
            
            dic = {"title" : [title_text] , "tag" : [tag_text] ,"time" : [T1] ,"keyword": [keyword], "explain": [explain] ,  "columns" : [lst], "number of columns" : [number_col]}
            df = pd.DataFrame(dic)
            print(df)
            df1 = pd.concat([df1,df])
            
            df1.to_csv("C:/Users/User/Desktop/Summarize_Public_data_6.csv",encoding='utf-8-sig')
            
            #새창 닫기
            
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            
            
        #게시판 ---
        #목록 하나 내려가기
             
            count = count +1
            
        #다 뽑앗으면?
            if count > 10:
                
                
                try:
                    print("----------------")
                    time.sleep(1)
                    
                    
                    driver.find_element_by_xpath('//*[@id="fileDataList"]/nav/a['+str(page)+']').click()
                    
                    if page >= 11:
                        
                        
                        count = 1 
                        page = 2
                        
                        
                    else:
                        count = 1 
                        page = page +1      
                        print(page)
                        
                
                except NoSuchElementException:
                    

                    break    
                #여기서 보내기 
                
                
                
                
                
           
        except NoSuchElementException:
            print(df1)
            
            
            break
        
    return df1



if __name__ == "__main__":
    a = croller()
    a.to_csv("C:/Users/User/Desktop/Summarize_Public_data_6.csv",encoding='utf-8-sig')
    

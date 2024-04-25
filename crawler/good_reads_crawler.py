#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 13:46:02 2021

@author: jeong-wonlyeol
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome("/Users/jeong-wonlyeol/Desktop/자료들/crawler_selenium/chromedriver2")



# driver.get(
#         "https://www.goodreads.com/book/show/70240470/reviews?reviewFilters={%22workId%22:%22kca://work/amzn1.gr.work.v3.FtAgcNwYGBeVoktw%22,%22after%22:%22MzQ3LDE3MDAzNDAzMTE4Mjk%22}")

driver.get('https://www.goodreads.com/book/show/42844155/reviews?reviewFilters={%22workId%22:%22kca://work/amzn1.gr.work.v1.TbpxJa2CwiSSz_9W2FruoA%22,%22after%22:%22NjAwMDEsMTM3NTQxODE5NjAwMA%22}')


time.sleep(15)
print('down')
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
cnt = 0
passed_cnt = 0 


total_df = pd.DataFrame()

cnt = 1
check = False


print('크롤링 시작합니다.')
while True:
    
    
    try:
        rating_1 = '//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[4]/div[4]/div/button'
        rating_2 = '//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[4]/div[4]/div/button'                                 
        rating_3 = '//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[4]/div[4]/div/button'
        normal = '//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[4]/div[5]/div/button'
        element = WebDriverWait(driver, 10).until(
                                                    
            EC.element_to_be_clickable((By.XPATH,rating_1 ))
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)

        time.sleep(3)

    except Exception as e:
        print(f"An error occurred: {e}")
        # Optional: break the loop if the element is not found or other errors occur
        break
    check = False
    
    
    while True:
        element_xpath = f'//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[4]/div[2]/div[{cnt}]'
        
        # element_xpath = f'//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[4]/div[3]/div[{cnt}]'
        
        
        rating_xpath = element_xpath+'/article/section/section[1]/div/span'
        
        contents_xpath = element_xpath + '/article/section/section[2]/section/div/div[1]/span'
        
        try:
            
            rating_element = driver.find_element(By.XPATH, rating_xpath)
            #print(rating_element.get_attribute('aria-label'))
            rating = rating_element.get_attribute('aria-label')
            # 만점 : 5 
            rating = rating.split(' ')[1] 
            
            content_element = driver.find_element(By.XPATH, contents_xpath)
            content = content_element.text
            tmp_df = pd.DataFrame({'rate':rating , 'text':content } ,index = [cnt-passed_cnt])
            total_df = pd.concat([total_df,tmp_df])
            print(tmp_df)
            check = False
        except:
            if check:
                break
            passed_cnt +=1
            print('해당 Element가 없습니다.')
            check = True
        cnt+=1
        
        
        total_df.to_csv('../output/Harry_Potter_5.csv')

    group_counts = total_df.groupby('rate').count()
    if (cnt-passed_cnt >= 1000):
        # If the condition is met for all groups, you can break the loop or alter your program flow
        print("All groups have counts >= 1000")
        # Break or alter flow as needed
        exit()
    print(group_counts)

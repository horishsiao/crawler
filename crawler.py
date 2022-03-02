from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
key_word = input("請輸入要查詢的關鍵字：")
url = "https://www.google.com.tw/maps/search/"+key_word+"/"

drivePath = "/Users/user/Desktop/1101 作業/企畫專題實務/爬蟲/chromedriver"

browser = webdriver.Chrome(executable_path = drivePath)
browser.get(url)
pane = browser.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]')
shop_name_list = []
star_num_list = []
adress_list = []
comment_num_list = []
tel_list = []
shop_url = []

#==============================================================
#控制選單下拉
for o in range(0,4):
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane) 
time.sleep(5)

#==============================================================
#找到標籤a下所有的店家資料
page1 = browser.page_source
Obj = BeautifulSoup(page1,'html.parser')

#==============================================================
#抓取店家基本資料:店鋪名稱、星級
shop_name = Obj.findAll("a",{'jstcache':'53',})
print('===店鋪名稱===')
for i in shop_name:
    print(i.get('aria-label'))
    shop_name_list.append(i.get('aria-label'))
    shop_url.append(i.get('href'))

browser.close()

#==============================================================
#開新網頁並且依序載入新的店家網頁
for k in shop_url:

    url = k
    drivePath = "/Users/user/Desktop/1101 作業/企畫專題實務/爬蟲/chromedriver"
    chrome = webdriver.Chrome(executable_path = drivePath)
    chrome.get(url)
    page1 = chrome.page_source
    Obj = BeautifulSoup(page1,'html.parser')
    time.sleep(3)

    #=========================================================

    adress = Obj.findAll('button',{'data-item-id':'address'})
    print('===地址===')
    for l in adress:
            print(l.get('aria-label'))
            adress_list.append(l.get('aria-label'))

    star_num = Obj.findAll('ol',{'class':'section-star-array'})
    for j in star_num:
        print(j.get('aria-label'))
        star_num_list.append(j.get('aria-label'))

    comment_num = Obj.findAll('button',{'class':'Yr7JMd-pane-hSRGPd'})
    for m in comment_num:
        print(m.get('aria-label'))
        comment_num_list.append(m.get('aria-label'))
        break

    tel = Obj.findAll('button',{'data-tooltip':'複製電話號碼'})
    for tels in tel:
        print(tels.get('aria-label'))
        tel_list.append(tels.get('aria-label'))
        break

    chrome.close()
print('============================')
for o in range(0,20):
    print(shop_name_list[o],adress_list[o],tel_list[o],star_num_list[o],comment_num_list[o])
    print('============================')











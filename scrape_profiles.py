from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import pandas 
import time
import csv
from selenium.webdriver.common.keys import Keys
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import sqlite3



def create_table():
    conn=sqlite3.connect("profiles.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profiles (name TEXT,email TEXT,link TEXT,status TEXT)")
    conn.commit()
    conn.close()


def insert(name,email,link,status):
    conn=sqlite3.connect("profiles.db")
    cur=conn.cursor()
    cur.execute("INSERT OR REPLACE INTO profiles VALUES(?,?,?,?)",(name,email,link,status))
    conn.commit()
    conn.close()
    
def check_if_exists(name):

    conn=sqlite3.connect("profiles.db")
    cur=conn.cursor()
    name_exists = cur.execute('SELECT 1 FROM profiles WHERE name="%s" LIMIT 1' % name)
    name_exists = cur.fetchone() is not None
    return (name_exists)

def update(scaned,link):
    conn=sqlite3.connect("profiles.db")
    cur=conn.cursor()
    cur.execute("UPDATE sources SET scaned=? WHERE link=?",(scaned,link))
    conn.commit()
    conn.close()

def select_all_sources():
    conn=sqlite3.connect("profiles.db")
    cur = conn.cursor()
    cur.execute("SELECT link FROM sources WHERE scaned=0")
    rows = cur.fetchall()
    conn.close()
    return (rows)

url="https://www.instagram.com/accounts/login/"

create_table()
webdriver="chromedriver.exe"
driver=Chrome(webdriver)

driver.get(url)
time.sleep(5)


username="****"#input("Enter you username : ")
password="****"#input("Enter your password : ")

user=driver.find_elements_by_css_selector('form input')[0]
passer=driver.find_elements_by_css_selector("form input")[1]
user.send_keys(username)
time.sleep(3)
passer.send_keys(password)
time.sleep(2)
passer.send_keys(Keys.ENTER)
time.sleep(5)



profiles = select_all_sources()
profiles = [item for (item,) in profiles]
for profile in profiles:
    follower_scraper=input("are you ready? : ")
    driver.get(profile)
    time.sleep(5)
    que="n"
    que=input("Click on the profiles followers and scroll to load as many followers names as you want. When you are ready Press y    (y,n): ")
    if que=="y":
        content=driver.page_source
        soup=BeautifulSoup(content,"html.parser")
        all=soup.find_all("a",{"class":"FPmhX notranslate _0imsa"})
        followers=[]
        i = 0 
        j = 0
        for item in all:
            followers.append(item.text)
            checker = check_if_exists(item.text)
            if checker == False:
                insert(item.text,"--","https://www.instagram.com/"+item.text,"not scraped for emails")
                i = i + 1
            else:
                j = j + 1
        update(i+j,profile)
        print(i," new entries",j," already existed")
    else:
        print("waiting")

print("program closed")




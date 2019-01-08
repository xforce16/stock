import json
import random
import re
import pymongo
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.by import By
from urllib import parse
from lxml import etree
from bs4 import BeautifulSoup
from pymongo import MongoClient
from openpyxl import load_workbook


class IrmCrawler():
    def __init__(self):
        self.login_url='http://irm.cninfo.com.cn/ircs/interaction/lastRepliesForSzse.do'
        self.MONGO_URI = 'localhost'
        self.client = MongoClient(host='localhost', port=27017)
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(15)
        self.wait = WebDriverWait(self.browser, 5)
        self.database =self.client["TpInvestment201812"]


    def start_request(self):

        self.browser.get(url=self.login_url)
        content = self.browser.page_source
        soup1 = BeautifulSoup(content, "html.parser")
        soup2 = soup1.find("div", {"class": "Tl talkList2"})
        content1 = soup2.find_all("a",{"class":"cntcolor"})


        for i in range(10):
            a = content1[i].text
            print(a.strip())





irm = IrmCrawler()


irm.start_request()
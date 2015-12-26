import scrapy
from selenium import webdriver
import time
import os.path
from search_test.items import IEEEItem
from scrapy.exceptions import CloseSpider
import sys

class IEEESpider(scrapy.Spider):
    name = "IEEE"
    allowed_domains = ["ieeexplore.ieee.org"]
    start_urls = ["http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=7128761"]#,
    #"http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=7347169"]

    def __init__(self):
        path_to_chromedriver = '/Users/xiaoli/Desktop/search/scrape/selenium_test/chromedriver'
        self.browser = webdriver.Chrome(executable_path = path_to_chromedriver)
        self.browser.get(IEEESpider.start_urls[0])

        self.filename = "titles.txt"
        self.title_count = 1

        if os.path.isfile(self.filename):
            os.remove(self.filename)

        self.browser.find_element_by_xpath('//*[@id="rows-per-page"]/option[contains(text(),"100")]').click()
        self.items = []
        
            
    def parse(self, response):

        if self.title_count == 1:
            self.parse_dir_contents(response)
            
        while True:
            try:
                next = self.browser.find_element_by_xpath('//*[@id="results-blk"]/div[2]/div/a[7]')
                next.click()
                time.sleep(5)
                yield scrapy.Request( self.browser.current_url, callback=self.parse_dir_contents)
            except:
                break          

    def parse_dir_contents(self, response):

        titles = response.xpath('//h3/a/span/text()').extract() 
       
        # -- write to item object ---
        
        for title in titles:
           item = IEEEItem()
           item['title'] = str(self.title_count) + ". " + title
           self.title_count += 1
           self.items.append(item)

        if len(self.items) > 200:
            with open(self.filename,'wb') as f:
                for item_temp in self.items:
                    #f.write(str(self.title_count) + '. ')
                    f.write(str(item_temp) + '\n')
                    f.write("\n")

           
               
                    
                    
                    
                    
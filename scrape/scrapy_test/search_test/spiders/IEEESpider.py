import scrapy
from selenium import webdriver
import time
import os.path
from search_test.items import MyItem
from scrapy.exceptions import CloseSpider
import sys
from pattern.web import URL


class IEEESpider(scrapy.Spider):
    name = "IEEE"
    allowed_domains = ["ieeexplore.ieee.org"]
    start_urls = ["http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=7128761"]

    def __init__(self):
        path_to_chromedriver = '/Users/xiaoli/Desktop/search/scrape/selenium_test/chromedriver'
        
        
        self.browser = webdriver.Chrome(executable_path = path_to_chromedriver)

      
        self.browser.get(IEEESpider.start_urls[0])
        self.browser.find_element_by_xpath('//*[@id="rows-per-page"]/option[contains(text(),"100")]').click()

        self.title_count = 1
            
    def parse(self, response):

        yield scrapy.Request( self.browser.current_url, callback=self.parse_dir_contents)
            

            
    def parse_dir_contents(self, response):

        titles = response.xpath('//h3/a/span/text()').extract() 
       
        # -- write to item object ---
        
        for title in titles:
           item = MyItem()
           item['title'] = str(self.title_count) + ". " + title
           item['file_urls'] = ["https://lagunita.stanford.edu/c4x/HumanitiesScience/StatLearning/asset/linear_regression.pdf"]
           self.title_count += 1
           yield item
           
        # recursively go to next page

        next = self.browser.find_element_by_xpath("//a[@aria-label='Pagination Next Page']")
        next.click()
        time.sleep(5)
        yield scrapy.Request( self.browser.current_url, callback=self.parse_dir_contents)
   
           
               
                    
                    
                    
                    
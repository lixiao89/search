import scrapy
from search_test.items import MyItem

class RSSSpider(scrapy.Spider):
    name = "RSS"
    allowed_domains = ["http://www.roboticsproceedings.org/"]
    start_urls = ["http://www.roboticsproceedings.org/rss11/index.html"]

    def __init__(self):
        self.title_count = 1
        
        
    def parse(self, response):

        for sel in response.xpath('//td[@width or @valign]'):
            item = MyItem()
            title = str(sel.xpath('a[not(@onclick)]/text()').extract())
            
            if title:
                item['title'] = str(self.title_count) + ". " + title[3:-2]
                self.title_count += 1
                yield item
                
            pdf_url =  RSSSpider.start_urls[0][:-10] + str(sel.xpath('a[@onclick]/@href').extract())[3:-2]

            # uncomment this if want to download pdfs !!
            # if pdf_url[-4:] == ".pdf":
            #     item['file_urls'] = [pdf_url]
            #     yield item

            
           
            
       
     
       
           
               
                    
                    
                    
                    
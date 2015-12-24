import scrapy

class IEEESpider(scrapy.Spider):
    name = "IEEE"
    allowed_domains = ["ieeexplore.ieee.org"]
    start_urls = ["http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=7128761"]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body) 

        filename = "titles.txt"
        with open(filename, 'wb') as f:
                f.write(response.xpath('//h3/a/span/@id/text()').extract()) 
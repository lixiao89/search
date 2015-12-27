# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class SearchTestPipeline(object):

    def __init__(self):
        self.file = open('pipline_out.json', 'wb')

    def process_item(self, item, spider):

        line = json.dumps(dict(item)['title']) + "\n"
        self.file.write(line)
        return item

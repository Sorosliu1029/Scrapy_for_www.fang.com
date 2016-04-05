# -*- coding: utf-8 -*-
from settings import FIELD_LIST
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FangPipeline(object):
    def __init__(self):
        self.file = open('fang.csv', 'w+')
        self.count = 0
        self.file.write('-1,' + ','.join(FIELD_LIST) + '\n')

    def process_item(self, item, spider):
        field_values = [item.get(field, ' ') for field in FIELD_LIST]
        self.file.write(str(self.count) + ',' + ','.join(field_values) + '\n')
        self.count += 1
        return item

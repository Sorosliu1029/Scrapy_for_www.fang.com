# -*- coding: utf-8 -*-
from settings import FIELD_LIST
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FangPipeline(object):
    def __init__(self):
        self.city_files = {}

    def process_item(self, item, spider):
        city_name = item['city_name']
        field_values = [item.get(field, ' ') for field in FIELD_LIST]
        if city_name not in self.city_files:
            self.city_files[city_name] = City(city_name)
            self.city_files[city_name].file = open(city_name + '.csv', 'w+')
            self.city_files[city_name].file.write('-1,' + ','.join(FIELD_LIST) + '\n')

        city = self.city_files[city_name]
        city.file.write(str(city.count) + ',' + ','.join(field_values) + '\n')
        city.count += 1

        return item


class City:
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.file = None

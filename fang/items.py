# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city_name = scrapy.Field()

    community_name = scrapy.Field()

    this_month_average = scrapy.Field()
    link_relative_last_month = scrapy.Field()
    year_on_year = scrapy.Field()

    community_address = scrapy.Field()
    program_characteristic = scrapy.Field()

    belonging_area = scrapy.Field()
    zipcode = scrapy.Field()

    circle_line_position = scrapy.Field()
    property_description = scrapy.Field()

    property_class = scrapy.Field()
    finished_time = scrapy.Field()

    developer = scrapy.Field()
    building_structure = scrapy.Field()

    building_class = scrapy.Field()
    building_area = scrapy.Field()

    floor_area = scrapy.Field()
    current_residence = scrapy.Field()

    total_residence = scrapy.Field()
    green_rate = scrapy.Field()

    plot_ratio = scrapy.Field()
    property_expense = scrapy.Field()

    additional_info = scrapy.Field()

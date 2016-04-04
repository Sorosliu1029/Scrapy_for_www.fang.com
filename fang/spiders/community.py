# -*- coding: utf-8 -*-
import scrapy
from fang.items import FangItem

class CommunitySpider(scrapy.Spider):
    name = 'Community'
    allowed_domains = ['fang.com']
    start_urls = ['http://esf.sh.fang.com/housing/']
    ch_en_pair = {
        '小区地址：': 'community_address',
        '项目特色：': 'program_characteristic',
        '所属区域：': 'belonging_area',
        '邮    编：': 'zipcode',
        '环线位置：': 'circle_line_position',
        '产权描述：': 'property_description',
        '物业类别：': 'property_class',
        '竣工时间：': 'finished_time',
        '开 发 商：': 'developer',
        '建筑结构：': 'building_structure',
        '建筑类别：': 'building_class',
        '建筑面积：': 'building_area',
        '占地面积：': 'floor_area',
        '当期户数：': 'current_residence',
        '总 户 数：': 'total_residence',
        '绿 化 率：': 'green_rate',
        '容 积 率：': 'plot_ratio',
        '物 业 费：': 'property_expense',
        '附加信息：': 'additional_info'
    }

    def parse(self, response):
        house_list = response.xpath('//div[@class="info rel floatl ml15"]/dl/dt/a')
        community_urls = map(lambda house: house.css('a::attr(href)').extract()[0].encode('utf-8'), house_list)
        community_urls = filter(lambda url: url[-4:] == 'com/', community_urls)
        community_urls = map(lambda url: url+'xiangqing/', community_urls)

        for url in community_urls[:2]:
            yield scrapy.Request(url, callback=self.parse_community_detail)

        next_page = response.xpath('//a[@id="PageControl1_hlk_next"]')
        if next_page and 0:
            next_page = next_page[0].css('a::attr(href)').extract()[0].encode('utf-8')
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
        else:
            return

    def parse_community_detail(self, response):
        item = FangItem()
        info = response.xpath('//div[@class="leftinfo"]')[0]
        community_name = info.xpath('//div[@class="ewmBoxTitle"]/span/text()').extract()[0]
        item['community_name'] = community_name.encode('utf-8')

        priceinfo= response.xpath('//span[@class="pred pirceinfo"]/text()')
        item['this_month_average'] = priceinfo[0].extract().encode('utf-8')
        item['link_relative_last_month'] = priceinfo[1].extract().encode('utf-8')
        item['year_on_year'] = priceinfo[2].extract().encode('utf-8')

        blocks = response.xpath('//dl[@class="lbox"]')
        for i, block in enumerate(blocks):
            if i == 0:
                dd_details = block.xpath('dd')
                for dd_detail in dd_details:
                    k = dd_detail.xpath('strong/text()').extract()[0].encode('utf-8')
                    try:
                        v = dd_detail.xpath('text()').extract()[0].encode('utf-8')
                    except IndexError:
                        v = dd_detail.xpath('span/text()').extract()[0].encode('utf-8')
                    if k == '环线位置':
                        k += '：'
                        v = v[3:]
                    if k in self.ch_en_pair:
                        item[self.ch_en_pair[k]] = v
        return item

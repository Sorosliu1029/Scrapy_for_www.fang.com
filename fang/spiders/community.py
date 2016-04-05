# -*- coding: utf-8 -*-
import scrapy
from fang.items import FangItem
from fang.settings import CH_EN_PAIR
CITY = 'sh'
START_URL = 'http://esf.%s.fang.com/housing/' % CITY

class CommunitySpider(scrapy.Spider):
    name = 'Community'
    allowed_domains = ['fang.com']
    start_urls = [START_URL]

    def parse(self, response):
        house_list = response.xpath('//div[@class="info rel floatl ml15"]/dl/dt/a')
        community_urls = map(lambda house: house.css('a::attr(href)').extract()[0].encode('utf-8'), house_list)
        community_urls = filter(lambda url: url[-4:] == 'com/', community_urls)
        community_urls = map(lambda url: url+'xiangqing/', community_urls)

        for url in community_urls:
            yield scrapy.Request(url, callback=self.parse_community_detail)

        next_page = response.xpath('//a[@id="PageControl1_hlk_next"]')
        if next_page:
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
        try:
            item['this_month_average'] = priceinfo[0].extract().encode('utf-8')
        except IndexError:
            item['this_month_average'] = ' '

        try:
            item['link_relative_last_month'] = priceinfo[1].extract().encode('utf-8')
        except IndexError:
            item['link_relative_last_month'] = ' '

        try:
            item['year_on_year'] = priceinfo[2].extract().encode('utf-8')
        except IndexError:
            item['year_on_year'] = ' '

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
                    v = v.replace(',', '、')
                    if k in CH_EN_PAIR:
                        item[CH_EN_PAIR[k]] = v
        return item

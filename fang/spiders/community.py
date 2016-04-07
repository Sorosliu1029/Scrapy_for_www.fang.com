# -*- coding: utf-8 -*-
import scrapy
from fang.items import FangItem
from fang.settings import CH_EN_PAIR, SPEC_CITIES


class CommunitySpider(scrapy.Spider):
    name = 'Community'
    allowed_domains = ['fang.com']
    start_urls = ['http://fang.com/SoufunFamily.html']
    requests = []
    city_index = 0

    def parse(self, response):
        if not SPEC_CITIES:
            main_body = response.xpath('//div[@id="c02"]')[0]
            all_city = main_body.xpath('.//a[contains(@href, ".fang.com/")]')
            for city in all_city:
                url = city.css('a::attr(href)').extract()[0].encode('utf-8')
                city_name = city.xpath('./text()').extract()[0].encode('utf-8')
                if url[7:9] == 'bj':
                    continue
                    # url for Beijing is broken, even with browser... :(
                    url = 'http://esf.fang.com/housing/'
                else:
                    url = 'http://esf.' + url[7:] + 'housing/'
                request = scrapy.Request(url, callback=self.parse_city)
                request.meta['city_name'] = city_name
                self.requests.append(request)

        else:
            with open('fang/city_list.txt') as file:
                cities = file.readlines()
            cities = map(lambda string: string.strip().split('-'), cities)
            for city in cities:
                request = scrapy.Request(city[1]+'housing', callback=self.parse_city)
                request.meta['city_name'] = city[0].decode('utf-8')
                self.requests.append(request)

        return self.get_city_request()


    def get_city_request(self):
        return self.requests[self.city_index]


    def parse_city(self, response):
        city_name = response.meta['city_name']
        house_list = response.xpath('//div[@class="info rel floatl ml15"]/dl/dt/a')
        community_urls = map(lambda house: house.css('a::attr(href)').extract()[0].encode('utf-8'), house_list)
        community_urls = filter(lambda url: url[-4:] == 'com/', community_urls)
        community_urls = map(lambda url: url+'xiangqing/', community_urls)

        next_page = response.xpath('//a[@id="PageControl1_hlk_next"]')
        if next_page:
            next_page = next_page[0].css('a::attr(href)').extract()[0].encode('utf-8')
            next_page_url = response.urljoin(next_page)
            request = scrapy.Request(next_page_url, callback=self.parse_city)
            request.meta['city_name'] = city_name
            yield request
        else:
            self.city_index += 1

        for url in community_urls:
            request = scrapy.Request(url, callback=self.parse_community_detail)
            request.meta['city_name'] = city_name
            if url == community_urls[-1] and not next_page:
                request.meta['city_done'] = True
            else:
                request.meta['city_done'] = False
            yield request


    def parse_community_detail(self, response):
        item = FangItem()

        is_city_done = response.meta['city_done']
        if is_city_done:
            yield self.get_city_request()

        item['city_name'] = response.meta['city_name']
        try:
            info = response.xpath('//div[@class="leftinfo"]')[0]
            community_name = info.xpath('//div[@class="ewmBoxTitle"]/span/text()').extract()[0]
            item['community_name'] = community_name.encode('utf-8')
        except IndexError:
            item['community_name'] = 'UNNAMED'

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
        yield item

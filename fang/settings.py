# -*- coding: utf-8 -*-

# Scrapy settings for fang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Googlebot'

SPIDER_MODULES = ['fang.spiders']
NEWSPIDER_MODULE = 'fang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fang (+http://www.yourdomain.com)'
USER_AGENT = 'MOZilla/5.0(x11; Linux x86_64; rv:7.0.1)Gecko/20100101 Firefox/7.7'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'fang.middlewares.MyCustomSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'fang.middlewares.MyCustomDownloaderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'fang.spiders.random_useragent.RandomUserAgentMiddleware': 400
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'fang.pipelines.FangPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

# setting according to scrapy_proxies module
# Retry many times since proxies often fail
# RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
# RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
#
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
#     # Fix path to this module
#     'fang.proxy.randomproxy.RandomProxy': 100,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
# }

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
# PROXY_LIST = '../http_proxy_list.txt'

COOKIES_ENABLED = False
################################################################

CH_EN_PAIR = {
    '小区地址：': 'community_address',
    '项目特色：': 'program_characteristic',
    '所属区域：': 'belonging_area',
    '邮    编：': 'zipcode',
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

FIELD_LIST = [
    'community_name',
    'this_month_average',
    'link_relative_last_month',
    'year_on_year',
    'community_address',
    'program_characteristic',
    'belonging_area',
    'zipcode',
    'circle_line_position',
    'property_description',
    'property_class',
    'finished_time',
    'developer',
    'building_structure',
    'building_class',
    'building_area',
    'floor_area',
    'current_residence',
    'total_residence',
    'green_rate',
    'plot_ratio',
    'property_expense',
    'additional_info'
]
from spiders.base_spider import BaseSpider

class CartoonSpider(BaseSpider):
    type = 1
    start_urls = [
        'https://api.bilibili.com/x/web-interface/dynamic/region?ps=10&rid=1'
    #     https://api.bilibili.com/x/web-interface/dynamic/region?ps=10&rid=36
    ]
    name = str(type)
    # name = 'cartoon_spider'
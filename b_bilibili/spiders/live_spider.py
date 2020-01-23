from spiders.base_spider import BaseSpider
class LiveSpider(BaseSpider):
    type = 160
    classify_id = 'bili_report_music'
    # name = 'live_spider'
    name = str(type)
    start_urls = [
        "https://api.bilibili.com/x/web-interface/dynamic/region?ps=10&rid=160"
    ]

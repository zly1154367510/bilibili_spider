from spiders.base_spider import BaseSpider
class MusicSpider(BaseSpider):
    type = 3
    classify_id = 'bili_report_music'
    # name = 'music_spider'
    name = str(type)
    start_urls = [
        'https://api.bilibili.com/x/web-interface/dynamic/region?ps=10&rid=3'
    #     "https://api.bilibili.com/x/web-interface/dynamic/region?ps=10&rid=160"
    ]

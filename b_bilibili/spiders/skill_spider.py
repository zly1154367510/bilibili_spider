from spiders.base_spider import BaseSpider

class SkillSpider(BaseSpider):
    type = 36
    start_urls = [
        "https://api.bilibili.com/x/web-interface/dynamic/region?ps=10&rid=36"
    ]
    # name = 'skill_spider'
    name = str(type)

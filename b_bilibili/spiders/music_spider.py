from spiders.base_spider import BaseSpider
from db_object import Video
class MusicSpider(BaseSpider):
    type = 1
    classify_id = 'bili_report_music'
    name = 'music_spider'
    start_urls = [
        'https://api.bilibili.com/x/web-interface/dynamic/region?ps=10&rid=3'
    ]
    def parse_data_insert_db(self,data):
        for i in data:
            # 去重下载过的视频不再下载
            org_video = self.session.query(Video).filter(Video.id == i['aid']).first()
            if org_video != None:
                continue
            bb = Video(
                id = i['aid'],
                title = i['title'],
                type = self.type,
                av_number = 'av%s'%(i['aid']),
                cover_loacl = i['pic'],
                video = '',
                video_download_url = 'https://www.bilibili.com/video/av%s' %(i['aid'])
            )
            self.session.add(bb)
            self.session.commit()

            if self.base_config['is_download_video']:
                self.download_video('https://www.bilibili.com/video/av%s' % (i['aid']))
            if self.base_config['is_download_cover']:
                self.download_cover('https://www.bilibili.com/video/av%s' % (i['aid']))
        pass
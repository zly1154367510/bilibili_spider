import scrapy
from config import Mysql,BaseConfig
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import you_get
import sys
import json
from db_object import Video
class BaseSpider(scrapy.Spider):
    engine = None
    session = None
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
    }
    mysql_config = Mysql.mysql_config
    base_config = BaseConfig.base_config
    sleepTime = 5

    start_urls = [
        'https://www.bilibili.com/'
    ]
    classify_id = ''

    def __init__(self):
        mysql_config = self.mysql_config
        if self.engine == None:
            self.engine = create_engine(
                "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4" % (mysql_config['username'], mysql_config['password'], mysql_config['hostname'], mysql_config['hostport'],mysql_config['database']),
                max_overflow=5, echo=True)
        if self.session == None:
            Session = sessionmaker(bind=self.engine)
            self.session = Session()

    def parse(self, response):
        body = json.loads(response.text)
        data = body['data']['archives']
        self.parse_data_insert_db(data)
        pass

    def parse_data_insert_db(self,data):
        pass


    def download_video(self,url):
        directory = self.base_config['video_local_dir']
        print(directory)
        sys.argv = ['you-get','--format=flv360','-o', directory, url,]
        # sys.argv = ['you-get', '-i', url]
        you_get.main()
        pass

    def download_cover(self,url):
        pass
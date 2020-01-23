import sys
import time
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import Mysql,BaseConfig
from db_object import Video
import os
mysql_config = Mysql.mysql_config
base_config = BaseConfig.base_config

mysql_config = mysql_config
engine = create_engine(
    "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4" % (
    mysql_config['username'], mysql_config['password'], mysql_config['hostname'], mysql_config['hostport'],
    mysql_config['database']),
    max_overflow=5, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

now_timestamp = int(time.time())
expiration_date = base_config['expiration_date']
org = now_timestamp - expiration_date
expire_video = session.query(Video).filter(Video.creation_time < org).all()
video_list_path = base_config['video_local_dir']
for i in expire_video:
    if os.path.exists(video_list_path+"/"+str(i.id)+'.flv'):
        os.remove(video_list_path+"/"+str(i.id)+'.flv')
    if os.path.exists(video_list_path+"/"+str(i.id)+'_.flv'):
        os.remove(video_list_path+"/"+str(i.id)+'_.flv')
    if os.path.exists(video_list_path+"/"+str(i.id)+'.crm.xml'):
        os.remove(video_list_path+"/"+str(i.id)+'.crm.xml')
    session.delete(i)

session.commit()
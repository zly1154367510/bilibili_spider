class Mysql:
    mysql_config = {
        "hostname":'106.12.138.179',
        "database":"b_bilibili",
        "username": 'root',
        "hostport": '3306',
        "password": '!Nozly514',
        "use_unicode":True,
        "charset":"utf8"
    }

class Redis:
    redis = {
        "hostname":"106.12.138.179",
        "port":"6379",
        "db":1,
        "password":"!redis514"
    }

class Mail:
    report_mail = {
        'email_address':"zhangliyuan@hongjianguo.com",
        'password':"Zly1154367510",
        'smtp_host':"smtp.exmail.qq.com",
        'smtp_port':"465",
        'is_ssl':True,
        'send_email_address':'1154367510@qq.com'
    }

class BaseConfig:
    base_config = {
        'is_download_video':True,
        'is_download_cover':True,
        'is_thread_download':False,
        'video_local_dir':'./video',
        'cover_local_dir':'./cover',
    }


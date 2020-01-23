from scrapy.cmdline import execute
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute('scrapy crawl reply -a tId=21160'.split())
# execute('scrapy crawl reply'.split())
# execute(['scrapy', 'crawl', 'hupu'])
# execute(['scrapy', 'crawl', 'weibo_top_search'])
# execute(['scrapy', 'crawl', 'jd_seckill_spider'])
# execute(['scrapy', 'crawl', 'music_spider'])

if len(sys.argv) == 1:
    execute(['scrapy', 'crawl', '1'])
else:
    cli_arg = sys.argv[1]
    execute(['scrapy', 'crawl', cli_arg])

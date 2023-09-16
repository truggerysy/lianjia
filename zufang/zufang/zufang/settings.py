# Scrapy settings for zufang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zufang'
LOG_LEVEL = 'ERROR'
SPIDER_MODULES = ['zufang.spiders']
NEWSPIDER_MODULE = 'zufang.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zufang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Host': 'hf.lianjia.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'Cookie': 'select_city=340100; lianjia_ssid=56194614-1ca3-4dfc-a22c-fa9c4b2cba5e; lianjia_uuid=7a25dd7f-dec4-42ad-816b-b0866719edff; login_ucid=2000000344968661; lianjia_token=2.0014e5e99379ef49aa0548c0a25742936a; lianjia_token_secure=2.0014e5e99379ef49aa0548c0a25742936a; security_ticket=tLm6uALOoZLqgVaahuVdd99yvb/FyPO5aOTH5g/gfjLazvvOhSABxhll/IZLMVjuSkqC2kIV38ot+1Wtr7Wpmvvy9rUpCkxDbZfK22WIqWtCiC6B+nqQ7HE5pLv0QZ9nrHCGvgPbXIfbZ8ZOls9BYSMnYVlQF7cKCz7T9sG5U6Q=; lfrc_=65aabb1d-7ab4-42ab-a22c-d6d7944efe44; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMDM5Yjk3NGNlMGM5Mjc1NGYwMmJiMzdjNWVlYTNkNGE0ODdlNzc0ZjYxMWM1ZTNlMGU1ZGE2ZGEzODE4NWE1ODJiMzJkZWZjMzIyYzUzOTFmMDE2ODYzMjVlM2Y2OGJiMjM2MTQyNzg3YTJlNzQ5ZjE1NDE3MTk4ZDBmMzM0YmVjMjcxNTMwODE0MGM2ZGU4OWNlZjc1M2RiZDY5ODI0OTVhOTM3ZDI0MDllMWI3ZjQ2NDBkZGNhZWExZTNkMTQxZTUzM2VlZDMxYzNlOTgzYWYzYjI2YzNjNGM1MWUzODVjOGU3NzU1NTc5NDM2MGFlYzJjZjY1MzM1MWQ0ZDA1MlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI4MDBiZjI1MFwifSIsInIiOiJodHRwczovL2hmLmxpYW5qaWEuY29tL3p1ZmFuZy9wZzEvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='
}

# DOWNLOADER_MIDDLEWARES = {
#     'zufang.middlewares.MyUserAgentMiddleware': 300
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zufang.middlewares.ZufangSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zufang.middlewares.ZufangDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zufang.pipelines.ZufangPipeline': 304,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

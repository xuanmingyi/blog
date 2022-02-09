AUTHOR = 'sin'
SITENAME = 'blog.lithum.tech'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('home', '/'),
         ('archive', '/archives.html'),
         ('tags', '/tags.html'),
         ('about this blog', '/about-this-blog.html'),
         ('wechat', '/wechat.html'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 15

THEME = "pelican-theme-jesuislibre"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra/favicon.ico', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/favicon.ico': {'path': 'favicon.ico'}, }

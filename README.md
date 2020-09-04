# tiantian
技术要求
python+mysql+redis+celery+fastDFS+nginx+uwsgi

实现功能

用户模块
    注册
    登录
    激活(celery)
    退出
    地址管理
    个人信息
    全部订单
商品模块
    商品详情
    商品列表
    搜索功能(haystack+whoose)
购物车模块(redis)
    增加
    删除
    修改
    查询
订单模块
    确认订单页面
    订单创建
    请求支付(支付宝)
    查询支付结果
评论

项目包介绍
ackage               Version
--------------------- ---------
amqp                  2.6.1
billiard              3.6.3.0
celery                4.4.7
certifi               2020.6.20
cffi                  1.14.2
chardet               3.0.4
cryptography          3.1
defusedxml            0.6.0
diff-match-patch      20200713
Django                2.2.15
django-formtools      2.2
django-haystack       2.8.1
django-import-export  2.3.0
django-redis          4.12.1
django-redis-sessions 0.5.6
django-tinymce        2.6.0
et-xmlfile            1.0.1
fdfs-client-py        1.2.6
future                0.18.2
httplib2              0.9.2
idna                  2.10
importlib-metadata    1.7.0
itsdangerous          1.1.0
jdcal                 1.4.1
jieba                 0.42.1
kombu                 4.6.11
MarkupPy              1.14
mutagen               1.45.1
odfpy                 1.4.1
openpyxl              2.6.4
Pillow                7.2.0
pip                   20.2.2
pkg-resources         0.0.0
py3Fdfs               2.2.0
pycparser             2.20
pycryptodomex         3.9.4
PyMySQL               0.10.0
pyOpenSSL             19.1.0
python-alipay-sdk     2.1.0
pytz                  2020.1
PyYAML                5.3.1
redis                 3.5.3
redis-py-cluster      1.3.5
requests              2.24.0
setuptools            49.2.1
six                   1.15.0
sqlparse              0.3.1
tablib                2.0.0
urllib3               1.25.10
uWSGI                 2.0.19.1
vine                  1.3.0
wheel                 0.34.2
Whoosh                2.7.4
xlrd                  1.2.0
xlwt                  1.3.0
zipp                  1.2.0

项目情况
.
├── apps
│   ├── cart
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       └── __init__.cpython-35.pyc
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   ├── admin.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── models.cpython-35.pyc
│   │   │   ├── urls.cpython-35.pyc
│   │   │   └── views.cpython-35.pyc
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── goods
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-35.pyc
│   │   │       └── __init__.cpython-35.pyc
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   ├── admin.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── models.cpython-35.pyc
│   │   │   ├── search_indexes.cpython-35.pyc
│   │   │   ├── urls.cpython-35.pyc
│   │   │   └── views.cpython-35.pyc
│   │   ├── search_indexes.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── __init__.py
│   ├── order
│   │   ├── admin.py
│   │   ├── alipay_public_key.pem
│   │   ├── app_private_key.pem
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_auto_20200827_1519.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-35.pyc
│   │   │       ├── 0002_auto_20200827_1519.cpython-35.pyc
│   │   │       └── __init__.cpython-35.pyc
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   ├── admin.cpython-35.pyc
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── models.cpython-35.pyc
│   │   │   ├── urls.cpython-35.pyc
│   │   │   └── views.cpython-35.pyc
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── __pycache__
│   │   └── __init__.cpython-35.pyc
│   └── user
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   ├── __init__.py
│       │   └── __pycache__
│       │       ├── 0001_initial.cpython-35.pyc
│       │       └── __init__.cpython-35.pyc
│       ├── models.py
│       ├── __pycache__
│       │   ├── admin.cpython-35.pyc
│       │   ├── __init__.cpython-35.pyc
│       │   ├── models.cpython-35.pyc
│       │   ├── urls.cpython-35.pyc
│       │   └── views.cpython-35.pyc
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── celery_tasks
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   └── tasks.cpython-35.pyc
│   └── tasks.py
├── db
│   ├── base_model.py
│   ├── __init__.py
│   └── __pycache__
│       ├── base_model.cpython-35.pyc
│       └── __init__.cpython-35.pyc
├── manage.py
├── static
│   ├── cart.html
│   ├── css
│   │   ├── main.css
│   │   └── reset.css
│   ├── detail.html
│   ├── images
│   │   ├── adv01.jpg
│   │   ├── adv02.jpg
│   │   ├── banner01.jpg
│   │   ├── banner02.jpg
│   │   ├── banner03.jpg
│   │   ├── banner04.jpg
│   │   ├── banner05.jpg
│   │   ├── banner06.jpg
│   │   ├── down.png
│   │   ├── fruit.jpg
│   │   ├── goods
│   │   │   ├── goods001.jpg
│   │   │   ├── goods002.jpg
│   │   │   ├── goods003.jpg
│   │   │   ├── goods004.jpg
│   │   │   ├── goods005.jpg
│   │   │   ├── goods006.jpg
│   │   │   ├── goods007.jpg
│   │   │   ├── goods008.jpg
│   │   │   ├── goods009.jpg
│   │   │   ├── goods010.jpg
│   │   │   ├── goods011.jpg
│   │   │   ├── goods012.jpg
│   │   │   ├── goods013.jpg
│   │   │   ├── goods014.jpg
│   │   │   ├── goods015.jpg
│   │   │   ├── goods016.jpg
│   │   │   ├── goods017.jpg
│   │   │   ├── goods018.jpg
│   │   │   ├── goods019.jpg
│   │   │   ├── goods020.jpg
│   │   │   ├── goods021.jpg
│   │   │   ├── sc01.jpg
│   │   │   ├── sc02.jpg
│   │   │   ├── sc03.jpg
│   │   │   ├── 鸡蛋.jpg
│   │   │   ├── 鸟蛋.jpg
│   │   │   ├── 咸鸭蛋.jpg
│   │   │   └── 鸭蛋.jpg
│   │   ├── goods02.jpg
│   │   ├── goods_detail.jpg
│   │   ├── goods.jpg
│   │   ├── icons02.png
│   │   ├── icons.png
│   │   ├── interval_line.png
│   │   ├── left_bg.jpg
│   │   ├── login_banner.png
│   │   ├── logo02.png
│   │   ├── logo.png
│   │   ├── pay_icons.png
│   │   ├── register_banner.png
│   │   ├── shop_cart.png
│   │   ├── slide02.jpg
│   │   ├── slide03.jpg
│   │   ├── slide04.jpg
│   │   ├── slide.jpg
│   │   └── 速冻与肉类
│   │       ├── 鸡腿.jpg
│   │       ├── 牛排.jpg
│   │       ├── 螃蟹肉.jpg
│   │       ├── 速冻水饺.jpg
│   │       ├── 虾丸.jpg
│   │       ├── 羊肉.jpg
│   │       ├── 鱼丸.jpg
│   │       └── 猪肉.jpg
│   ├── index.html
│   ├── js
│   │   ├── jquery-1.12.4.min.js
│   │   ├── jquery.cookie.js
│   │   ├── jquery-ui.min.js
│   │   ├── register.js
│   │   └── slide.js
│   ├── list.html
│   ├── login.html
│   ├── place_order.html
│   ├── register.html
│   ├── user_center_info.html
│   ├── user_center_order.html
│   └── user_center_site.html
├── templates
│   ├── base_detail_list.html
│   ├── base.html
│   ├── base_no_cart.html
│   ├── base_user_center.html
│   ├── cart.html
│   ├── detail.html
│   ├── index.html
│   ├── list.html
│   ├── login.html
│   ├── nginx版templates
│   │   ├── base_detail_list.html
│   │   ├── base.html
│   │   ├── base_no_cart.html
│   │   ├── base_user_center.html
│   │   ├── cart.html
│   │   ├── detail.html
│   │   ├── index.html
│   │   ├── list.html
│   │   ├── login.html
│   │   ├── order_comment.html
│   │   ├── place_order.html
│   │   ├── register.html
│   │   ├── static_base.html
│   │   ├── static_index.html
│   │   ├── user_center_info.html
│   │   ├── user_center_order.html
│   │   └── user_center_site.html
│   ├── order_comment.html
│   ├── place_order.html
│   ├── register.html
│   ├── search
│   │   ├── indexes
│   │   │   └── goods
│   │   │       └── goodssku_text.txt
│   │   ├── search1.html
│   │   └── search.html
│   ├── static_base.html
│   ├── static_index.html
│   ├── user_center_info.html
│   ├── user_center_order.html
│   └── user_center_site.html
├── tiantian
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   ├── settings.cpython-35.pyc
│   │   ├── urls.cpython-35.pyc
│   │   └── wsgi.cpython-35.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── utils
│   ├── fdfs
│   │   ├── client.conf
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   └── storage.cpython-35.pyc
│   │   └── storage.py
│   ├── __init__.py
│   ├── mixin.py
│   └── __pycache__
│       ├── __init__.cpython-35.pyc
│       └── mixin.cpython-35.pyc
├── uwsgi2.ini
├── uwsgi2.log
├── uwsgi2.pid
├── uwsgi.ini
├── uwsgi.log
├── uwsgi.pid
└── whoosh_index
    ├── MAIN_31ucmjcjxrddxiwz.seg
        ├── _MAIN_3.toc
            ├── MAIN_fvslspzaruljrrgd.seg
                ├── MAIN_vw3et6ccecqxx9jz.seg
                    └── MAIN_WRITELOCK




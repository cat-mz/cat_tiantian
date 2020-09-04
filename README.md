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

Package               Version
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

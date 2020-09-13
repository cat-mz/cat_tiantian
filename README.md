tiantian
===========================
**预览**：
!["预览"](C:\Users\cat\Desktop\01.png)

**环境依赖**
django + redis + mysql + fsatDFS + celery + nginx 

**部署步骤**

1. 启动redis
	- sudo redis-server /etc/redis/redis.conf 指定加载的配置文件(每个人安装地方不一样启动方式有差异)
2. 启动celery
	- celery -A celery_tasks.tasks worker -l info
3. 启动fastDFS
	- 正確启动方式：
		- sudo fdfs_trackerd /etc/fdfs/tracker.conf
		- sudo fdfs_storaged /etc/fdfs/storage.conf
	- 查看
		- ps -ef | grep fdfs
4. 启动uwsgi
	- 启动：uwsgi uwsgi.ini
	- 停止：uwsgi --stop uwsgi.pid
5. 启动nginx
	- sudo /usr/local/nginx/sbin/nginx

**目录结构描述**

```
.
├── apps
├── celery_tasks
├── db
├── manage.py
├── static
├── templates
├── tiantian
├── utils
├── uwsgi2.ini
├── uwsgi2.log
├── uwsgi2.pid
├── uwsgi.ini
├── uwsgi.log
├── uwsgi.pid
└── whoosh_index
```

**V1.0.0 版本内容更新**:

- [x] 生鲜类产品
	- [x] B2C
	- [x] PC电脑端网页
- [x] 功能模块：
 	- [x] 用户模块  
 	- [x] 商品模块（首页、 搜索、商品） 
 	- [x] 购物车模块  
 	- [x] 订单模块（下单、 支付）
- [x] 用户模块：
	- [x] 注册
	- [x] 登录
	- [x] 激活
	- [x] 退出
	- [x] 个人中心
	- [x] 地址
- [x] 商品模块：
	- [x] 首页
	- [x] 详情
	- [x] 列表
	- [x] 搜索（haystack+whoosh）
- [x] 购物车： 
	- [x] 增加
	- [x] 删除
	- [x] 修改
	- [x] 查询
- [x] 订单模块：
	- [x] 确认订单页面
	- [x] 提交订单（下单）
	- [x] 请求支付
	- [x] 查询支付结果
	- [x] 评论

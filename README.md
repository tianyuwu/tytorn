## Tytorn - A simple MVC framework based on tornado
一个基于tornado的简单MVC框架


### 框架特点
- 友好的中文注释
- 足够轻量，高度可定制
- 实现了子域名的配置
- 封装了日志记录，postgresql，session等web开发基本功能，让您更专注业务逻辑
- 集成了restful api 接口
- 实现了postgre sql的异步数据库操作
- 更多...

### 适用者
正在学习tornado，并尝试用tornado搭建项目的python开发者，虽然官方提供很多demo，但是那些demo都只是作为参考，不能应付实际开发需要。
本项目可以直接部署并作为开发的基本框架。

###快速上手

##### 1.安装tornado

[了解tornado](https://github.com/tornadoweb/tornado "了解tornado")

```shell
pip install tornado
```

##### 2.克隆本项目
如果你已经安装了git作为你的版本控制系统,可以执行下面的命令
```
git clone https://github.com/tornadoweb/tornado
```
如果没有安装git,可以下载本项目的压缩包

####  3.安装项目包依赖
```
pip install -r requirements.txt
```

####   4.配置数据库连接
修改config.py目录里的对应项
```
DB_HOST = '127.0.0.1'
DB_PORT = 5432
DB_DATABASE = 'your database'
DB_USER = 'tytorn'
DB_PASSWORD = '123456'
DB_ASYNC_MAXCONN = 33  # 最大异步连接数
DB_SYNC_MAXCONN = 10  # 最大同步连接数
```
#####  5.运行项目
在命令行下进入本项目，执行下面的命令
```
python server.py
```

It is ok, so easy!

###目录结构
```
├── README.md
├── requirements.txt   //包依赖
├── handlers           //处理网站请求的handler模块
│   ├── api              //rest api 模块
│   ├── main.py          //主域名下的handlers
│   ├── admin.py         //后台模块
│   ├── ...
├── models         // 模型
├── libs            //常用第三方库
├── static          //静态资源
├── utils           //项目底层库
│   ├── log.py           //日志操作类
│   ├── postgredb        //数据库操作类
│   ├── session.py       //session操作类
│   ├── tools.py         //工具库
│   ├── httpresponse.py  //rest api响应数据规范
├── server.py       //入口文件
├── urls.py         //路由配置文件
├── config.py         //项目配置文件
└── app.py          //application实例
```
###Credit
项目综合了guthub其他同仁的一些代码然后加以改进完成的，在此鸣谢
比如session模块是采用的[REDIS -TORNADO -SESSION](https://github.com/zs1621/tornado-redis-session)
restful方案是采用的[tornado-rest](https://github.com/rancavil/tornado-rest)
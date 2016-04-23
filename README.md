## Tytorn - A simple MVC framework based on tornado
一个基于tornado的简单MVC框架


### 框架特点
- 足够轻量，高度可定制，没有任何第三方包依赖，只要安装了tornado就能顺利运行
- 实现了子域名的配置
- 更多...

### 适用者
正在学习tornado，并尝试用tornado搭建项目的python开发者，虽然官方提供很多demo，但是那些demo都只是作为参考，不能应付实际开发需要。本项目可以直接部署并作为开发的基本框架。

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

##### 3.运行项目
在命令行下进入本项目，执行下面的命令
```
python server.py
```

It is ok, so easy!

###目录结构

├── README.md
├── handlers           //处理网站请求的handler模块
│   ├── main.py          //主域名下的handlers
│   ├── admin.py         //后台模块
│   ├── ...
├── models         // 模型
├── libs            //常用库
├── static          //静态资源
├── server.py       //入口文件
├── urls.py         //路由配置文件
└── application.py
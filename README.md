## 简介
本项目是 Hello Django 的配套编程项目，通过使用 Django 编写一个个人博客项目达到入门 Django 的目的。

## 项目环境依赖
1. Python 3.7.2
2. Django 2.2
3. SQlite 3.27.2
4. [pipenv](https://github.com/pypa/pipenv)

## 安装
1. 点击右上角的 Fork 按钮将项目 Fork 到自己的 GitHub
2. 将项目 Clone 到本地
3. 使用 pipenv 初始化环境 `cd djblog && pipenv install`
4. 进入 python 虚拟环境 `pipenv shell`
5. 执行数据库变更 `python manage.py migrate`
6. 运行项目 `python manage.py runserver`

打开浏览器访问 `http://127.0.0.1:8000` 出现下图则安装成功：
![Hello Django](http://cdn.defcoding.com/E4DB73AF-5F05-46EF-A9FE-67B8CC574F3B.png)

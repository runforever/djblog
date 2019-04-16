## 简介
本项目是 Hello Django 的配套编程项目，通过使用 Django 编写一个个人博客项目达到入门 Django 的目的。

## 项目环境依赖
1. Python 3.7.2
2. Django 2.2
3. SQlite 3.27.2

使用前请确定自己 Python 版本是否符合，建议使用 pyenv 来管理多个 Python 版本。

## 安装
1. 点击右上角的 Fork 按钮将项目 Fork 到自己的 GitHub
2. 将项目 Clone 到本地
3. 使用 virtualenv 初始化环境 `cd djblog && virtualenv .venv`
4. 安装依赖 `source .venv && pip install requirements.txt`
5. 运行项目 `python manage.py runserver`

打开浏览器访问 `http://127.0.0.1:8000` 出现下图则安装成功。

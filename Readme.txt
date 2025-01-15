基于多模态知识图谱的中医智能辅助诊疗平台
以“症状-证素-证-代表方-中药”为核心的多模态知识图谱，其中症状部分包括舌图

使用说明
环境准备：
操作系统：Windows 10 x64
运行环境，conda版本 python3.9
需要的python包：Flask Flask-SQLAlchemy Flask-Login Flask-WTF neo4j-driver(4.4.10) PyMySQL time json pandas py2neo

安装数据库（Neo4j Mysql）（将数据库备份导入数据库）
（1）安装Neo4j数据库，版本为 neo4j-community-4.4.12 
（2）安装Mysql数据库，版本为 5.7.24

运行步骤：
app.py为主文件，终端在其目录下输入flask run运行
浏览器输入 http://127.0.0.1:5000 即可打开网页

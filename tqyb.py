# -*- coding: UTF-8 -*-
# @Time :2021/2/8 9:41
# @Author :Liuzheng
# @Email :1540234613@qq.com

import pymysql
import requests
import json
import  datetime
from fake_useragent import UserAgent
requests.DEFAULT_RETRIES = 100#增加重试连接次数
s = requests.session()
s.keep_alive = False#关闭多余连接
requests.packages.urllib3.disable_warnings()
from lxml import etree
from sqlalchemy import create_engine
import pandas as pd


def get_data():
    # 访问详情界面
    # headers2 = {
    #     "Cookie": "JSESSIONID=13pdj2jnl5is0; JSESSIONID=4r2rv0b4ns8qj; com.topsec.sysTheme=default; com.topsec.sid=33fc1ead-68f1-11eb-8d23-890e153d9326/2887458053/525600/1644203073348/zhihui2020/0/1218972907; com.topsec.licence.report=true; com.topsec.tsm.userName=zhihui2020; com.topsec.tsm.operations=/portal/-/; com.topsec.tsm.adminRole=false; com.topsec.tsm.name=%25E6%2599%25BA%25E6%2585%25A7%25E5%259F%258E%25E5%25B8%2582; department=; com.topsec.portal.loginTime=1612667073396"
    # }
    session2 = requests.session()
    res2 = session2.get("https://tianqi.moji.com/", verify=False)
    # print(res2.text)
    html_xml = etree.HTML(res2.text)
    # print(html_xml)

    #获取天气信息
    tqzk=html_xml.xpath("//div[@class='forecast clearfix']/ul[@class='days clearfix'][1]/li[2]/text()")[1].strip()
    wd=html_xml.xpath("//div[@class='forecast clearfix']/ul[@class='days clearfix'][1]/li[3]/text()")[0].strip()
    f=html_xml.xpath("//div[@class='forecast clearfix']/ul[@class='days clearfix'][1]/li[4]/em/text()")[0].strip()
    j=html_xml.xpath("//div[@class='forecast clearfix']/ul[@class='days clearfix'][1]/li[4]/b/text()")[0].strip()
    # print(j)
    # 增加一列日期数据
    now = datetime.datetime.now()
    rq = now.strftime("%Y-%m-%d %H:%M:%S")
    # print(gjtj)

    conn = pymysql.connect('218.*。*。*', 'liuzheng', '***', '***', 3306)
    cur = conn.cursor()
    print('数据库连接成功!')

    sql = """insert into wq_tqyb(tqzk,wd,f,j,rq) values (%s,%s,%s,%s,%s) """
    cur.execute(sql, (tqzk,wd,f,j,rq))

    conn.commit()
    cur.close()


get_data()

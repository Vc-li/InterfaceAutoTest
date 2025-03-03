import logging

import allure
import pymysql
import requests

from config.config import *
from utils.analyse_case import analyse_case


@allure.step(" 发起http请求")
def send_http_request(case):
    request_data = analyse_case(case)
    res = requests.request(**request_data)
    logging.info(f"发起http请求 请求结果：{res.text}")
    return res


@allure.step(" 发起sql请求")
def send_sql_request(sql):
    connect = pymysql.Connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE, port=PORT, charset=CHARSET)
    cursor = connect.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    cursor.close()
    connect.close()
    logging.info(f"发起sql请求 sql语句：{sql} 结果：{row}")
    return row

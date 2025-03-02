import allure
import pymysql
import requests

from config.config import *
from utils.analyse_case import analyse_case


@allure.step(" 发起http请求")
def send_http_request(case):
    request_data = analyse_case(case)
    return requests.request(**request_data)


@allure.step(" 发起sql请求")
def send_sql_request(sql):
    connect = pymysql.Connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE, port=PORT, charset=CHARSET)
    cursor = connect.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    cursor.close()
    connect.close()
    return row

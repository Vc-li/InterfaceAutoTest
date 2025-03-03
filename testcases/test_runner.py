import pytest as pytest
from jinja2 import Template

from config.config import CASE_PATH
from utils.allure_init import allure_init
from utils.asserts import http_assert, json_assert
from utils.excel_utils import *
from utils.extractor import json_extractor
from utils.send_requests import send_http_request, send_sql_request


class TestRunner:
    case_data = analysis_casedata(CASE_PATH)
    all = {}  # 全局变量，存储提取器提取的数据

    @pytest.mark.parametrize("case", case_data)
    def test_case(self, case):
        all = self.all
        case = eval(Template(str(case)).render(all))  # 根据all内的值渲染case
        allure_init(case)  # 初始化allure

        res = send_http_request(case)  # 发起http请求

        # http 响应断言,
        http_assert(case, res)

        # sql响应断言
        json_assert(case)

        # Json 提取器 ，将提取到的值存入全局变量all
        json_extractor(case, res, all)

        # SQL 提取器 ，将提取到的值存入全局变量all


        # if case["files"]:
        #     for key, value in eval(case["files"]).items():

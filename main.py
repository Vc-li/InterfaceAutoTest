import os

import pytest

if __name__ == '__main__':
    pytest.main(["-vs", "./testcases/test_runner.py", "--alluredir=./report/json_report", "--clean-alluredir"])
    os.system("./allure-2.32.2/bin/allure generate ./report/json_report -o ./report/html_report --clean")

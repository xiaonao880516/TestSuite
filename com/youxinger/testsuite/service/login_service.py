import requests
from com.youxinger.testsuite.utils import constant
from com.youxinger.testsuite.utils import variables
import logging


# 前端登录
def foreground_login():
    if variables.foregroundTID == "":
        logging.info(u"前台登录")
        url = constant.DOMAIN + "/frontStage/login/login"
        data = {'username': constant.EMPLOYEE.get('employee_phone'), 'password': constant.EMPLOYEE.get('employee_password')}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        resp = requests.post(url, data, headers)
        tid = resp.headers.get('tid')
        variables.foregroundTID = tid
        json_data = resp.json()
        # # assert resp.status_code == 200, "返回200说明访问成功"
        if int(json_data['code']) != 200:
            raise Exception('前台登录失败')


# 后台登录
def background_login():
    if variables.backgroundTID == "":
        logging.info(u"后台登录")
        url = constant.DOMAIN + "/backStage/login/login"
        data = {'username': constant.BACKGROUND_USER.get('username'), 'password': constant.BACKGROUND_USER.get('password')}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        resp = requests.post(url, data, headers)
        variables.backgroundTID = resp.headers.get('tid')
        json_data = resp.json()
        if int(json_data['code']) != 200:
            raise Exception('后台登录失败')
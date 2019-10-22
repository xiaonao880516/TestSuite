import requests

from com.youxinger.testsuite.bean.area import AreaVerifyData
from com.youxinger.testsuite.bean.employee import EmployeeVerifyData
from com.youxinger.testsuite.bean.lc_global import LCGlobalVerifyData
from com.youxinger.testsuite.bean.platform import PlatVerifyData
from com.youxinger.testsuite.bean.store import StoreVerifyData
from com.youxinger.testsuite.utils import constant, variables, util
import logging


def get_update_global_data(verify_data: LCGlobalVerifyData):
    """
    获取总览数据
    :return:
    """
    logging.info(u"获取总览数据")
    if verify_data is None:
        verify_data = LCGlobalVerifyData()
    url = constant.DOMAIN + "/backStage/export/report/view-data"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.backgroundTID}
    params = {'start': variables.s_month_date_time, 'end': variables.s_month_date_time}
    resp = requests.get(url, params, headers=headers)
    try:
        json_data = resp.json()
        verify_data.i_lc_global_arrive_store_num = int(json_data['data']['arrive_store_num'])
        verify_data.f_lc_global_bhm_percent = util.percentage_2_float(json_data['data']['bhm_percent'])
        verify_data.i_lc_global_newvip_num = int(json_data['data']['newvip_num'])
        verify_data.f_lc_global_newvip_order_percent = util.percentage_2_float(json_data['data']['newvip_order_percent'])
        verify_data.i_lc_global_order_num = int(json_data['data']['order_num'])
        verify_data.i_lc_global_refund_num = int(json_data['data']['refund_num'])
        verify_data.f_lc_global_sale_num = float(json_data['data']['sale_num'])
        verify_data.f_lc_global_sale_percent = util.percentage_2_float(json_data['data']['sale_percent'])
        logging.debug('获取总览数据成功')
    except Exception as e:
        logging.error("获取总览数据错误, %s" % e)
    return verify_data


def get_update_area_data(area_id, verify_data: AreaVerifyData):
    """
    获取大区数据
    :return:
    """
    logging.info(u"获取大区数据")
    if verify_data is None:
        verify_data = AreaVerifyData()
    url = constant.DOMAIN + "/backStage/export/report/area-performance"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.backgroundTID}
    params = {'start': variables.s_month_date_time, 'end': variables.s_month_date_time, 'produce': ''}
    resp = requests.get(url, params, headers=headers)
    try:
        json_data = resp.json()
        area_array = json_data['data']
        for area in area_array:
            if area['area_id'] == area_id:
                verify_data.f_area_sales_amount = float(area['shiji'])
                break
        logging.debug('获取大区数据成功')
    except Exception as e:
        logging.error("获取大区数据错误, %s" % e)
    return verify_data


def get_update_store_data(store_id, verify_data: StoreVerifyData):
    """
    获取门店数据
    :return:
    """
    logging.info(u"获取门店数据")
    if verify_data is None:
        verify_data = StoreVerifyData()
    url = constant.DOMAIN + "/backStage/export/report/view-data"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.backgroundTID}
    params = {'start': variables.s_month_date_time, 'end': variables.s_month_date_time, 'store_id': store_id}
    resp = requests.get(url, params, headers=headers)
    try:
        json_data = resp.json()
        verify_data.i_store_arrive_store_num = int(json_data['data']['arrive_store_num'])
        verify_data.f_store_bhm_percent = util.percentage_2_float(json_data['data']['bhm_percent'])
        verify_data.i_store_newvip_num = int(json_data['data']['newvip_num'])
        verify_data.f_store_newvip_order_percent = util.percentage_2_float(json_data['data']['newvip_order_percent'])
        verify_data.i_store_order_num = int(json_data['data']['order_num'])
        verify_data.i_store_refund_num = int(json_data['data']['refund_num'])
        verify_data.f_store_sale_num = float(json_data['data']['sale_num'])
        verify_data.f_store_sale_percent = util.percentage_2_float(json_data['data']['sale_percent'])
        verify_data.f_store_plat_sale_num = float(json_data['data']['plat_sale_num'])
        verify_data.f_store_plat_sale_percent = util.percentage_2_float(json_data['data']['plat_sale_percent'])
        logging.debug('获取门店数据成功')
    except Exception as e:
        logging.error("获取门店数据错误, %s" % e)
    return verify_data


def get_update_platform_data(store_id, platform_id, verify_data: PlatVerifyData):
    """
    获取平台数据
    :return:
    """
    logging.info(u"获取平台数据")
    if verify_data is None:
        verify_data = PlatVerifyData()
    url = constant.DOMAIN + "/backStage/export/report/pingtai-performance"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.backgroundTID}
    params = {'start': variables.s_month_date_time, 'end': variables.s_month_date_time, 'store_id': store_id}
    resp = requests.get(url, params, headers=headers)
    try:
        json_data = resp.json()
        platform_array = json_data['data']['list']
        for platform in platform_array:
            if platform['platform_id'] == platform_id:
                verify_data.f_platform_sale_num = float(platform['shiji'])
                break
        logging.debug('获取平台数据成功')
    except Exception as e:
        logging.error("获取平台数据错误, %s" % e)
    return verify_data


def get_update_employee_data(store_id, employee_id, verify_data: EmployeeVerifyData):
    """
    获取员工数据
    :return:
    """
    logging.info(u"获取员工数据")
    if verify_data is None:
        verify_data = EmployeeVerifyData()
    url = constant.DOMAIN + "/backStage/export/report/employee-performance"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.backgroundTID}
    params = {'start': variables.s_month_date_time, 'end': variables.s_month_date_time, 'store_id': store_id}
    resp = requests.get(url, params, headers=headers)
    try:
        json_data = resp.json()
        employee_array = json_data['data']['list']
        for employee in employee_array:
            if employee['employee_id'] == employee_id:
                verify_data.i_employee_sale_num = int(employee['shiji'])
                break
        logging.debug('获取员工数据成功')
    except Exception as e:
        logging.error("获取员工数据错误, %s" % e)
    return verify_data
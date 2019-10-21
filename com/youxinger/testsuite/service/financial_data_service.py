import requests

from com.youxinger.testsuite.bean.lc_global import LCGlobalVerifyData
from com.youxinger.testsuite.utils import constant, variables
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
        verify_data.i_lc_global_arrive_store_num = json_data['data']['arrive_store_num']
        verify_data.i_lc_global_bhm_percent = json_data['data']['bhm_percent']
        verify_data.i_lc_global_newvip_num = json_data['data']['newvip_num']
        verify_data.i_lc_global_newvip_order_percent = json_data['data']['newvip_order_percent']
        verify_data.i_lc_global_order_num = json_data['data']['order_num']
        verify_data.i_lc_global_refund_num = json_data['data']['refund_num']
        verify_data.i_lc_global_sale_num = json_data['data']['sale_num']
        verify_data.i_lc_global_sale_percent = json_data['data']['sale_percent']
        logging.error('获取总览数据成功')
    except Exception as e:
        logging.error("获取总览数据错误, %s" % e)
    return verify_data
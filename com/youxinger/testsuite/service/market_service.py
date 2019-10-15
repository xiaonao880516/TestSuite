import logging

from com.youxinger.testsuite.utils import constant, variables
import requests


def pos_order(order_parms):
    """
    pos下单并付款
    """
    logging.info(u"pos订单")
    url = constant.DOMAIN + "/frontStage/orders/new-orders"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID}
    resp = requests.post(url, order_parms, headers)
    json_data = resp.json()


def recharge_order(order_parms):
    """
    余额付款订单
    :param order_parms:
    :return:
    """


def good_shipped():
    """
    更新物流信息
    :return:
    """


def order_return():
    """
    退货
    :return:
    """


def order_exchange():
    """
    换货
    :return:
    """
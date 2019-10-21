import logging
from com.youxinger.testsuite.utils import constant, variables, util
import requests


def pos_order(order_parms):
    """
    pos下单并付款
    """
    logging.info(u"pos订单")
    url = constant.DOMAIN + "/frontStage/orders/new-orders"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID}
    resp = requests.post(url, order_parms, headers=headers)
    json_data = resp.json()
    try:
        shopping_order_id = json_data['data']['order_id']
        real_pay = json_data['data']['real_pay'].replace(".", "")
        if pos_order_pay(shopping_order_id, real_pay) is True:
            good_shipped(shopping_order_id)
    except Exception as e:
        logging.error("pos下单失败, %s" % e)
        return False


def pos_order_pay(shopping_order_id, real_pay):
    """
    pos订单付款
    :param shopping_order_id: 订单编号
    :param real_pay: 订单金额
    :return:是否付款成功
    """
    logging.debug("shopping_order_id=" + shopping_order_id + ", real_pay=" + real_pay)
    pay_key = "b2FzZGblubLmraPkuovvvIzor7fkuI3opoHov53ms5UlQCMmKlFlMWhmMQ"
    mernum = "898110256914031"
    termid = "77347852"
    trandate = "20180821"
    trantime = "163828"
    referno = "154140244647"
    pan = "481699******4413"
    val = util.md5(mernum + termid + trandate + trantime + referno + pan + real_pay + pay_key)
    url = constant.DOMAIN + "/frontStage/wfjpay/order-done"
    headers = {'Content-Type': 'text/xml'}
    body = '<?xml version="1.0" encoding="UTF-8"?><request><trandate>'+trandate+'</trandate><mernum>'+mernum+'</mernum><termid>'+termid+'</termid><referno>'+referno+'</referno><trantype>01</trantype><trantime>'+trantime+'</trantime><pan>'+pan+'</pan><sign>'+val+'</sign><amt>'+real_pay+'</amt><batchno>000003</batchno><ext1>1</ext1><ext2></ext2><paytype>1</paytype><channel>11</channel><orderId>'+shopping_order_id+'</orderId><serialno>002137</serialno></request>'
    resp = requests.post(url, body, headers=headers)
    return resp.text.__contains__('成功')


def recharge_order(order_parms):
    """
    余额付款订单
    :param order_parms:
    :return:
    """
    pass


def good_shipped(shopping_order_id):
    """
    更新物流信息，发货
    :return:
    """
    logging.info(u"总仓发货")
    try:
        export_url = constant.DOMAIN + "/backStage/orders/not-export-orders"
        export_headers = {'Accept': 'application/json, text/plain, */*',
                          'tid': variables.backgroundTID}
        export_parms = dict(start=variables.s_start_datetime, end=variables.s_end_date_time)
        export_resp = requests.post(export_url, export_parms, headers=export_headers)
        export_json_data = export_resp.json()

        delivery_url = constant.DOMAIN + "/backStage/orders/update-orders"
        delivery_headers = {'Accept': 'application/json, text/plain, */*',
                            'tid': variables.backgroundTID}
        delivery_parms = dict(order_id=shopping_order_id, tracking_number='123456789')
        delivery_resp = requests.post(delivery_url, delivery_parms, headers=delivery_headers)
        delivery_json_data = delivery_resp.json()
        return True
    except Exception as e:
        logging.error("发货失败, %s" % e)
        return False


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
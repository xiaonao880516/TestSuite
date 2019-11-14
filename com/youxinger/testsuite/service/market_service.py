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
        return shopping_order_id
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
    logging.info(u"余额订单")
    url = constant.DOMAIN + "/frontStage/orders/new-orders"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID}
    resp = requests.post(url, order_parms, headers=headers)
    json_data = resp.json()
    try:
        shopping_order_id = json_data['data']['order_id']
        if recharge_order_pay(shopping_order_id) is True:
            good_shipped(shopping_order_id)
        return shopping_order_id
    except Exception as e:
        logging.error("余额下单失败, %s" % e)
        return False


def no_recharge_order(order_parms):
    """
    余额不付款订单
    :param order_parms:
    :return:
    """
    logging.info(u"余额不支付订单")
    url = constant.DOMAIN + "/frontStage/orders/new-orders"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID}
    resp = requests.post(url, order_parms, headers=headers)
    json_data = resp.json()
    shopping_order_id = json_data['data']['order_id']
    return shopping_order_id


def cancellation_of_order(return_param):
    """
    余额取消订单
    :param order_parms:
    :return:
    """
    logging.info(u"余额取消订单")
    url = constant.DOMAIN + "/frontStage/orders/cancel-orders"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID}
    resp = requests.post(url, return_param, headers=headers)
    json_data = resp.json()


def recharge_order_pay(shopping_order_id):
    """
    余额订单付款
    :param shopping_order_id: 订单编号
    :param real_pay: 订单金额
    :return:是否付款成功
    """
    logging.info(u"余额订单付款")
    url = constant.WX_DOMAIN + "/api/lchmpFrontStage/recharge/pay-ceshi"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.foregroundTID}
    body = {'order_id': shopping_order_id}
    resp = requests.post(url, body, headers=headers)
    return resp.text.__contains__('成功')


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


def return_order(params):
    """
    退货
    :return:
    """
    after_sale_id = create_return_order(params)
    return after_sale_review(1, after_sale_id)


def create_return_order(order_params):
    """
    创建退货订单
    :return:
    """
    return_url = constant.DOMAIN + "/frontStage/aftersale/apply-return"
    return_headers = {'Accept': 'application/json, text/plain, */*',
                      'tid': variables.foregroundTID}
    resp = requests.post(return_url, order_params, headers=return_headers)
    json_data = resp.json()
    after_sale_id = json_data['data']['aftersale_id']
    return after_sale_id


def after_sale_review(review_type, after_sale_id):
    """
    售后审核
    :param review_type:售后类型
    :param after_sale_id: 售后id
    :return:
    """
    logging.info(u"审批")
    url = constant.DOMAIN + "/frontStage/aftersale/review"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.foregroundTID}
    params = dict(aftersale_id=after_sale_id, status=1, reason='审核通过', type=review_type)
    resp = requests.post(url, params, headers=headers)
    return resp.text.__contains__('成功')


def exchange_order(params):
    """
    换货
    :return:
    """
    after_sale_id = create_changer_order(params)
    return after_sale_review(2, after_sale_id)


def create_changer_order(params):
    """
    创建换货订单
    :return:
    """
    logging.info(u"换货接口")
    return_url = constant.DOMAIN + "/frontStage/aftersale/apply"
    return_headers = {'Accept': 'application/json, text/plain, */*',
                      'tid': variables.foregroundTID}
    resp = requests.post(return_url, params, headers=return_headers)
    json_data = resp.json()
    after_sale_id = json_data['data']['aftersale_id']
    return after_sale_id


def find_order_id(shopping_order_id):
    url = constant.DOMAIN + "/frontStage/vip/search-byphone"
    params = {'phone': 17151800009}
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.foregroundTID}
    resp = requests.get(url, params=params, headers=headers)
    json_data = resp.json()
    customer_array = json_data['data']
    member_number = customer_array[0]['member_number']
    print(member_number)
    try:
        url = constant.DOMAIN + '/frontStage/orders/search-orders?order_status=0&keywords=&search_type=member&member_id=' + member_number
        return_headers = {'Accept': 'application/json, text/plain, */*',
                          'tid': variables.foregroundTID}
        resp = requests.get(url, headers=return_headers)
        json_data = resp.json()
        orderList = json_data['data']['all_goods']
        print(orderList[0].order_id)
        # for i in range(0, orderList.length):
        #     if shopping_order_id == orderList[i].order_id:
        #         afterSaleOrders = orderList[i].aftersale_orders_info
        #         exchangeOrderId = afterSaleOrders[afterSaleOrders.length - 1].order_id
        #         return exchangeOrderId
    except Exception as e:
        logging.error("新单号获取失败, %s" % e)
        return False






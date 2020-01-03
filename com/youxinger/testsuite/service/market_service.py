import logging
from com.youxinger.testsuite.utils import constant, variables, util
import requests
import json

from com.youxinger.testsuite.utils.constant import  CUSTOMER_PLATFORM_SALE


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


def recharge_order(order_parms,id):
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
            if id ==1:
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


def cancellation_of_order(order_id):
    """
    余额取消订单
    :param order_parms:
    :return:
    """
    logging.info(u"余额取消订单")
    url = constant.DOMAIN + "/frontStage/orders/cancel-orders"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID}
    delivery_parms = dict(order_id=order_id)
    resp = requests.post(url,delivery_parms, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '操作成功':
        logging.info('取消成功')
    else:
        logging.info('取消失败')


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
    order_params['is_confirm'] = '0'
    return_url = constant.DOMAIN + "/frontStage/aftersale/apply-return"
    return_headers = {'Accept': 'application/json, text/plain, */*',
                      'tid': variables.foregroundTID}
    resp = requests.post(return_url, order_params, headers=return_headers)
    json_data = resp.json()
    request_refund_result = json_data['msg']
    if request_refund_result == "SUCCESS":
        order_params['is_confirm'] = '1'
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


def find_order_id(shopping_order_id, member_number):
    """
    获取换货时生成的新订单order_id
    :return:
    """
    try:
        url = constant.DOMAIN + '/frontStage/orders/search-orders?order_status=0&keywords=&search_type=member&member_id=' + member_number
        return_headers = {'Accept': 'application/json, text/plain, */*',
                          'tid': variables.foregroundTID}
        resp = requests.get(url, headers=return_headers)
        json_data = resp.json()
        orderList = json_data['data']['all_goods']
        for i in range(0, len(orderList)):
            if shopping_order_id == orderList[i]['order_id']:
                afterSaleOrders = orderList[i]['aftersale_orders_info']
                exchangeOrderId = afterSaleOrders[len(afterSaleOrders)-1]['order_id']
                return exchangeOrderId
    except Exception as e:
        logging.error("新单号获取失败, %s" % e)
        return False


def set_no_discount_no_score_product(product):
    """
    设置商品不折扣不积分
    :return:
    """
    url = constant.DOMAIN + "/backStage/baseinfo/goods/set-act-tag"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.backgroundTID,
               'Content-Type': 'application/json'}
    data = {'discount_switch': 'on', 'score_switch': 'on', 'tiaoma':  product}
    json_str = json.dumps(data)
    resp = requests.post(url, json_str, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '操作成功':
        logging.info('设置商品不折扣不积分成功')
    else:
        logging.info('设置商品不折扣不积分失败')


def set_pre_sale_product(sku_id, num):
    """
    设置预售商品发售不发售
    :return:
    """
    url = constant.DOMAIN + "/backStage/baseinfo/goods/sale"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.backgroundTID,
               'Content-Type': 'application/json'}
    data = {'id': sku_id, 'on_sale': num}
    json_str = json.dumps(data)
    resp = requests.post(url, json_str, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '操作成功':
        logging.info('成功')
    else:
        logging.info('失败')


def presell_pos(order_parms):
    """
    生成预售订单
    """
    logging.info(u"pos订单")
    json_str = json.dumps(order_parms)
    url = constant.DOMAIN + "/frontStage/orders/presale/ordain"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID,
               'Content-Type': 'application/json'}
    resp = requests.post(url, json_str, headers=headers)
    json_data = resp.json()
    try:
        shopping_order_id = json_data['data']['record_id']
        real_pay = json_data['data']['price'].replace(".", "")
        if list(order_parms.values())[5] == "recharge":
            recharge_order_pay(shopping_order_id)
        else:
            pos_order_pay(shopping_order_id, real_pay)
        return shopping_order_id
    except Exception as e:
        logging.error("pos下单失败, %s" % e)
        return False


def choose_size(param,id):
    """
    生成预售转订单
    """
    logging.info(u"预售选码")
    json_str = json.dumps(param)
    url = constant.DOMAIN + "/frontStage/orders/presale/new-orders"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID,
               'Content-Type': 'application/json'}
    resp = requests.post(url, json_str, headers=headers)
    json_data = resp.json()
    order_id = json_data['data']['order_id']
    recharge_order_pay(order_id)
    if id ==1:
       good_shipped(order_id)
    return order_id


def cancel_booking(record_id):
    logging.info(u"取消预售订单")
    url = constant.DOMAIN + "/frontStage/orders/presale/cancel-presale"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID}
    delivery_parms = dict(record_id=record_id)
    resp = requests.post(url, delivery_parms, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '操作成功':
        logging.info('取消预售成功')

    else:
        logging.info('取消预售失败')


def jifen(param):
    """
    更新会员的验证数据
    :param is_operated: True：执行操作之后， False：执行操作之前
    :param customer: 会员对象
    :return:
    """
    logging.info(u"查找会员，更新操作执行数据")
    url = constant.DOMAIN + "/frontStage/vip/search-byphone"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.foregroundTID}
    resp = requests.get(url, params=param, headers=headers)
    json_data = resp.json()
    customer_array = json_data['data'][0]['swap_score']
    return customer_array


def rewards_order(order_parms):
    """
    积分商城下单
    """
    logging.info(u" 积分商城下单")
    url = constant.DOMAIN + "/frontStage/pointsmall/order/new-orders"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID,
               'Content-Type': 'application/x-www-form-urlencoded'}
    resp = requests.post(url, order_parms, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '下单成功':
        logging.info('下单成功')
        reward = json_data['data']['order_id']

        if rewards_order_pay(reward) is True:
            rewards_order_success(reward)
        return  reward
    else:
        logging.info('下单失败')

def rewards_order_pay(order_parms):
    """
    纯积分兑换
    """
    logging.info(u"  纯积分兑换")
    url = constant.DOMAIN + "/frontStage/pointsmall/order/score-exchange"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID,
               'Content - Type': 'application / x - www - form - urlencoded'
              }
    delivery_parms = dict(order_id=order_parms)
    resp = requests.post(url, delivery_parms, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '兑换成功':
        logging.info('兑换成功')
        return True

    else:
        logging.info('兑换失败')

def rewards_order_success(order_id):
    """
    积分商城发货
    """
    logging.info(u"   积分商城发货")
    url = constant.DOMAIN + "/backStage/pointsmall/update-tracking-number"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID,
               'Content - Type': 'application / x - www - form - urlencoded'
              }
    delivery_parms = dict(order_id=order_id,tracking_number=12313)
    resp = requests.post(url, delivery_parms, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '已发货':
        logging.info('已发货成功')

    else:
        logging.info('已发货失败')

def rewards_order_refund(order_id):
    """
    积分商城退货
    """
    logging.info(u"  积分商城退货")
    url = constant.DOMAIN + "/backStage/pointsmall/aftersale/refund"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.backgroundTID,
               'Content - Type': 'application / x - www - form - urlencoded'
              }
    delivery_parms = dict(order_id=order_id,beizhu=12313,type=1)
    resp = requests.post(url, delivery_parms, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '操作成功':
        logging.info('退货成功')

    else:
        logging.info('退货失败')

def cash_refund(param):
    """
    会员余额提现
    """
    logging.info(u"  会员余额提现")
    url = constant.DOMAIN + "/backStage/vip/vipcardmanage/cash-out"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.backgroundTID,
              }

    resp = requests.post(url, param, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '操作成功':
        logging.info('提现成功')

    else:
        logging.info('提现失败')
def remainder_roll_out(param):
    """
    会员余额转出
    """
    logging.info(u"   会员余额转出")
    url = constant.DOMAIN + "/backStage/vip/vipcardmanage/remainder-roll-out"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.backgroundTID,
              }
    resp = requests.post(url, param, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '操作成功':
        logging.info('转出成功')

    else:
        logging.info('转出失败')
def change_score(param):
    """
    会员积分改变
    """
    logging.info(u"   会员积分改变")
    url = constant.DOMAIN + "/backStage/vip/vipinfo/change-score"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.backgroundTID,
              }
    resp = requests.post(url, param, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '操作成功':
        logging.info('会员积分改变成功')

    else:
        logging.info('会员积分改变失败')
def find_repository():
    """
    后台获取销售余额
    """
    logging.info(u"  后台获取销售余额")
    url = constant.DOMAIN + "/backStage/stores/platform/getlist?"+CUSTOMER_PLATFORM_SALE
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.backgroundTID,
              }
    resp = requests.get(url,headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '返回列表成功':
        logging.info('查找成功')
        repository =json_data['data']['rows']
        if int(float(repository[0]["remainder"])) == 0.00:
            return repository[0]["debt_remainder"]
        return repository[0]["remainder"]


    else:
        logging.info('查找失败')





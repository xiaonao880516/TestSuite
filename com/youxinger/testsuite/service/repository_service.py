import requests

from com.youxinger.testsuite.bean.repository import GoodVerifyData
from com.youxinger.testsuite.utils import constant, variables
import logging
import json


def get_store_repository_by_tid(is_operated, foreground_store_tid, verify_good_list: dict):
    """
    根据tid查找门店的商品库存
    :param is_operated: True：操作之后，False：操作之前
    :param foreground_store_tid: tid：确定门店
    :param verify_good_list: 要验证的商品列表
    :return:
    """
    logging.info(u"根据tid与商品条码查找门店的商品库存")
    if verify_good_list is None:
        return None
    url = constant.DOMAIN + "/frontStage/repository/inventory/search-inventory"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': foreground_store_tid}
    resp = requests.get(url, headers=headers)
    json_data = resp.json()
    goods_list = json_data['data']['goods_list']
    for good in goods_list:
        if verify_good_list.keys().__contains__(good['tiaoma']):
            if is_operated:
                verify_good_list[good['tiaoma']].i_post_quantity = int(good['num'])
            else:
                verify_good_list[good['tiaoma']].i_pre_quantity = int(good['num'])


def get_global_repository(is_operated, verify_good_list: [GoodVerifyData]):
    """
    查找总仓的商品库存
    :param is_operated: True：操作之后，False：操作之前
    :param verify_good_list: 要验证的商品列表
    :return:
    """
    logging.info(u"根据商品条码查找总仓的商品库存")
    if verify_good_list is None:
        return None
    url = constant.DOMAIN + "/backStage/baseinfo/goods/search-goods"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.backgroundTID}
    resp = requests.get(url, headers=headers)
    json_data = resp.json()
    goods_list = json_data['data']['all_goods']
    for good in goods_list:
        if verify_good_list.keys().__contains__(good['tiaoma']):
            if is_operated:
                verify_good_list[good['tiaoma']].i_post_quantity = int(good['kucun'])
            else:
                verify_good_list[good['tiaoma']].i_pre_quantity = int(good['kucun'])

def standard_request(params):
    """
    标准仓补仓申请
    :return:
    """
    apply_for_warehouse(params)
    find = {'page_size': '15', 'page_num': '1'}
    application_id = get_application_id(find)
    param = {'application_id': application_id}
    audit_pass(param)
    warehouse_express(application_id)
    confirm_the_inventory(application_id, 1)
    return application_id


def return_request(params):
    """
    标准仓退货申请
    :return:
    """
    apply_for_return(params)
    find = {'page_size': '15', 'page_num': '1'}
    return_id = get_return_id(find)
    param = {'application_id': return_id, 'tracking_number': '123456789'}
    fill_in_the_number(param)
    file = export_orders(return_id)
    # to_guide_into(file, return_id)
    return return_id


def apply_for_warehouse(param):
    """
    补仓申请
    """
    logging.info(u"补仓申请")
    url = constant.DOMAIN + "/frontStage/repository/repo/add-apply"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID,
               'Content - Type': 'application/x-www-form-urlencoded'
               }
    resp = requests.post(url, param, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '补仓申请提交成功':
        logging.info('提交补仓申请成功')
    else:
        logging.info('提交补仓申请失败')


def apply_for_return(param):
    """
    仓库退货申请
    """
    logging.info(u"补仓申请")
    url = constant.DOMAIN + "/frontStage/repository/return_application/apply-return"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID,
               'Content - Type': 'application/x-www-form-urlencoded'
               }
    resp = requests.post(url, param, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '退货申请提交成功':
        logging.info('提交退货申请成功')
    else:
        logging.info('提交退货申请失败')


def get_application_id(param):
    """
    申请补仓获取补仓id
    :return:
    """
    logging.info(u"获取补仓id")
    url = constant.DOMAIN + "/backStage/repository/addGoods/get-list"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.backgroundTID,
               }
    resp = requests.get(url, param, headers=headers)
    json_data = resp.json()
    application_id = json_data['data']['rows'][0]['application_id']
    return application_id


def get_return_id(param):
    """
    退货时获取补仓id
    :return:
    """
    logging.info(u"获取补仓id")
    url = constant.DOMAIN + "/backStage/repository/return_application/return-list"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.backgroundTID,
               }
    resp = requests.get(url, param, headers=headers)
    json_data = resp.json()
    return_id = json_data['data']['rows'][0]['return_id']
    return return_id


def audit_pass(param):
    """
    补仓审请通过
    :return:
    """
    logging.info(u"补仓审请通过")
    url = constant.DOMAIN + "/backStage/repository/addGoods/agree"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.backgroundTID,
               }
    resp = requests.post(url, param, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '已通过补仓申请':
        logging.info('补仓申请成功')
    else:
        logging.info('补仓申请失败')


def warehouse_express(application_id):
    """
    更新物流信息，发货
    :return:
    """
    logging.info(u"总仓发货")
    try:
        export_url = constant.DOMAIN + "/backStage/repository/addGoods/inbound-export"
        export_headers = {'Accept': 'application/json, text/plain, */*',
                          'tid': variables.backgroundTID}
        export_parms = dict(start=variables.s_start_datetime, end=variables.s_end_date_time, application_id=application_id)
        export_resp = requests.post(export_url, export_parms, headers=export_headers)
        export_json_data = export_resp.json()

        delivery_url = constant.DOMAIN + "/backStage/repository/addGoods/add-order-num"
        delivery_headers = {'Accept': 'application/json, text/plain, */*',
                            'tid': variables.backgroundTID}
        delivery_parms = dict(application_id=application_id, order_num='123456789')
        delivery_resp = requests.post(delivery_url, delivery_parms, headers=delivery_headers)
        delivery_json_data = delivery_resp.json()
        return True
    except Exception as e:
        logging.error("发货失败, %s" % e)
        return False


def confirm_the_inventory(application_id, type):
    """
    前台确认入库
    """
    logging.info(u"确认入库")
    url = constant.DOMAIN + "/frontStage/repository/in-repo"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID,
               }
    delivery_parms = dict(application_id=application_id, type=type)
    resp = requests.post(url, delivery_parms, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '兑换成功':
        logging.info('兑换成功')
        return True
    else:
        logging.info('兑换失败')


def fill_in_the_number(param):
    """
    填写仓库退货物流单号
    :return:
    """
    logging.info(u"填写仓库退货物流单号")
    url = constant.DOMAIN + "/frontStage/repository/return_application/add-tracking-number"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID,
               }
    resp = requests.post(url, param, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '该退货申请已发货':
        logging.info('仓库退货物流单号填写成功')
        return True
    else:
        logging.info('仓库退货物流单号填写失败')


def export_orders(return_id):
    """
    退货导出订单
    :return:
    """
    logging.info(u"导出订单")
    export_url = constant.DOMAIN + "/backStage/repository/return_application/application-export"
    export_headers = {'Accept': 'application/json, text/plain, */*',
                      'tid': variables.backgroundTID}
    export_parms = dict(start=variables.s_start_datetime, end=variables.s_end_date_time, application_id=return_id)
    export_resp = requests.post(export_url, export_parms, headers=export_headers)
    export_json_data = export_resp.json()
    if export_json_data['msg'] == '导出成功':
        file = export_json_data['data']
        logging.info('退货订单导出成功')
        return file
    else:
        logging.info('退货订单导出失败')


def to_guide_into(file, return_id):
    """
    导入退货审批
    :return:
    """
    logging.info(u"导出订单")
    export_url = constant.DOMAIN + "/backStage/repository/return_application/import-apply-goods"
    export_headers = {'Accept': 'application/json, text/plain, */*',
                      'tid': variables.backgroundTID}
    export_parms = dict(file=file, return_id=return_id)
    export_resp = requests.post(export_url, export_parms, headers=export_headers)
    export_json_data = export_resp.json()
    print(export_json_data['data'])


def examine_and_approve(param):
    """
    退货审核
    :return:
    """
    logging.info(u"导出订单")
    data = json.dumps(param)
    export_url = constant.DOMAIN + "/backStage/repository/return_application/apply-return"
    export_headers = {'Accept': 'application/json, text/plain, */*',
                      'Content-Type': 'application/json;charset=UTF-8',
                      'tid': variables.backgroundTID}
    export_resp = requests.post(export_url, data=data, headers=export_headers)
    export_json_data = export_resp.json()
    if export_json_data['msg'] == '审核成功':
        logging.info('退货订单审核成功')
        return True
    else:
        logging.info('退货订单审核失败')


def search_information(keywords):
    """
    查询总览仓库的商品库存
    :return:
    """
    logging.info(u"导出订单")
    export_url = constant.DOMAIN + "/backStage/repository/baseinfo/goods/search-goods"
    export_headers = {'Accept': 'application/json, text/plain, */*',
                      'tid': variables.backgroundTID}
    export_parms = dict(keywords=keywords)
    export_resp = requests.get(export_url, export_parms, headers=export_headers)
    export_json_data = export_resp.json()
    sp = export_json_data['data']['all_goods'][0]['kucun']
    return sp


def balance_of_warehouse(repository_id):
    """
    查询可补货金额
    :return:
    """
    logging.info(u"导出订单")
    export_url = constant.DOMAIN + "/backStage/repository/inventory/search-inventory"
    export_headers = {'Accept': 'application/json, text/plain, */*',
                      'tid': variables.backgroundTID}
    export_parms = dict(repository_id=repository_id)
    export_resp = requests.get(export_url, export_parms, headers=export_headers)
    export_json_data = export_resp.json()
    ye = export_json_data['data']['repo_info']['available_money']
    return ye


def edit_the_warehouse(repository_id, repository_name, repo_type, repo_discount, max_money, store_id):
    """
    编辑仓库为标准仓还是余额仓
    :return:
    """
    logging.info(u"导出订单")
    export_url = constant.DOMAIN + "/backStage/repository/repo/update"
    export_headers = {'Accept': 'application/json, text/plain, */*',
                      'tid': variables.backgroundTID}
    export_parms = dict(repository_id=repository_id, repository_name=repository_name, repo_type=repo_type, repo_discount=repo_discount, max_money=max_money, store_id=store_id)
    export_resp = requests.post(export_url, export_parms, headers=export_headers)
    export_json_data = export_resp.json()
    if export_json_data['msg'] == '更新成功':
        logging.info('仓库变更成功')
        return True
    else:
        logging.info('仓库变更失败')


def find_warehouse(sid):
    """
    通过门店编号查询门店下的仓库编号和仓库名称
    :return:
    """
    logging.info(u"导出订单")
    export_url = constant.DOMAIN + "/backStage/repository/repo/get-list"
    export_headers = {'Accept': 'application/json, text/plain, */*',
                      'tid': variables.backgroundTID}
    export_parms = dict(sid=sid)
    export_resp = requests.get(export_url, export_parms, headers=export_headers)
    export_json_data = export_resp.json()
    repository_id = export_json_data['data']['rows'][0]['repository_id']
    repository_name = export_json_data['data']['rows'][0]['repository_name']
    return repository_id, repository_name

import requests

from com.youxinger.testsuite.bean.repository import GoodVerifyData
from com.youxinger.testsuite.utils import constant, variables
import logging


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
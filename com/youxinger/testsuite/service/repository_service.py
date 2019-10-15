import requests
from com.youxinger.testsuite.utils import constant, variables
import logging


# 根据tid查找门店的商品库存
def get_store_repository_by_tid(foreground_store_tid, goods_code: list):
    logging.info(u"根据tid与商品条码查找门店的商品库存")
    if goods_code is None:
        return None
    url = constant.DOMAIN + "/frontStage/repository/inventory/search-inventory"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': foreground_store_tid}
    resp = requests.get(url, headers=headers)
    json_data = resp.json()
    goods_list = json_data['data']['goods_list']
    store_repository = dict()
    for code in goods_code:
        has_code = False
        for good in goods_list:
            if code == good['tiaoma']:
                store_repository[code] = int(good['num'])
                has_code = True
                break
        if has_code is False:
            store_repository[code] = 0
    return store_repository


# 查找总仓的商品库存
def get_main_repository(goods_code: list):
    logging.info(u"根据商品条码查找总仓的商品库存")
    if goods_code is None:
        return None
    url = constant.DOMAIN + "/backStage/baseinfo/goods/search-goods"
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.backgroundTID}
    resp = requests.get(url, headers=headers)
    json_data = resp.json()
    goods_list = json_data['data']['all_goods']
    main_repository = dict()
    for code in goods_code:
        has_code = False
        for good in goods_list:
            if code == good['tiaoma']:
                main_repository[code] = int(good['kucun'])
                has_code = True
                break
        if has_code is False:
            main_repository[code] = 0
    return main_repository
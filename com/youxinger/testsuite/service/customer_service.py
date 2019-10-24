import requests

from com.youxinger.testsuite.bean.customer import Customer, CustomerVerifyData
from com.youxinger.testsuite.bean.employee import Employee
from com.youxinger.testsuite.bean.platform import Platform
from com.youxinger.testsuite.utils import constant
from com.youxinger.testsuite.utils import variables
import logging
import copy


def register_customer(customer_info, employee: Employee, platform: Platform):
    """
    注册用户
    :param customer_info: 配置会员对象
    :param employee: 员工信息
    :param platform: 平台信息
    :return: 会员对象
    """
    customer = get_customer_by_phone(customer_info['phone'])
    if customer is not None:
        del_customer(customer)
        return register_customer(customer_info, employee, platform)
    else:
        logging.info(u"注册会员")
        url = constant.WX_DOMAIN + "/api/lchmpFrontStage/reg"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = copy.deepcopy(customer_info)
        if employee is not None:
            data['employee_number'] = employee.employee_id
            if platform is not None:
                data['platform_number'] = platform.platform_id
        resp = requests.post(url, data, headers=headers)
        json_data = resp.json()
        if json_data['msg'] == '注册成功!':
            customer = get_customer_by_phone(customer_info['phone'])
            ___add_customer_address(customer, customer_info)
            customer.sex = customer_info['sex']
            customer.birthday = customer_info['birthday']
            customer.openid = customer_info['openid']
            customer.address = customer_info['address']
            customer.area = customer_info['area']
            customer.city = customer_info['city']
            customer.province = customer_info['province']
            customer.consignee = customer_info['consignee']
            customer.consignee_phone = customer_info['phone']
            customer.employee = employee
            customer.platform = platform
            return customer
        else:
            raise Exception('会员注册失败')


def ___add_customer_address(customer: Customer, customer_info):
    """
    会员增加收货地址
    :param customer: 会员对象
    :param customer_info: 配置会员对象
    :return:
    """
    logging.info(u"会员增加收获地址")
    if customer is None:
        return
    url = constant.DOMAIN + "/frontStage/vip/address/create-address"
    headers = {'Accept': 'application/json, text/plain, */*',
               'tid': variables.foregroundTID}
    customer_address = dict(address=customer_info['address'], area=customer_info['area'],
                            city=customer_info['city'], province=customer_info['province'],
                            consignee=customer_info['consignee'], is_default=customer_info['is_default'],
                            consignee_phone=customer_info['phone'],
                            member_number=customer.member_number)
    resp = requests.post(url, customer_address, headers=headers)
    json_data = resp.json()
    if json_data['msg'] == '操作成功':
        pass
    else:
        raise Exception('会员增加收获地址失败')


def get_customer_by_phone(phone: str):
    """
    根据手机号获取会员
    :param phone: 手机号
    :return:会员对象
    """
    logging.info(u"根据手机号获取会员")
    if (phone is None) or phone == "":
        return None
    url = constant.DOMAIN + "/frontStage/vip/search-byphone"
    params = {'phone': phone}
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.foregroundTID}
    resp = requests.get(url, params=params, headers=headers)
    json_data = resp.json()
    customer_array = json_data['data']
    if customer_array == '':
        logging.debug(u"查找会员，会员不存在")
        return None
    else:
        logging.debug(u"查找会员，会员存在")
        try:
            customer = Customer()
            customer.member_number = customer_array[0]['member_number']
            customer.name = customer_array[0]['real_name']
            customer.phone = customer_array[0]['phone']
            return customer
        except TypeError:
            raise Exception('查找会员，查找会员异常')


def update_customer_verify_data(is_operated: bool, customer: Customer):
    """
    更新会员的验证数据
    :param is_operated: True：执行操作之后， False：执行操作之前
    :param customer: 会员对象
    :return:
    """
    logging.info(u"查找会员，更新操作执行后数据")
    if (customer is None) or customer.phone == "":
        return
    url = constant.DOMAIN + "/frontStage/vip/search-byphone"
    params = {'phone': customer.phone}
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.foregroundTID}
    resp = requests.get(url, params=params, headers=headers)
    json_data = resp.json()
    customer_array = json_data['data']
    if customer_array == '':
        logging.debug(u"查找会员，会员不存在")
    else:
        __update_customer_verify_data(is_operated, customer, customer_array)
        logging.debug(u"查找会员，会员存在")


def __update_customer_verify_data(is_operated, customer: Customer, customer_array):
    """
    更新会员的验证数据
    :param is_operated: True：执行操作之后， False：执行操作之前
    :param customer: 会员对象
    :param customer_array: 实际值
    :return:
    """
    try:
        verify_data = CustomerVerifyData()
        verify_data.i_total_consume = int(customer_array[0]['total_consume'])
        verify_data.i_swap_score = int(customer_array[0]['swap_score'])
        verify_data.i_card_level = int(customer_array[0]['card_level'])
        verify_data.i_remainder = __get_customer_balance(customer)
        if is_operated is True:
            customer.postVerifyData = verify_data
        else:
            customer.preVerifyData = verify_data
    except TypeError:
        raise Exception('查找会员，查找会员异常')


def __get_customer_balance(customer: Customer):
    """
    查找并保存会员余额
    :param customer: 会员对象
    :return: 余额
    """
    logging.info(u"查找并保存会员余额")
    if (customer is None) or customer.member_number == "":
        return
    url = constant.DOMAIN + "/frontStage/customer/get-balance"
    params = {'member_number': customer.member_number}
    headers = {'Accept': 'application/json, text/plain, */*', 'tid': variables.foregroundTID}
    resp = requests.get(url, params=params, headers=headers)
    json_data = resp.json()
    return int(float(json_data['data']['remainder']))


def recharge_customer(customer: Customer, remainder):
    """
    会员充值, 创建充值订单
    :param customer: 会员对象
    :param remainder: 充值额
    :return:
    """
    logging.info(u"会员充值， 创建充值订单")
    if customer is not None:
        url = constant.DOMAIN + "/frontStage/recharge/generate-order"
        headers = {'Accept': 'application/json, text/plain, */*',
                   'tid': variables.foregroundTID}
        recharge_data = {'amount': remainder, 'channel': 'pos', 'member_number': customer.member_number}
        resp = requests.post(url, recharge_data, headers=headers)
        json_data = resp.json()
        charge_order_id = json_data['data']
        __charge_order_pay(charge_order_id)


def __charge_order_pay(charge_order_id):
    """
    充值订单付款
    :param charge_order_id: 充值订单
    :return:
    """
    logging.info(u"充值订单付款")
    url = constant.DOMAIN + "/frontStage/recharge/ceshi"
    order_data = {'order_id': charge_order_id}
    resp = requests.post(url, order_data)
    json_data = resp.json()
    if json_data['msg'] == 'ok':
        pass
    else:
        raise Exception('会员充值失败')


def del_customer(customer: Customer):
    """
    会员删除
    :param customer:
    :return:
    """
    logging.info(u"删除会员")
    if customer is not None:
        url = constant.DOMAIN + "/backStage/vip/vipinfo/del-vip"
        headers = {'Accept': 'application/json, text/plain, */*',
                   'tid': variables.backgroundTID}
        customer_data = {'member_number': customer.member_number}
        resp = requests.post(url, customer_data, headers=headers)
        json_data = resp.json()
        if json_data['msg'] == '删除成功':
            pass
        else:
            raise Exception('会员删除失败')

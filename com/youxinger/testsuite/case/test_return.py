from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service


class TestGeneralGoods(BaseCase):
    """
    一般商品测试
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 会员充值40000
        cls._customer.recharge(40000)

    def setUp(self):
        super().setUp()
        # 更新充值前的验证数据
        self._test_data.update_pre_verify_data()

    def tearDown(self):
        super().tearDown()

    def test_1_recharge_shopping_order(self):
        """
        charge门店总仓混合下单单购物成功检测
        腰背夹M216C237，深蓝色，58 总仓5个，门店5个
        :return:
        """
        logging.debug("test_1_recharge_shopping_order")
        order_param = {'price': '33800.00', 'discount_money': '2704.00', 'real_pay': '31096.00', 'receive_name': self._customer.consignee, 'receive_phone': self._customer.phone,
                       'receive_sheng': self._customer.province, 'receive_shi': self._customer.city, 'receive_diqu': self._customer.area, 'receive_address': self._customer.address,
                       'member_id': self._customer.member_number, 'member_name': self._customer.name, 'member_phone': self._customer.phone,
                       'plateform_id': self._customer.platform.platform_id, 'special_employee_id': self._customer.employee.employee_id, 'discount_rate': '0.92',
                       'goods_list[0][danjia]': '3380.00', 'goods_list[0][sku_num]': '10', 'goods_list[0][sku_name]': '腰背夹',
                       'goods_list[0][price]': '33800.00', 'goods_list[0][real_pay_price]': '31096.00', 'goods_list[0][discount_price]': '2704.00',
                       'goods_list[0][sku_id]': '4878', 'goods_list[0][tiaoma]': 'M216C237C0458', 'goods_list[0][kuanhao]': 'M216C237',
                       'goods_list[0][sku_detail]': '深蓝色 58', 'goods_list[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
                       'goods_list[0][repo_out_num]': '5', 'goods_list[0][com_out_num]': '5', 'goods_list[0][no_discount]': '0', 'goods_list[0][no_score]': '0',
                       'goods_list[0][is_active]': '0', 'goods_list[0][type]': '1', 'pay_type': 'recharge', 'zip_code': '', 'referral_phone': '', 'beizhu': '',
                       'discount_id': '', 'discount_description': '', 'coupon_id': '', 'coupon_discount_amount': '0.00', 'coupon_discount_rate': ''}
        # 下单购物
        globals()['shopping_order_id'] = market_service.recharge_order(order_param)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 验证值
        self.expectedData(31096  # 会员消费额
                          , 0  # 会员积分
                          , 2  # 会员卡等级
                          , -31096  # 会员余额
                          , 1  # 总揽到店次数
                          , 0  # 总揽新增会员数
                          , 1  # 总揽订单数
                          , 0  # 总揽退单数
                          , 31096  # 总揽销售总额
                          , -5  # M216C237C0458总仓库存
                          , 0  # M216C237C0464总仓库存
                          , 0  # M116E248B0158总仓库存
                          , 0  # M116E248B0164总仓库存
                          , 0  # M316J232B01106总仓库存
                          , 0  # M316J232B0176总仓库存
                          , 0  # ZH02B215190T796242总仓库存
                          , 3.11  # 验证值
                          , -5  # M216C237C0458门店库存
                          , 0  # M216C237C0464门店库存
                          , 0  # M116E248B0158门店库存
                          , 0  # M116E248B0164门店库存
                          , 0  # M316J232B01106门店库存
                          , 0  # M316J232B0176门店库存
                          , 0  # ZH02B215190T796242门店库存
                          , 1  # 门店到店次数期待增加值
                          , 0  # 门店新增会员数期待增加值
                          , 1  # 门店订单数期待增加值
                          , 0  # 门店退单数期待增加值
                          , 31096  # 门店销售总额期待增加值
                          , 31096  # 门店平台销售总额期待增加值
                          )
        # 验证数据
        self._data_assertion()

    def test_2_changer_10pieces(self):
        """
        换货10件商品数据
        腰背夹M216C237，深蓝色，58 换10个 腰背夹M216C237C0464， 深蓝色，64
        :return:
        """
        logging.debug("test_2_changer_10pieces")
        if globals()['shopping_order_id'] is not None:
            exchange_order_id = globals()['shopping_order_id'] + "_0"
            params = {'sub_order_id': exchange_order_id, 'goods_num': '10', 'goods_total_price': '31096.00', 'reason': '尺码不合适', 'remarks': '换货', 'type': '2','goods_type': '1',
                      'goods_list': '[{"num":10,"sku_id":"4879","sku_name":"腰背夹","sku_detail":"深蓝色 64","tiaoma":"M216C237C0464","kuanhao":"M216C237","danjia":"3380.00","img":"https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg"}]',
                      }

            market_service.exchange_order(params)
            # 更新充值后的验证数据
            self._test_data.update_post_verify_data()
            # 验证值
            self.expectedData(  0# 会员消费额
                              , 0 # 会员积分
                              , 2 # 会员卡等级
                              , 0 # 会员余额
                              , 0 # 总揽到店次数
                              , 0 # 总揽新增会员数
                              , 1 # 总揽订单数
                              , 0 # 总揽退单数
                              , 0 # 总揽销售总额
                              , 0 # M216C237C0458总仓库存
                              , 0 # M216C237C0464总仓库存
                              , 0 # M116E248B0158总仓库存
                              , 0 # M116E248B0164总仓库存
                              , 0 # M316J232B01106总仓库存
                              , 0 # M316J232B0176总仓库存
                              , 0 # ZH02B215190T796242总仓库存
                              , 0 # 验证值
                              , 10 # M216C237C0458门店库存
                              , -10 # M216C237C0464门店库存
                              , 0 # M116E248B0158门店库存
                              , 0 # M116E248B0164门店库存
                              , 0 # M316J232B01106门店库存
                              , 0 # M316J232B0176门店库存
                              , 0 # ZH02B215190T796242门店库存
                              , 0 # 门店到店次数期待增加值
                              , 0 # 门店新增会员数期待增加值
                              , 1 # 门店订单数期待增加值
                              , 0 # 门店退单数期待增加值
                              , 0 # 门店销售总额期待增加值
                              , 0 # 门店平台销售总额期待增加值
                              )
            # 验证数据
            self._data_assertion()

    def test_3_return_10pieces(self):
        """
        退货10件商品数据
        腰背夹M216C237，深蓝色，64 退10个
        :return:
        """
        logging.debug("test_3_return_10pieces")
        shopping_order_id = globals()['shopping_order_id']
        member_number = self._customer.member_number
        exchangeOrderId = market_service.find_order_id(shopping_order_id,member_number)
        return_order_id = exchangeOrderId + "_0"
        return_param = {'main_order_id': exchangeOrderId, 'return_price': '31096.00', 'reason': '15天无理由退货', 'remarks': '退货10件',
                        'afterSales_info[0][order_id]': return_order_id, 'afterSales_info[0][danjia]': '3380.00', 'afterSales_info[0][sku_name]':'腰背夹',
                        'afterSales_info[0][sku_detail]': '深蓝色 64', 'afterSales_info[0][tiaoma]': 'M216C237C0464', 'afterSales_info[0][kuanhao]': 'M216C237',
                        'afterSales_info[0][sku_id]': '4879', 'afterSales_info[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
                        'afterSales_info[0][aftersale_num]': '10', 'afterSales_info[0][aftersale_money]':  '31096.00', 'afterSales_info[0][goods_type]': '1'}
        market_service.return_order(return_param)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 验证值
        self.expectedData(-31096.00 # 会员消费额
                              , 0 # 会员积分
                              , 2 # 会员卡等级
                              , 31096 # 会员余额
                              , 0 # 总揽到店次数
                              , 0 # 总揽新增会员数
                              , 0 # 总揽订单数
                              , 1 # 总揽退单数
                              , 31096.00 # 总揽销售总额
                              , 0 # M216C237C0458总仓库存
                              , 0 # M216C237C0464总仓库存
                              , 0 # M116E248B0158总仓库存
                              , 0 # M116E248B0164总仓库存
                              , 0 # M316J232B01106总仓库存
                              , 0 # M316J232B0176总仓库存
                              , 0 # ZH02B215190T796242总仓库存
                              , -3.11 # 验证值
                              , 0 # M216C237C0458门店库存
                              , 10 # M216C237C0464门店库存
                              , 0 # M116E248B0158门店库存
                              , 0 # M116E248B0164门店库存
                              , 0 # M316J232B01106门店库存
                              , 0 # M316J232B0176门店库存
                              , 0 # ZH02B215190T796242门店库存
                              , 0 # 门店到店次数期待增加值
                              , 0 # 门店新增会员数期待增加值
                              , 0 # 门店订单数期待增加值
                              , 1 # 门店退单数期待增加值
                              , -31096.00 # 门店销售总额期待增加值
                              , -31096.00 # 门店平台销售总额期待增加值
                              )
        # 验证数据
        self._data_assertion()



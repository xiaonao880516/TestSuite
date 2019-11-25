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

    def test_1_pos_shopping_order(self):
        """
        pos门店下单单购物成功检测
        男士塑身背心M316J232，黑色，106 门店2个
        :return:
        """
        logging.debug("test_pos_shopping_order")
        order_param = {'price': '5320.00', 'discount_money': '0.00', 'real_pay': '5320.00', 'receive_name': self._customer.consignee, 'receive_phone': self._customer.phone,
                       'receive_sheng': self._customer.province, 'receive_shi': self._customer.city, 'receive_diqu': self._customer.area, 'receive_address': self._customer.address,
                       'member_id': self._customer.member_number, 'member_name': self._customer.name, 'member_phone': self._customer.phone,
                       'plateform_id': self._customer.platform.platform_id, 'special_employee_id': self._customer.employee.employee_id, 'discount_rate': '0.92',
                       'goods_list[0][danjia]': '2660.00', 'goods_list[0][sku_num]': '2', 'goods_list[0][sku_name]': '男士塑身背心',
                       'goods_list[0][price]': '5320.00', 'goods_list[0][real_pay_price]': '5320.00', 'goods_list[0][discount_price]': '0.00',
                       'goods_list[0][sku_id]': '4996', 'goods_list[0][tiaoma]': 'M316J232B01106', 'goods_list[0][kuanhao]': 'M316J232',
                       'goods_list[0][sku_detail]': '黑色 106', 'goods_list[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010526413875910.jpg',
                       'goods_list[0][repo_out_num]': '2', 'goods_list[0][com_out_num]': '0', 'goods_list[0][no_discount]': '1', 'goods_list[0][no_score]': '1',
                       'goods_list[0][is_active]': '0', 'goods_list[0][type]': '1', 'pay_type': 'pos', 'zip_code': '', 'referral_phone': '', 'beizhu': '',
                       'discount_id': '', 'discount_description': '', 'coupon_id': '', 'coupon_discount_amount': '0.00', 'coupon_discount_rate': ''}
        # 下单购物
        globals()['shopping_order_id'] = market_service.pos_order(order_param)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 验证值
        self.expectedData(5320.00  # 会员消费额
                          , 0  # 会员积分
                          , 2  # 会员卡等级
                          , 0  # 会员余额
                          , 1  # 总揽到店次数
                          , 0  # 总揽新增会员数
                          , 1  # 总揽订单数
                          , 0  # 总揽退单数
                          , 5320.00  # 总揽销售总额
                          , 0  # M216C237C0458总仓库存
                          , 0  # M216C237C0464总仓库存
                          , 0  # M116E248B0158总仓库存
                          , 0  # M116E248B0164总仓库存
                          , 0  # M316J232B01106总仓库存
                          , 0  # M316J232B0176总仓库存
                          , 0  # ZH02B215190T796242总仓库存
                          , 0.53  # 验证值
                          , 0  # M216C237C0458门店库存
                          , 0  # M216C237C0464门店库存
                          , 0  # M116E248B0158门店库存
                          , 0  # M116E248B0164门店库存
                          , -2  # M316J232B01106门店库存
                          , 0  # M316J232B0176门店库存
                          , 0  # ZH02B215190T796242门店库存
                          , 1  # 门店到店次数期待增加值
                          , 0  # 门店新增会员数期待增加值
                          , 1  # 门店订单数期待增加值
                          , 0  # 门店退单数期待增加值
                          , 5320.00  # 门店销售总额期待增加值
                          , 5320.00  # 门店平台销售总额期待增加值
                          )
        # 验证数据
        self._data_assertion()

    def test_2_changer_some(self):
        """
        换货1件商品数据
        男士塑身背心M316J232，黑色，106 换 黑色 76
        :return:
        """
        logging.debug("test_2_changer_10pieces")
        if globals()['shopping_order_id'] is not None:
            exchange_order_id = globals()['shopping_order_id'] + "_0"
            params = {'sub_order_id': exchange_order_id, 'goods_num': '1', 'goods_total_price': '2660.00', 'reason': '30天无理由换货', 'remarks': '哈哈', 'type': '2',
                      'goods_list': '[{"num":1,"sku_id":"4997","sku_name":"男士塑身背心","sku_detail":"黑色 76","tiaoma":"M316J232B0176","kuanhao":"M316J232","danjia":"2660.00","img":"https://lchapp.oss-cn-beijing.aliyuncs.com/2019010526413875910.jpg"}]'
                      }

            market_service.exchange_order(params)
            # 更新充值后的验证数据
            self._test_data.update_post_verify_data()
            # 验证值
            self.expectedData( 0 # 会员消费额
                              ,0 # 会员积分
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
                              , 0 # M216C237C0458门店库存
                              , 0 # M216C237C0464门店库存
                              , 0 # M116E248B0158门店库存
                              , 0 # M116E248B0164门店库存
                              , 1 # M316J232B01106门店库存
                              , -1 # M316J232B0176门店库存
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

    def test_3_return_some(self):
        """
        退货1件商品
        1件选择 男士塑身背心 黑色 76
        :return:
        """
        logging.debug("test_return_some")
        shopping_order_id = globals()['shopping_order_id']
        member_number = self._customer.member_number
        exchangeOrderId = market_service.find_order_id(shopping_order_id, member_number)
        return_order_id0 = exchangeOrderId + "_0"
        return_param = {'main_order_id': exchangeOrderId, 'return_price': '2660.00', 'reason': '拍错/不想要', 'remarks': '非', 'afterSales_info[0][order_id]': return_order_id0, 'afterSales_info[0][danjia]': '2660.00',
                        'afterSales_info[0][sku_name]': '男士塑身背心', 'afterSales_info[0][sku_detail]': '黑色 76', 'afterSales_info[0][tiaoma]': 'M316J232B0176', 'afterSales_info[0][kuanhao]': 'M316J232',
                        'afterSales_info[0][sku_id]': '4997', 'afterSales_info[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010526413875910.jpg', 'afterSales_info[0][aftersale_num]': '1',
                        'afterSales_info[0][aftersale_money]': '2660.00', 'afterSales_info[0][goods_type]': '1'}
        market_service.return_order(return_param)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 验证值
        self.expectedData(-2660 # 会员消费额
                              , 0 # 会员积分
                              , 2 # 会员卡等级
                              , 0 # 会员余额
                              , 0 # 总揽到店次数
                              , 0 # 总揽新增会员数
                              , 0 # 总揽订单数
                              , 0 # 总揽退单数
                              , -2660 # 总揽销售总额
                              , 0 # M216C237C0458总仓库存
                              , 0 # M216C237C0464总仓库存
                              , 0 # M116E248B0158总仓库存
                              , 0 # M116E248B0164总仓库存
                              , 0 # M316J232B01106总仓库存
                              , 0 # M316J232B0176总仓库存
                              , 0 # ZH02B215190T796242总仓库存
                              , -0.27 # 验证值
                              , 0 # M216C237C0458门店库存
                              , 0 # M216C237C0464门店库存
                              , 0 # M116E248B0158门店库存
                              , 0 # M116E248B0164门店库存
                              , 0 # M316J232B01106门店库存
                              , 1 # M316J232B0176门店库存
                              , 0 # ZH02B215190T796242门店库存
                              , 0 # 门店到店次数期待增加值
                              , 0 # 门店新增会员数期待增加值
                              , 0 # 门店订单数期待增加值
                              , 0 # 门店退单数期待增加值
                              , -2660 # 门店销售总额期待增加值
                              , -2660 # 门店平台销售总额期待增加值
                              )
        # 验证数据
        self._data_assertion()

    def test_4_return_other(self):
        """
        退货1件商品
        1件选择 男士塑身背心 黑色 106
        :return:
        """
        logging.debug("test_return_some")
        if globals()['shopping_order_id'] is not None:
            return_order_id0 = globals()['shopping_order_id'] + "_0"
            return_param = {'main_order_id': globals()['shopping_order_id'], 'return_price': '2660.00', 'reason': '拍错/不想要', 'remarks': '适当', 'afterSales_info[0][order_id]': return_order_id0, 'afterSales_info[0][danjia]': '2660.00',
                            'afterSales_info[0][sku_name]': '男士塑身背心', 'afterSales_info[0][sku_detail]': '黑色 106', 'afterSales_info[0][tiaoma]':'M316J232B01106', 'afterSales_info[0][kuanhao]': 'M316J232',
                            'afterSales_info[0][sku_id]': '4996', 'afterSales_info[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010526413875910.jpg', 'afterSales_info[0][aftersale_num]': '1',
                            'afterSales_info[0][aftersale_money]': '2660.00', 'afterSales_info[0][goods_type]': '1'}

            market_service.return_order(return_param)
            # 更新充值后的验证数据
            self._test_data.update_post_verify_data()
            # 验证值
            self.expectedData(-2660 # 会员消费额
                              , 0 # 会员积分
                              , 2 # 会员卡等级
                              , 0 # 会员余额
                              , 0 # 总揽到店次数
                              , 0 # 总揽新增会员数
                              , 0 # 总揽订单数
                              , 0 # 总揽退单数
                              , -2660 # 总揽销售总额
                              , 0 # M216C237C0458总仓库存
                              , 0 # M216C237C0464总仓库存
                              , 0 # M116E248B0158总仓库存
                              , 0 # M116E248B0164总仓库存
                              , 0 # M316J232B01106总仓库存
                              , 0 # M316J232B0176总仓库存
                              , 0 # ZH02B215190T796242总仓库存
                              , -0.27 # 验证值
                              , 0 # M216C237C0458门店库存
                              , 0 # M216C237C0464门店库存
                              , 0 # M116E248B0158门店库存
                              , 0 # M116E248B0164门店库存
                              , 1 # M316J232B01106门店库存
                              , 0 # M316J232B0176门店库存
                              , 0 # ZH02B215190T796242门店库存
                              , 0 # 门店到店次数期待增加值
                              , 0 # 门店新增会员数期待增加值
                              , 0 # 门店订单数期待增加值
                              , 0 # 门店退单数期待增加值
                              , -2660 # 门店销售总额期待增加值
                              , -2660 # 门店平台销售总额期待增加值
                              )
            # 验证数据
            self._data_assertion()
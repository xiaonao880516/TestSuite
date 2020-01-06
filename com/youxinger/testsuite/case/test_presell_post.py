from com.youxinger.testsuite.bean.customer import CustomerVerifyData
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
        self._test_data_re.update_pre_verify_data()

    def tearDown(self):
        super().tearDown()

    def test_1_presell_post_order(self):
        """
        pos下单
        YS5130N748574 预售商品 不累计积分
        """
        logging.debug("test_1_presell_post_order")
        market_service.set_pre_sale_product('6430', '2')
        recharge_param = {'member_id': self._customer.member_number, 'member_name': self._customer.name, 'member_phone': self._customer.phone,
                          'plateform_id': self._customer.platform.platform_id, 'special_employee_id': self._customer.employee.employee_id, 'pay_type': 'pos',
                          'goods_info': {"sku_num": "1", "sku_name": "周自动化测试勿动", "sku_id": "6430", "tiaoma": "YS5130N748574", "price": "1000.00", "kuanhao": "", "sku_detail": "", "img": "https://lchapp.oss-cn-beijing.aliyuncs.com/2019112610521983674.jpg"}
                          }
        # 下单购物
        globals()['shopping_order_id'] = market_service.presell_pos(recharge_param)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        self._test_data_re.update_post_verify_data()
        # 验证值
        self.expectedData(0  # 会员消费额
                          , 0  # 会员积分
                          , 2  # 会员卡等级
                          , 0  # 会员余额
                          , 1  # 总揽到店次数
                          , 0  # 总揽新增会员数
                          , 0  # 总揽订单数
                          , 0  # 总揽退单数
                          , 0  # 总揽销售总额
                          , 0  # M216C237C0458总仓库存
                          , 0  # M216C237C0464总仓库存
                          , 0  # M116E248B0158总仓库存
                          , 0  # M116E248B0164总仓库存
                          , 0  # M316J232B01106总仓库存
                          , 0  # M316J232B0176总仓库存
                          , 0  # ZH02B215190T796242总仓库存
                          , 0  # 验证值
                          , 0  # M216C237C0458门店库存
                          , 0  # M216C237C0464门店库存
                          , 0  # M116E248B0158门店库存
                          , 0  # M116E248B0164门店库存
                          , 0  # M316J232B01106门店库存
                          , 0  # M316J232B0176门店库存
                          , 0  # ZH02B215190T796242门店库存
                          , 1  # 门店到店次数期待增加值
                          , 0  # 门店新增会员数期待增加值
                          , 0  # 门店订单数期待增加值
                          , 0  # 门店退单数期待增加值
                          , 0  # 门店销售总额期待增加值
                          , 0  # 门店平台销售总额期待增加值
                          )

        # 验证数据
        self._data_assertion()


    def test_2_zero_pay_order(self):
        """
        余额扫描确认0元单
        选码黑色58 深蓝色58
        YS5130N748574 预售商品
        :return:
        """
        logging.debug("test_2_zero_pay_order")
        market_service.set_pre_sale_product('6430', '1')
        param = {'record_id': globals()['shopping_order_id'], 'receive_name': self._customer.consignee, 'receive_phone': self._customer.phone, 'beizhu': '',
                 'com_out_num': '0', 'receive_sheng': self._customer.province, 'receive_shi': self._customer.city, 'receive_diqu': self._customer.area, 'receive_address': self._customer.address, 'repo_out_num': '1',
                 'referral_phone':self._customer_re.phone, 'goods_info': [{"danjia": "0.01", "sku_num": 1, "sku_name": "腰背夹", "price": "0.01", "sku_id": "4878", "tiaoma": "M216C237C0458", "kuanhao": "M216C237", "sku_detail": "深蓝色 58",
                 "img": "https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg", "repo_out_num": 1, "com_out_num":0},
                                                      {"danjia": "0.01", "sku_num": 1, "sku_name": "包臀内裤", "price": "0.01", "sku_id": "4701", "tiaoma": "M116E248B0158", "kuanhao": "M116E248", "sku_detail": "黑色 58",
                 "img": "https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg", "repo_out_num": 1, "com_out_num":0}]
                 }
        # 0,1表示发货与否，1表示发货，0表示不发货
        id = 1
        globals()['order_id'] = market_service.choose_size(param,id)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        self._test_data_re.update_post_verify_data()
        # 验证值
        self.expectedData(1000  # 会员消费额
                          , 0  # 会员积分
                          , 2  # 会员卡等级
                          , 0  # 会员余额
                          , 0  # 总揽到店次数
                          , 0  # 总揽新增会员数
                          , 1  # 总揽订单数
                          , 0  # 总揽退单数
                          , 0  # 总揽销售总额
                          , 0  # M216C237C0458总仓库存
                          , 0  # M216C237C0464总仓库存
                          , 0  # M116E248B0158总仓库存
                          , 0  # M116E248B0164总仓库存
                          , 0  # M316J232B01106总仓库存
                          , 0  # M316J232B0176总仓库存
                          , 0  # ZH02B215190T796242总仓库存
                          , 0.1  # 验证值
                          , -1  # M216C237C0458门店库存
                          , 0  # M216C237C0464门店库存
                          , -1  # M116E248B0158门店库存
                          , 0  # M116E248B0164门店库存
                          , 0  # M316J232B01106门店库存
                          , 0  # M316J232B0176门店库存
                          , 0  # ZH02B215190T796242门店库存
                          , 0  # 门店到店次数期待增加值
                          , 0  # 门店新增会员数期待增加值
                          , 1  # 门店订单数期待增加值
                          , 0  # 门店退单数期待增加值
                          , 1000  # 门店销售总额期待增加值
                          , 1000 # 门店平台销售总额期待增加值
                          )
        # 封装验证值
        self._customer_re.expectedData = CustomerVerifyData.expected_data(0, 0, 0, 0)  # 更新转介绍会员验证值
        # 验证数据
        self._data_assertion()
        self._data_assertion_re()

    def test_3_changer_pieces(self):
        """
        换货预售商品
        YS5130N748574
        深蓝色58 黑色58 换 深蓝色64 黑色64
        :return:
        """
        logging.debug("test_3_changer_10pieces")
        if globals()['order_id'] is not None:
            exchange_order_id = globals()['order_id'] + "_1"
            params = {'sub_order_id': exchange_order_id, 'goods_num': '1', 'goods_total_price': '0.00', 'reason': '30天无理由换货', 'remarks': '测试', 'type': '2', 'goods_type': '3',
                      'goods_list': '[{"num":"1","sku_id":"6430","sku_name":"周自动化测试勿动","sku_detail":"","tiaoma":"YS5130N748574","kuanhao":"","danjia":"1000.00","img":"https://lchapp.oss-cn-beijing.aliyuncs.com/2019112610521983674.jpg"}]',
                      'sub_goods_list': '{"YS5130N748574":[{"num":1,"sku_id":"4702","sku_name":"包臀内裤","sku_detail":"黑色 64","tiaoma":"M116E248B0164","kuanhao":"M116E248","danjia":"0.01","img":"https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg","repo_num":488},{"num":1,"sku_id":"4879","sku_name":"腰背夹","sku_detail":"深蓝色 64","tiaoma":"M216C237C0464","kuanhao":"M216C237","danjia":"0.01","img":"https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg","repo_num":338}]}'
                      }
            market_service.exchange_order(params)
            # 更新充值后的验证数据
            self._test_data.update_post_verify_data()
            self._test_data_re.update_post_verify_data()
            # 验证值
            self.expectedData(0 # 会员消费额
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
                              , 1 # M216C237C0458门店库存
                              , -1 # M216C237C0464门店库存
                              , 1 # M116E248B0158门店库存
                              , -1 # M116E248B0164门店库存
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
            # 封装验证值
            self._customer_re.expectedData = CustomerVerifyData.expected_data(0, 0, 0, 0)  # 更新转介绍会员验证值
            # 验证数据
            self._data_assertion()
            self._data_assertion_re()

    def test_4_return_pieces(self):
        """
        退货预售商品
        YS5130N748574
        :return:
        """
        logging.debug("test_4_return_10pieces")
        shopping_order_id = globals()['order_id']
        member_number = self._customer.member_number
        exchangeOrderId = market_service.find_order_id(shopping_order_id, member_number)
        return_order_id = exchangeOrderId + "_0"
        return_param = {'main_order_id': exchangeOrderId, 'return_price': '0.00', 'reason': '15天无理由退货', 'remarks': '测试', 'afterSales_info[0][order_id]':  return_order_id, 'afterSales_info[0][danjia]': '1000.00',
                        'afterSales_info[0][sku_name]': '周自动化测试勿动', 'afterSales_info[0][sku_detail]': '', 'afterSales_info[0][tiaoma]':  'YS5130N748574', 'afterSales_info[0][kuanhao]': '', 'afterSales_info[0][sku_id]': '6430',
                        'afterSales_info[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019112610521983674.jpg', 'afterSales_info[0][aftersale_num]': '1', 'afterSales_info[0][aftersale_money]': '0.00', 'afterSales_info[0][goods_type]': '2'}
        market_service.return_order(return_param)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        self._test_data_re.update_post_verify_data()
        # 验证值
        self.expectedData(-1000 # 会员消费额
                          , 0 # 会员积分
                          , 2 # 会员卡等级
                          , 0 # 会员余额
                          , 0 # 总揽到店次数
                          , 0 # 总揽新增会员数
                          , 0 # 总揽订单数
                          , 1 # 总揽退单数
                          , -1000.00 # 总揽销售总额
                          , 0 # M216C237C0458总仓库存
                          , 0 # M216C237C0464总仓库存
                          , 0 # M116E248B0158总仓库存
                          , 0 # M116E248B0164总仓库存
                          , 0 # M316J232B01106总仓库存
                          , 0 # M316J232B0176总仓库存
                          , 0 # ZH02B215190T796242总仓库存
                          , -0.1 # 验证值
                          , 0 # M216C237C0458门店库存
                          , 1 # M216C237C0464门店库存
                          , 0 # M116E248B0158门店库存
                          , 1 # M116E248B0164门店库存
                          , 0 # M316J232B01106门店库存
                          , 0 # M316J232B0176门店库存
                          , 0 # ZH02B215190T796242门店库存
                          , 0 # 门店到店次数期待增加值
                          , 0 # 门店新增会员数期待增加值
                          , 0 # 门店订单数期待增加值
                          , 1 # 门店退单数期待增加值
                          , -1000.00 # 门店销售总额期待增加值
                          , -1000.00 # 门店平台销售总额期待增加值
                          )
        # 封装验证值
        self._customer_re.expectedData = CustomerVerifyData.expected_data(0, 0, 0, 0)  # 更新转介绍会员验证值
        # 验证数据
        self._data_assertion()
        self._data_assertion_re()

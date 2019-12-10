
from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service

class TestChargePreSaleGoods(BaseCase):
    """
    预售商品余额支付（一件预售商品 公司发货）
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

    def test_1_ChargePreSaleGoods_order(self):
        """
       预售商品下单(两件子商品，公司发货)
        :return:
        """
        logging.debug("test_1_rechargesskuds_order")
        params={
                          'member_id': self._customer.member_number, 'member_name': self._customer.name,
                          'member_phone': self._customer.phone,
                          'plateform_id': self._customer.platform.platform_id,
                          'special_employee_id': self._customer.employee.employee_id,
                          'pay_type': 'recharge',
                          'goods_info':{'sku_num':'1','sku_name':'何明锐预售','sku_id':'6434','tiaoma':'YS6789N838655','price':'1234.00','kuanhao':'','img':'https://lchapp.oss-cn-beijing.aliyuncs.com/2019112758736210149.png','sku_detail':''}
        }
        #设置商品不发售
        product_id =6434
        market_service.set_pre_sale_product(product_id,2)
        globals()['shopping_order_id']= market_service.presell_pos(params)
        #设置商品发售
        market_service.set_pre_sale_product(product_id,1)
        # 选择商品转订单
        param = {'record_id': globals()['shopping_order_id'], 'receive_name': self._customer.consignee,
                 'receive_phone': self._customer.phone, 'beizhu': '',
                 'com_out_num': '1', 'receive_sheng': self._customer.province, 'receive_shi': self._customer.city,
                 'receive_diqu': self._customer.area, 'receive_address': self._customer.address, 'repo_out_num': '0',
                 'referral_phone': '', 'goods_info': [
                {"danjia": "0.01", "sku_num": 1, "sku_name": "腰背夹", "price": "0.01", "sku_id": "4878",
                 "tiaoma": "M216C237C0458", "kuanhao": "M216C237", "sku_detail": "深蓝色 58",
                 "img": "https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg", "repo_out_num": 0,
                 "com_out_num": 1},
                {"danjia": "0.01", "sku_num": 1, "sku_name": "包臀内裤", "price": "0.01", "sku_id": "4701",
                 "tiaoma": "M116E248B0158", "kuanhao": "M116E248", "sku_detail": "黑色 58",
                 "img": "https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg", "repo_out_num": 0,
                 "com_out_num": 1}]
                 }
        globals()['order_shopping_id'] =market_service.choose_size(param)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 封装验证值
        self.expectedData(1234  # 会员消费额
                          , 0  # 会员积分
                          , 2  # 会员卡等级
                          , -1234  # 会员余额
                          , 1  # 总揽到店次数
                          , 0  # 总揽新增会员数
                          , 1  # 总揽订单数
                          , 0  # 总揽退单数
                          , 1234  # 总揽销售总额
                          , -1  # M216C237C0458总仓库存
                          , 0  # M216C237C0464总仓库存
                          , -1  # M116E248B0158总仓库存
                          , 0  # M116E248B0164总仓库存
                          , 0  # M316J232B01106总仓库存
                          , 0  # M316J232B0176总仓库存
                          , 0  # ZH02B215190T796242总仓库存
                          , 0.12  # 验证值
                          , 0  # M216C237C0458门店库存
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
                          , 1234  # 门店销售总额期待增加值
                          , 1234 # 门店平台销售总额期待增加值
                          )
        # 验证数据
        self._data_assertion()

    def test_2_ChargePreSaleGoods_Exchange_part(self):
        """
       预售商品换货
        :return:
        """
        pass
        logging.debug("test_2_ChargePreSaleGoods_Exchange_part")
        if globals()['order_shopping_id'] is not None:
            exchange_order_id = globals()['order_shopping_id'] + "_1"
            recharge_param={
                'sub_order_id': exchange_order_id, 'goods_num': '1', 'goods_total_price': '0.00',
                'reason': '30天无理由换货','remarks': '哈哈', 'type': '2','goods_type':'3',
                'goods_list': '[{"num":"1","sku_id":"6434","sku_name":"何明锐预售","sku_detail":"","tiaoma":"YS6789N838655","kuanhao":"","danjia":"1234.00","img":"https://lchapp.oss-cn-beijing.aliyuncs.com/2019112758736210149.png"}]',
                'sub_goods_list': '{"YS6789N838655":[{"num":1,"sku_id":"4702","sku_name":"包臀内裤","sku_detail":"黑色 64","tiaoma":"M116E248B0164","kuanhao":"M116E248","danjia":"1.00","img":"https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg","repo_num":147},{"num":1,"sku_id":"4879","sku_name":"腰背夹","sku_detail":"深蓝色 64","tiaoma":"M216C237C0464","kuanhao":"M216C237","danjia":"1.00","img":"https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg","repo_num":196}]}'
            }
            market_service.exchange_order(recharge_param)
            # 更新充值后的验证数据
            self._test_data.update_post_verify_data()
            # 封装验证值
            self.expectedData(0 # 会员消费额
                              , 0  # 会员积分
                              , 2  # 会员卡等级
                              , 0  # 会员余额
                              , 0  # 总揽到店次数
                              , 0  # 总揽新增会员数
                              , 0  # 总揽订单数
                              , 1  # 总揽退单数
                              , 0  # 总揽销售总额
                              , 0  # M216C237C0458总仓库存
                              , 0  # M216C237C0464总仓库存
                              , 0  # M116E248B0158总仓库存
                              , 0  # M116E248B0164总仓库存
                              , 0  # M316J232B01106总仓库存
                              , 0  # M316J232B0176总仓库存
                              , 0  # ZH02B215190T796242总仓库存
                              , 0  # 验证值
                              , 1  # M216C237C0458门店库存
                              , -1 # M216C237C0464门店库存
                              , 1  # M116E248B0158门店库存
                              , -1  # M116E248B0164门店库存
                              , 0  # M316J232B01106门店库存
                              , 0  # M316J232B0176门店库存
                              , 0  # ZH02B215190T796242门店库存
                              , 0  # 门店到店次数期待增加值
                              , 0  # 门店新增会员数期待增加值
                              , 1  # 门店订单数期待增加值
                              , 0  # 门店退单数期待增加值
                              , 0  # 门店销售总额期待增加值
                              , 0  # 门店平台销售总额期待增加值
                              )
            # 验证数据
            self._data_assertion()





    def test_3_ChargePreSaleGoods_Exchange_other(self):
                """
                预售商品换的两件商品退货
                :return:
                """
                logging.debug("test_3_ChargeSimpleAndComplex_Exchange_other")
                if globals()['order_shopping_id'] is not None:
                    exchange_order = market_service.find_order_id(globals()['order_shopping_id'],
                                                                  self._customer.member_number)

                    return_order_c = exchange_order + "_0"
                    recharge_param = {
                        'main_order_id': exchange_order, 'return_price': '0.00', 'reason': '15天无理由退货',
                        'remarks': '不要了', 'afterSales_info[0][order_id]': return_order_c,
                        'afterSales_info[0][danjia]': '1234.00',
                        'afterSales_info[0][sku_name]': '何明锐预售', 'afterSales_info[0][sku_detail]': '',
                        'afterSales_info[0][tiaoma]': 'YS6789N838655', 'afterSales_info[0][kuanhao]': '',
                        'afterSales_info[0][sku_id]': '6434',
                        'afterSales_info[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019112758736210149.png',
                        'afterSales_info[0][aftersale_num]': '1',
                        'afterSales_info[0][aftersale_money]': '0.00', 'afterSales_info[0][goods_type]': '2',

                    }
                    market_service.return_order(recharge_param)
                    # 更新充值后的验证数据
                    self._test_data.update_post_verify_data()
                    # 封装验证值
                    self.expectedData(-1234  # 会员消费额
                                      , 0  # 会员积分
                                      , 2  # 会员卡等级
                                      , 1234 # 会员余额
                                      , 0  # 总揽到店次数
                                      , 0  # 总揽新增会员数
                                      , 0  # 总揽订单数
                                      , 1  # 总揽退单数
                                      , 0  # 总揽销售总额
                                      , 0  # M216C237C0458总仓库存
                                      , 0  # M216C237C0464总仓库存
                                      , 0  # M116E248B0158总仓库存
                                      , 0  # M116E248B0164总仓库存
                                      , 0  # M316J232B01106总仓库存
                                      , 0  # M316J232B0176总仓库存
                                      , 0  # ZH02B215190T796242总仓库存
                                      , -0.12  # 验证值
                                      , 0  # M216C237C0458门店库存
                                      , 1  # M216C237C0464门店库存
                                      , 0  # M116E248B0158门店库存
                                      , 1  # M116E248B0164门店库存
                                      , 0  # M316J232B01106门店库存
                                      , 0  # M316J232B0176门店库存
                                      , 0  # ZH02B215190T796242门店库存
                                      , 0  # 门店到店次数期待增加值
                                      , 0  # 门店新增会员数期待增加值
                                      , 0  # 门店订单数期待增加值
                                      , 1  # 门店退单数期待增加值
                                      , -1234  # 门店销售总额期待增加值
                                      , -1234  # 门店平台销售总额期待增加值
                                      )
                    # 验证数据
                    self._data_assertion()


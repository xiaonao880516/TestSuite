
from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service




class TestPosNoDiscountNoScoreSimpleGoods(BaseCase):
    """
   不折扣不积分与普通商品pos混合下单
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 设置特定商品不折扣不积分
        product =["M316J232B0198", "M316J232B0190", "M316J232B0182", "M316J232B0176", "M316J232B01106"]
        market_service.set_no_discount_no_score_product(product)

        # 会员充值40000
        cls._customer.recharge(40000)


    def setUp(self):
        super().setUp()
        # 更新充值前的验证数据
        self._test_data.update_pre_verify_data()

    def tearDown(self):
        super().tearDown()

    def test_1_NoDiscountNoScoreSimple_order(self):
        """
      不折扣不积分与普通商品pos混合下单
        :return:
        """
        logging.debug("test_1_NoDiscountNoScoreSimple_order")
        params={
            'price': '18120.00', 'discount_money': '512.00', 'real_pay': '17608.00',
            'receive_name': self._customer.consignee, 'receive_phone': self._customer.phone,
            'receive_sheng': self._customer.province, 'receive_shi': self._customer.city,
            'receive_diqu': self._customer.area, 'receive_address': self._customer.address,
            'member_id': self._customer.member_number, 'member_name': self._customer.name,
            'member_phone': self._customer.phone,
            'plateform_id': self._customer.platform.platform_id,
            'special_employee_id': self._customer.employee.employee_id, 'discount_rate': '0.96',
            'goods_list[0][danjia]': '2000.00', 'goods_list[0][sku_num]': '3',
            'goods_list[0][sku_name]': '腰背夹',
            'goods_list[0][price]': '6000.00', 'goods_list[0][real_pay_price]': '5760.00',
            'goods_list[0][discount_price]': '240.00',
            'goods_list[0][sku_id]': '4878', 'goods_list[0][tiaoma]': 'M216C237C0458',
            'goods_list[0][kuanhao]': 'M216C237',
            'goods_list[0][sku_detail]': '深蓝色 58',
            'goods_list[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
            'goods_list[0][repo_out_num]': '3', 'goods_list[0][com_out_num]': '0',
            'goods_list[0][no_discount]': '0', 'goods_list[0][no_score]': '0',
            'goods_list[0][is_active]': '0', 'goods_list[0][type]': '2',
            'goods_list[0][zh_num]': '1', 'goods_list[0][zh_repo_out_num]': '1',
            'goods_list[0][zh_com_out_num]': '0', 'goods_list[0][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[0][zh_mark]': '1', 'goods_list[0][zh_no_discount]': '0',
            'goods_list[0][zh_no_score]': '0',
            'goods_list[1][danjia]': '400.00',
            'goods_list[1][sku_num]': '1',
            'goods_list[1][sku_name]': '包臀内裤', 'goods_list[1][price]': '400.00',
            'goods_list[1][real_pay_price]': '384.00', 'goods_list[1][discount_price]': '16.00',
            'goods_list[1][sku_id]': '4701',
            'goods_list[1][tiaoma]': 'M116E248B0158', 'goods_list[1][kuanhao]': 'M116E248',
            'goods_list[1][sku_detail]': '黑色 58',
            'goods_list[1][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
            'goods_list[1][repo_out_num]': '1',
            'goods_list[1][com_out_num]': '0', 'goods_list[1][no_discount]': '0',
            'goods_list[1][no_score]': '0', 'goods_list[1][is_active]': '0', 'goods_list[1][type]': '2',
            'goods_list[1][zh_num]': '1', 'goods_list[1][zh_repo_out_num]': '1',
            'goods_list[1][zh_com_out_num]': '0', 'goods_list[1][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[1][zh_mark]': '1', 'goods_list[1][zh_no_discount]': '0',
            'goods_list[1][zh_no_score]': '0', 'goods_list[2][danjia]': '2000.00',
            'goods_list[2][sku_num]': '3',
            'goods_list[2][sku_name]': '腰背夹', 'goods_list[2][price]': '6000.00',
            'goods_list[2][real_pay_price]': '5760.00', 'goods_list[2][discount_price]': '240.00',
            'goods_list[2][sku_id]': '4878',
            'goods_list[2][tiaoma]': 'M216C237C0458', 'goods_list[2][kuanhao]': 'M216C237',
            'goods_list[2][sku_detail]': '深蓝色 58',
            'goods_list[2][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
            'goods_list[2][repo_out_num]': '3',
            'goods_list[2][com_out_num]': '0', 'goods_list[2][no_discount]': '0',
            'goods_list[2][no_score]': '0', 'goods_list[2][is_active]': '0', 'goods_list[2][type]': '2',
            'goods_list[2][zh_num]': '1', 'goods_list[2][zh_repo_out_num]': '1',
            'goods_list[2][zh_com_out_num]': '0', 'goods_list[2][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[2][zh_mark]': '2', 'goods_list[2][zh_no_discount]': '0',
            'goods_list[2][zh_no_score]': '0', 'goods_list[3][danjia]': '400.00',
            'goods_list[3][sku_num]': '1',
            'goods_list[3][sku_name]': '包臀内裤', 'goods_list[3][price]': '400.00',
            'goods_list[3][real_pay_price]': '384.00', 'goods_list[3][discount_price]': '16.00',
            'goods_list[3][sku_id]': '4701',
            'goods_list[3][tiaoma]': 'M116E248B0158', 'goods_list[3][kuanhao]': 'M116E248',
            'goods_list[3][sku_detail]': '黑色 58',
            'goods_list[3][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
            'goods_list[3][repo_out_num]': '1',
            'goods_list[3][com_out_num]': '0', 'goods_list[3][no_discount]': '0',
            'goods_list[3][no_score]': '0', 'goods_list[3][is_active]': '0', 'goods_list[3][type]': '2',
            'goods_list[3][zh_num]': '1', 'goods_list[3][zh_repo_out_num]': '1',
            'goods_list[3][zh_com_out_num]': '0', 'goods_list[3][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[3][zh_mark]': '2', 'goods_list[3][zh_no_discount]': '0',
            'goods_list[3][zh_no_score]': '0', 'goods_list[4][danjia]': '2660',
            'goods_list[4][sku_num]': '2',
            'goods_list[4][sku_name]': '男士塑身背心', 'goods_list[4][price]': '5320.00',
            'goods_list[4][real_pay_price]': '5320.00', 'goods_list[4][discount_price]': '0.00',
            'goods_list[4][sku_id]': '4996',
            'goods_list[4][tiaoma]': 'M316J232B0198', 'goods_list[4][kuanhao]': 'M316J232',
            'goods_list[4][sku_detail]': '黑色 98',
            'goods_list[4][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010526413875910.jpg',
            'goods_list[4][repo_out_num]': '2',
            'goods_list[4][com_out_num]': '0', 'goods_list[4][no_discount]': '1',
            'goods_list[4][no_score]': '1', 'goods_list[4][is_active]': '0', 'goods_list[4][type]': '1',
            'pay_type': 'pos','coupon_discount_amount':'0.00'


        }
        globals()['shopping_order_id']= market_service.pos_order(params)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 封装验证值
        self.expectedData(17608  # 会员消费额
                          , 12288  # 会员积分
                          , 2  # 会员卡等级
                          , 0  # 会员余额
                          , 0  # 总揽到店次数
                          , 0  # 总揽新增会员数
                          , 1  # 总揽订单数
                          , 0  # 总揽退单数
                          , 17608  # 总揽销售总额
                          , 0  # M216C237C0458总仓库存
                          , 0  # M216C237C0464总仓库存
                          , 0  # M116E248B0158总仓库存
                          , 0  # M116E248B0164总仓库存
                          , 0  # M316J232B01106总仓库存
                          , 0  # M316J232B0176总仓库存
                          , -2  # ZH02B215190T796242总仓库存
                          , 1.76  # 验证值
                          , -6  # M216C237C0458门店库存
                          , 0  # M216C237C0464门店库存
                          , -2  # M116E248B0158门店库存
                          , 0  # M116E248B0164门店库存
                          , 0  # M316J232B01198门店库存
                          , 0  # M316J232B0176门店库存
                          , 0  # ZH02B215190T796242门店库存
                          , 1  # 门店到店次数期待增加值
                          , 0  # 门店新增会员数期待增加值
                          , 1  # 门店订单数期待增加值
                          , 0  # 门店退单数期待增加值
                          , 17608  # 门店销售总额期待增加值
                          , 17608  # 门店平台销售总额期待增加值
                          )
        # 验证数据
        self._data_assertion()

    def test_2_NoDiscountNoScoreSimple_ReturnPart(self):
        """
       不折扣不积分商品退货
        :return:
        """
        logging.debug("test_2_NoDiscountNoScoreSimple_ReturnPart")
        if globals()['shopping_order_id'] is not None:
            return_order_id = globals()['shopping_order_id'] + "_0"
            recharge_param = {
                'main_order_id': globals()['shopping_order_id'],
                'return_price': '5320.00', 'reason': '拍错/不想要',
                'remarks': '第三方', 'afterSales_info[0][order_id]': return_order_id,
                'afterSales_info[0][danjia]': '2660.00',
                'afterSales_info[0][sku_name]': '男士塑身背心',
                'afterSales_info[0][sku_detail]': '黑色 98',
                'afterSales_info[0][tiaoma]': 'M316J232B0198',
                'afterSales_info[0][kuanhao]': 'M316J232',
                'afterSales_info[0][sku_id]': '4996',
                'afterSales_info[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019080310765489321.jpg',
                'afterSales_info[0][aftersale_num]': '2',
                'afterSales_info[0][aftersale_money]': '5320.00',
                'afterSales_info[0][goods_type]': '1'

            }
            market_service.return_order(recharge_param)
            # 更新充值后的验证数据
            self._test_data.update_post_verify_data()
            # 封装验证值
            self.expectedData(-5320  # 会员消费额
                              , 0  # 会员积分
                              , 2  # 会员卡等级
                              , 0  # 会员余额
                              , 0  # 总揽到店次数
                              , 0  # 总揽新增会员数
                              , 0  # 总揽订单数
                              , 1  # 总揽退单数
                              , -5320  # 总揽销售总额
                              , 0  # M216C237C0458总仓库存
                              , 0  # M216C237C0464总仓库存
                              , 0  # M116E248B0158总仓库存
                              , 0  # M116E248B0164总仓库存
                              , 0  # M316J232B01106总仓库存
                              , 0  # M316J232B0176总仓库存
                              , 0  # ZH02B215190T796242总仓库存
                              , -0.53  # 验证值
                              , 0  # M216C237C0458门店库存
                              , 0  # M216C237C0464门店库存
                              , 0  # M116E248B0158门店库存
                              , 0  # M116E248B0164门店库存
                              , 0  # M316J232B01106门店库存
                              , 0  # M316J232B0176门店库存
                              , 0  # ZH02B215190T796242门店库存
                              , 0  # 门店到店次数期待增加值
                              , 0  # 门店新增会员数期待增加值
                              , 0  # 门店订单数期待增加值
                              , 0  # 门店退单数期待增加值
                              , -5320  # 门店销售总额期待增加值
                              ,-5320  # 门店平台销售总额期待增加值
                              )
            # 验证数据
            self._data_assertion()





    def test_3_NoDiscountNoScoreSimple_ReturnOther(self):
                """
               不折扣不积分与普通商品pos混合下单，剩余商品退货
                :return:
                """
                logging.debug("test_3_NoDiscountNoScoreSimple_ReturnOther")
                if globals()['shopping_order_id'] is not None:
                    return_order_id = globals()['shopping_order_id'] + "_2"
                    return_order_id_b = globals()['shopping_order_id'] + "_1"

                    return_other_param = {
                        'main_order_id': globals()['shopping_order_id'], 'return_price': '12288.00',
                        'reason': '15天无理由退货', 'remarks': '撒旦发', 'afterSales_info[0][order_id]': return_order_id,
                        'afterSales_info[0][danjia]': '6400.00',
                        'afterSales_info[0][sku_name]': '孟伟组合商品', 'afterSales_info[0][sku_detail]': '2件商品',
                        'afterSales_info[0][tiaoma]': 'ZH02B215190T796242', 'afterSales_info[0][kuanhao]': '',
                        'afterSales_info[0][sku_id]': '5955',
                        'afterSales_info[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019080310765489321.jpg',
                        'afterSales_info[0][aftersale_num]': '1', 'afterSales_info[0][aftersale_money]': '6144.00',
                        'afterSales_info[0][goods_type]': '2',
                        'afterSales_info[1][order_id]': return_order_id_b, 'afterSales_info[1][danjia]': '6400.000',
                        'afterSales_info[1][sku_name]': '孟伟组合商品', 'afterSales_info[1][sku_detail]': '2件商品',
                        'afterSales_info[1][tiaoma]': 'ZH02B215190T796242', 'afterSales_info[1][kuanhao]': '',
                        'afterSales_info[1][sku_id]': '5955',
                        'afterSales_info[1][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019080310765489321.jpg',
                        'afterSales_info[1][aftersale_num]': '1', 'afterSales_info[1][aftersale_money]': '6144.00',
                        'afterSales_info[1][goods_type]': '2'
                    }
                    market_service.return_order(return_other_param)
                    # 更新充值后的验证数据
                    self._test_data.update_post_verify_data()
                    # 封装验证值
                    self.expectedData(-12288  # 会员消费额
                                      ,-12288 # 会员积分
                                      , 2  # 会员卡等级
                                      , 0  # 会员余额
                                      , 0  # 总揽到店次数
                                      , 0  # 总揽新增会员数
                                      , 0  # 总揽订单数
                                      , 1  # 总揽退单数
                                      , -12288  # 总揽销售总额
                                      , 0  # M216C237C0458总仓库存
                                      , 0  # M216C237C0464总仓库存
                                      , 0  # M116E248B0158总仓库存
                                      , 0  # M116E248B0164总仓库存
                                      , 0  # M316J232B01106总仓库存
                                      , 0  # M316J232B0176总仓库存
                                      , 2  # ZH02B215190T796242总仓库存
                                      , -1.23  # 验证值
                                      , 6  # M216C237C0458门店库存
                                      , 0  # M216C237C0464门店库存
                                      , 2  # M116E248B0158门店库存
                                      , 0  # M116E248B0164门店库存
                                      , 0  # M316J232B01106门店库存
                                      , 0  # M316J232B0176门店库存
                                      , 0  # ZH02B215190T796242门店库存
                                      , 0  # 门店到店次数期待增加值
                                      , 0  # 门店新增会员数期待增加值
                                      , 0  # 门店订单数期待增加值
                                      , 0  # 门店退单数期待增加值
                                      , -12288  # 门店销售总额期待增加值
                                      , -12288  # 门店平台销售总额期待增加值
                                      )
                    # 验证数据
                    self._data_assertion()



















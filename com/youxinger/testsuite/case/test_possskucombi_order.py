
from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service

class TestPosCombinationAndCommonGoods(BaseCase):
    """
   组合商品与普通商品
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

    def test_1_pos_Combination_and_common_order(self):
        """
       组合商品与普通商品pos下单（两件组合商品和一件普通商品)
        :return:
        """
        logging.debug("test_1_pos_Combination_and_common_order")
        params={
            'price': '19560.00', 'discount_money': '782.40', 'real_pay': '18777.60',
            'receive_name': self._customer.consignee, 'receive_phone': self._customer.phone,
            'receive_sheng': self._customer.province, 'receive_shi': self._customer.city,
            'receive_diqu': self._customer.area, 'receive_address': self._customer.address,
            'member_id': self._customer.member_number, 'member_name': self._customer.name,
            'member_phone': self._customer.phone,
            'plateform_id': self._customer.platform.platform_id,
            'special_employee_id': self._customer.employee.employee_id, 'discount_rate': '0.96',
            'goods_list[0][danjia]': '3380', 'goods_list[0][sku_num]': '2',
            'goods_list[0][sku_name]': '腰背夹',
            'goods_list[0][price]': '6760.00', 'goods_list[0][real_pay_price]': '6489.60',
            'goods_list[0][discount_price]': '270.40',
            'goods_list[0][sku_id]': '4878', 'goods_list[0][tiaoma]': 'M216C237C0458',
            'goods_list[0][kuanhao]': 'M216C237',
            'goods_list[0][sku_detail]': '深蓝色 58',
            'goods_list[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
            'goods_list[0][repo_out_num]': '0', 'goods_list[0][com_out_num]': '2',
            'goods_list[0][no_discount]': '0', 'goods_list[0][no_score]': '0',
            'goods_list[0][is_active]': '0', 'goods_list[0][type]': '1',
            'goods_list[1][danjia]': '2000.00',
            'goods_list[1][sku_num]': '3',
            'goods_list[1][sku_name]': '腰背夹', 'goods_list[1][price]': '6000.00',
            'goods_list[1][real_pay_price]': '5760.00', 'goods_list[1][discount_price]': '240.00',
            'goods_list[1][sku_id]': '4878',
            'goods_list[1][tiaoma]': 'M216C237C0458', 'goods_list[1][kuanhao]': 'M216C237',
            'goods_list[1][sku_detail]': '深蓝色 58',
            'goods_list[1][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
            'goods_list[1][repo_out_num]': '0',
            'goods_list[1][com_out_num]': '3', 'goods_list[1][no_discount]': '0',
            'goods_list[1][no_score]': '0', 'goods_list[1][is_active]': '0', 'goods_list[1][type]': '2',
            'goods_list[1][zh_num]': '1', 'goods_list[1][zh_repo_out_num]': '0',
            'goods_list[1][zh_com_out_num]': '1', 'goods_list[1][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[1][zh_mark]': '2', 'goods_list[1][zh_no_discount]': '0',
            'goods_list[1][zh_no_score]': '0', 'goods_list[2][danjia]': '400.00',
            'goods_list[2][sku_num]': '1',
            'goods_list[2][sku_name]': '包臀内裤', 'goods_list[2][price]': '400.00',
            'goods_list[2][real_pay_price]': '384.00', 'goods_list[2][discount_price]': '16.00',
            'goods_list[2][sku_id]': '4701',
            'goods_list[2][tiaoma]': 'M116E248B0158', 'goods_list[2][kuanhao]': 'M116E248',
            'goods_list[2][sku_detail]': '黑色 58',
            'goods_list[2][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
            'goods_list[2][repo_out_num]': '0',
            'goods_list[2][com_out_num]': '1', 'goods_list[2][no_discount]': '0',
            'goods_list[2][no_score]': '0', 'goods_list[2][is_active]': '0', 'goods_list[2][type]': '2',
            'goods_list[2][zh_num]': '1', 'goods_list[2][zh_repo_out_num]': '0',
            'goods_list[2][zh_com_out_num]': '1', 'goods_list[2][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[2][zh_mark]': '2', 'goods_list[2][zh_no_discount]': '0',
            'goods_list[2][zh_no_score]': '0', 'goods_list[3][danjia]': '2000.00',
            'goods_list[3][sku_num]': '3',
            'goods_list[3][sku_name]': '腰背夹', 'goods_list[3][price]': '6000.00',
            'goods_list[3][real_pay_price]': '5760.00', 'goods_list[3][discount_price]': '240.00',
            'goods_list[3][sku_id]': '4878',
            'goods_list[3][tiaoma]': 'M216C237C0458', 'goods_list[3][kuanhao]': 'M216C237',
            'goods_list[3][sku_detail]': '深蓝色 58',
            'goods_list[3][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
            'goods_list[3][repo_out_num]': '0',
            'goods_list[3][com_out_num]': '3', 'goods_list[3][no_discount]': '0',
            'goods_list[3][no_score]': '0', 'goods_list[3][is_active]': '0', 'goods_list[3][type]': '2',
            'goods_list[3][zh_num]': '1', 'goods_list[3][zh_repo_out_num]': '0',
            'goods_list[3][zh_com_out_num]': '1', 'goods_list[3][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[3][zh_mark]': '3', 'goods_list[3][zh_no_discount]': '0',
            'goods_list[3][zh_no_score]': '0', 'goods_list[4][danjia]': '400.00',
            'goods_list[4][sku_num]': '1',
            'goods_list[4][sku_name]': '包臀内裤', 'goods_list[4][price]': '400.00',
            'goods_list[4][real_pay_price]': '384.00', 'goods_list[4][discount_price]': '16.00',
            'goods_list[4][sku_id]': '4701',
            'goods_list[4][tiaoma]': 'M116E248B0158', 'goods_list[4][kuanhao]': 'M116E248',
            'goods_list[4][sku_detail]': '黑色 58',
            'goods_list[4][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
            'goods_list[4][repo_out_num]': '0',
            'goods_list[4][com_out_num]': '1', 'goods_list[4][no_discount]': '0',
            'goods_list[4][no_score]': '0', 'goods_list[4][is_active]': '0', 'goods_list[4][type]': '2',
            'goods_list[4][zh_num]': '1', 'goods_list[4][zh_repo_out_num]': '0',
            'goods_list[4][zh_com_out_num]': '1', 'goods_list[4][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[4][zh_mark]': '3', 'goods_list[4][zh_no_discount]': '0',
            'goods_list[4][zh_no_score]': '0',
            'pay_type': 'pos'

        }
        globals()['shopping_order_id']= market_service.pos_order(params)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 封装验证值
        self.expectedData(18778  # 会员消费额
                          , 18778  # 会员积分
                          , 2  # 会员卡等级
                          , 0  # 会员余额
                          , 1  # 总揽到店次数
                          , 0  # 总揽新增会员数
                          , 1  # 总揽订单数
                          , 0  # 总揽退单数
                          , 18778  # 总揽销售总额
                          , -8  # M216C237C0458总仓库存
                          , 0  # M216C237C0464总仓库存
                          , -2  # M116E248B0158总仓库存
                          , 0  # M116E248B0164总仓库存
                          , 0  # M316J232B01106总仓库存
                          , 0  # M316J232B0176总仓库存
                          , -2  # ZH02B215190T796242总仓库存
                          , 1.88  # 验证值
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
                          , 18778  # 门店销售总额期待增加值
                          , 18778  # 门店平台销售总额期待增加值
                          )
        # 验证数据
        self._data_assertion()

    def test_2_pos_Combination_and_common_exchange_part(self):
        """
       组合商品与普通商品pos订单，部分换货(普通商品)
        :return:
        """
        logging.debug("test_2_possskucombi_return_part")
        if globals()['shopping_order_id'] is not None:
            exchange_order_id = globals()['shopping_order_id'] + "_0"
            pos_param={
                'sub_order_id': exchange_order_id,
                'goods_num':'1','goods_total_price':'3244.80',
                'reason':'30天无理由换货',
                'remarks':'哈哈','type':'2' ,
                'goods_list':'[{"num":1,"sku_id":"4879","sku_name":"腰背夹","sku_detail":"深蓝色 64","tiaoma":"M216C237C0464","kuanhao":"M216C237","danjia":"3380.00","img":"https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg"}]',


            }
            market_service.exchange_order(pos_param)
            # 更新充值后的验证数据
            self._test_data.update_post_verify_data()
            # 封装验证值
            self.expectedData(0  # 会员消费额
                              , 0  # 会员积分
                              , 2  # 会员卡等级
                              , 0  # 会员余额
                              , 0  # 总揽到店次数
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
                              , 1  # M216C237C0458门店库存
                              , -1  # M216C237C0464门店库存
                              , 0  # M116E248B0158门店库存
                              , 0  # M116E248B0164门店库存
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





    def test_3_Combination_and_common_return_part(self):
                """
               换的商品退货
                :return:
                """
                logging.debug("test_3_recharge_return_other")
                if globals()['shopping_order_id'] is not None:
                    exchange_order_id = market_service.find_order_id(globals()['shopping_order_id'],
                                                                                 self._customer.member_number)
                    exchange_order_id_a=exchange_order_id +'_0'
                    return_exchange = {
                        'main_order_id': exchange_order_id,  'return_price':'3244.80',
                        'reason':'拍错/不想要',  'remarks':'',  'afterSales_info[0][order_id]':exchange_order_id_a,
                        'afterSales_info[0][danjia]':'3380.00',
                        'afterSales_info[0][sku_name]':'腰背夹',  'afterSales_info[0][sku_detail]':'深蓝色 64',
                        'afterSales_info[0][tiaoma]':'M216C237C0464',  'afterSales_info[0][kuanhao]':'M216C237',  'afterSales_info[0][sku_id]':'4879',
                        'afterSales_info[0][img]':'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
                        'afterSales_info[0][aftersale_num]':'1','afterSales_info[0][aftersale_money]':'3244.80',
                        'afterSales_info[0][goods_type]':'1',

                    }
                    market_service.return_order(return_exchange)
                    # 更新充值后的验证数据
                    self._test_data.update_post_verify_data()
                    # 封装验证值
                    self.expectedData(-3244  # 会员消费额
                                      , -3244  # 会员积分
                                      , 2  # 会员卡等级
                                      , 0  # 会员余额
                                      , 0  # 总揽到店次数
                                      , 0  # 总揽新增会员数
                                      , 0  # 总揽订单数
                                      , 1  # 总揽退单数
                                      , -3244  # 总揽销售总额
                                      , 0  # M216C237C0458总仓库存
                                      , 0  # M216C237C0464总仓库存
                                      , 0  # M116E248B0158总仓库存
                                      , 0  # M116E248B0164总仓库存
                                      , 0  # M316J232B01106总仓库存
                                      , 0  # M316J232B0176总仓库存
                                      , 0  # ZH02B215190T796242总仓库存
                                      , -0.32  # 验证值
                                      , 0  # M216C237C0458门店库存
                                      , 1  # M216C237C0464门店库存
                                      , 0  # M116E248B0158门店库存
                                      , 0  # M116E248B0164门店库存
                                      , 0  # M316J232B01106门店库存
                                      , 0  # M316J232B0176门店库存
                                      , 0  # ZH02B215190T796242门店库存
                                      , 0  # 门店到店次数期待增加值
                                      , 0  # 门店新增会员数期待增加值
                                      , 0  # 门店订单数期待增加值
                                      , 0  # 门店退单数期待增加值
                                      , -3244  # 门店销售总额期待增加值
                                      ,-3244  # 门店平台销售总额期待增加值
                                      )
                    # 验证数据
                    self._data_assertion()

    def test_4_Combination_and_common_return_other(self):
        """
        组合商品与普通商品posd订单，其余商品退货
        :return:
        """
        logging.debug("test_4_Combination_and_common_return_other")
        if globals()['shopping_order_id'] is not None:
            return_order_id = globals()['shopping_order_id'] + "_2"
            return_order_id_a = globals()['shopping_order_id'] + "_1"
            return_order_id_b = globals()['shopping_order_id'] + "_0"

            return_other = {
    'main_order_id': globals()['shopping_order_id'], 'return_price': '15532.80',
    'reason': '缺货', 'remarks': '', 'afterSales_info[0][order_id]': return_order_id,
    'afterSales_info[0][danjia]': '6400.00',
    'afterSales_info[0][sku_name]': '孟伟组合商品', 'afterSales_info[0][sku_detail]': '2件商品',
    'afterSales_info[0][tiaoma]': 'ZH02B215190T796242', 'afterSales_info[0][kuanhao]': '',
    'afterSales_info[0][sku_id]': '5955',
    'afterSales_info[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019080310765489321.jpg',
    'afterSales_info[0][aftersale_num]': '1', 'afterSales_info[0][aftersale_money]': '6144.00',
    'afterSales_info[0][goods_type]': '2',
    'afterSales_info[1][order_id]': return_order_id_a, 'afterSales_info[1][danjia]': '6400.00',
    'afterSales_info[1][sku_name]': '孟伟组合商品', 'afterSales_info[1][sku_detail]': '2件商品',
    'afterSales_info[1][tiaoma]': 'ZH02B215190T796242', 'afterSales_info[1][kuanhao]': '',
    'afterSales_info[1][sku_id]': '5955',
    'afterSales_info[1][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019080310765489321.jpg',
    'afterSales_info[1][aftersale_num]': '1', 'afterSales_info[1][aftersale_money]': '6144.00',
    'afterSales_info[1][goods_type]': '2', 'afterSales_info[2][order_id]':  return_order_id_b,
    'afterSales_info[2][danjia]': '3380.00',
    'afterSales_info[2][sku_name]': '腰背夹', 'afterSales_info[2][sku_detail]': '深蓝色 58',
    'afterSales_info[2][tiaoma]': 'M216C237C0458', 'afterSales_info[2][kuanhao]': 'M216C237',
    'afterSales_info[2][sku_id]': '4878',
    'afterSales_info[2][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
    'afterSales_info[2][aftersale_num]': '1',
    'afterSales_info[2][aftersale_money]': '3244.80',
    'afterSales_info[2][goods_type]': '1'

            }
            market_service.return_order(return_other)
            # 更新充值后的验证数据
            self._test_data.update_post_verify_data()
            # 封装验证值
            self.expectedData(-15532  # 会员消费额
                              , -15532  # 会员积分
                              , 2  # 会员卡等级
                              , 0  # 会员余额
                              , 0  # 总揽到店次数
                              , 0  # 总揽新增会员数
                              , 0  # 总揽订单数
                              , 1  # 总揽退单数
                              , -15532  # 总揽销售总额
                              , 0  # M216C237C0458总仓库存
                              , 0  # M216C237C0464总仓库存
                              , 0  # M116E248B0158总仓库存
                              , 0  # M116E248B0164总仓库存
                              , 0  # M316J232B01106总仓库存
                              , 0  # M316J232B0176总仓库存
                              , 2  # ZH02B215190T796242总仓库存
                              , -1.55  # 验证值
                              , 7  # M216C237C0458门店库存
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
                              , -15532  # 门店销售总额期待增加值
                              , -15532  # 门店平台销售总额期待增加值
                              )
            # 验证数据
            self._data_assertion()



















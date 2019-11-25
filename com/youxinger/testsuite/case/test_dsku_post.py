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

    def test_1_dsku_post_order(self):
        """
        pos下单
        ZH02B215190T796242   2件
        2件选择 深蓝色 58 和黑色 58
        ZH02B215190T264284   2件
        2件选择 深蓝色 58 和黑色 58
        :return:
        """
        logging.debug("test_1_dsku_post_order")
        recharge_param = {'price': '19400.00', 'discount_money': '776.00', 'real_pay': '18624.00',
                          'receive_name': self._customer.consignee, 'receive_phone': self._customer.phone,
                          'receive_sheng': self._customer.province, 'receive_shi': self._customer.city,
                          'receive_diqu': self._customer.area, 'receive_address': self._customer.address,
                          'member_id': self._customer.member_number, 'member_name': self._customer.name,
                          'member_phone': self._customer.phone,
                          'plateform_id': self._customer.platform.platform_id,
                          'special_employee_id': self._customer.employee.employee_id, 'discount_rate': '0.96',
                          'goods_list[0][danjia]': '1000.00', 'goods_list[0][sku_num]': '3',
                          'goods_list[0][sku_name]': '腰背夹',
                          'goods_list[0][price]': '3000.00', 'goods_list[0][real_pay_price]': '2880.00',
                          'goods_list[0][discount_price]': '120.00',
                          'goods_list[0][sku_id]': '4878', 'goods_list[0][tiaoma]': 'M216C237C0458',
                          'goods_list[0][kuanhao]': 'M216C237',
                          'goods_list[0][sku_detail]': '深蓝色 58',
                          'goods_list[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
                          'goods_list[0][repo_out_num]': '3', 'goods_list[0][com_out_num]': '0',
                          'goods_list[0][no_discount]': '0', 'goods_list[0][no_score]': '0',
                          'goods_list[0][is_active]': '0', 'goods_list[0][type]': '2', 'goods_list[0][zh_num]': '1',
                          'goods_list[0][zh_repo_out_num]': '1', 'goods_list[0][zh_com_out_num]': '0',
                          'goods_list[0][zh_tiaoma]:': 'ZH02B215190T264284',
                          'goods_list[0][zh_mark]': '1', 'goods_list[0][zh_no_discount]': '0',
                          'goods_list[0][zh_no_score]': '0', 'goods_list[1][danjia]': '300.00',
                          'goods_list[1][sku_num]': '1',
                          'goods_list[1][sku_name]': '包臀内裤', 'goods_list[1][price]': '300.00',
                          'goods_list[1][real_pay_price]': '288.00', 'goods_list[1][discount_price]': '12.00',
                          'goods_list[1][sku_id]': '4701',
                          'goods_list[1][tiaoma]': 'M116E248B0158', 'goods_list[1][kuanhao]': 'M116E248',
                          'goods_list[1][sku_detail]': '黑色 58',
                          'goods_list[1][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
                          'goods_list[1][repo_out_num]': '1',
                          'goods_list[1][com_out_num]': '0', 'goods_list[1][no_discount]': '0',
                          'goods_list[1][no_score]': '0', 'goods_list[1][is_active]': '0', 'goods_list[1][type]': '2',
                          'goods_list[1][zh_num]': '1', 'goods_list[1][zh_repo_out_num]': '1',
                          'goods_list[1][zh_com_out_num]': '0', 'goods_list[1][zh_tiaoma]:': 'ZH02B215190T264284',
                          'goods_list[1][zh_mark]': '1', 'goods_list[1][zh_no_discount]': '0',
                          'goods_list[1][zh_no_score]': '0', 'goods_list[2][danjia]': '1000.00',
                          'goods_list[2][sku_num]': '3',
                          'goods_list[2][sku_name]': '腰背夹', 'goods_list[2][price]': '3000.00',
                          'goods_list[2][real_pay_price]': '2880.00', 'goods_list[2][discount_price]': '120.00',
                          'goods_list[2][sku_id]': '4878',
                          'goods_list[2][tiaoma]': 'M216C237C0458', 'goods_list[2][kuanhao]': 'M216C237',
                          'goods_list[2][sku_detail]': '深蓝色 58',
                          'goods_list[2][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
                          'goods_list[2][repo_out_num]': '3',
                          'goods_list[2][com_out_num]': '0', 'goods_list[2][no_discount]': '0',
                          'goods_list[2][no_score]': '0', 'goods_list[2][is_active]': '0', 'goods_list[2][type]': '2',
                          'goods_list[2][zh_num]': '1', 'goods_list[2][zh_repo_out_num]': '1',
                          'goods_list[2][zh_com_out_num]': '0', 'goods_list[2][zh_tiaoma]:': 'ZH02B215190T264284',
                          'goods_list[2][zh_mark]': '2', 'goods_list[2][zh_no_discount]': '0',
                          'goods_list[2][zh_no_score]': '0', 'goods_list[3][danjia]': '300.00',
                          'goods_list[3][sku_num]': '1',
                          'goods_list[3][sku_name]': '包臀内裤', 'goods_list[3][price]': '300.00',
                          'goods_list[3][real_pay_price]': '288.00', 'goods_list[3][discount_price]': '12.00',
                          'goods_list[3][sku_id]': '4701',
                          'goods_list[3][tiaoma]': 'M116E248B0158', 'goods_list[3][kuanhao]': 'M116E248',
                          'goods_list[3][sku_detail]': '黑色 58',
                          'goods_list[3][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
                          'goods_list[3][repo_out_num]': '1',
                          'goods_list[3][com_out_num]': '0', 'goods_list[3][no_discount]': '0',
                          'goods_list[3][no_score]': '0', 'goods_list[3][is_active]': '0', 'goods_list[3][type]': '2',
                          'goods_list[3][zh_num]': '1', 'goods_list[3][zh_repo_out_num]': '1',
                          'goods_list[3][zh_com_out_num]': '0', 'goods_list[3][zh_tiaoma]:': 'ZH02B215190T264284',
                          'goods_list[3][zh_mark]': '2', 'goods_list[3][zh_no_discount]': '0',
                          'goods_list[3][zh_no_score]': '0', 'goods_list[4][danjia]': '2000.00',
                          'goods_list[4][sku_num]': '3',
                          'goods_list[4][sku_name]': '腰背夹', 'goods_list[4][price]': '6000.00',
                          'goods_list[4][real_pay_price]': '5760.00', 'goods_list[4][discount_price]': '240.00',
                          'goods_list[4][sku_id]': '4878',
                          'goods_list[4][tiaoma]': 'M216C237C0458', 'goods_list[4][kuanhao]': 'M216C237',
                          'goods_list[4][sku_detail]': '深蓝色 58',
                          'goods_list[4][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
                          'goods_list[4][repo_out_num]': '3',
                          'goods_list[4][com_out_num]': '0', 'goods_list[4][no_discount]': '0',
                          'goods_list[4][no_score]': '0', 'goods_list[4][is_active]': '0', 'goods_list[4][type]': '2',
                          'goods_list[4][zh_num]': '1', 'goods_list[4][zh_repo_out_num]': '1',
                          'goods_list[4][zh_com_out_num]': '0', 'goods_list[4][zh_tiaoma]:': 'ZH02B215190T796242',
                          'goods_list[4][zh_mark]': '3', 'goods_list[4][zh_no_discount]': '0',
                          'goods_list[4][zh_no_score]': '0', 'goods_list[5][danjia]': '400.00',
                          'goods_list[5][sku_num]': '1',
                          'goods_list[5][sku_name]': '包臀内裤', 'goods_list[5][price]': '400.00',
                          'goods_list[5][real_pay_price]': '384.00', 'goods_list[5][discount_price]': '16.00',
                          'goods_list[5][sku_id]': '4701',
                          'goods_list[5][tiaoma]': 'M116E248B0158', 'goods_list[5][kuanhao]': 'M116E248',
                          'goods_list[5][sku_detail]': '黑色 58',
                          'goods_list[5][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
                          'goods_list[5][repo_out_num]': '1',
                          'goods_list[5][com_out_num]': '0', 'goods_list[5][no_discount]': '0',
                          'goods_list[5][no_score]': '0', 'goods_list[5][is_active]': '0', 'goods_list[5][type]': '2',
                          'goods_list[5][zh_num]': '1', 'goods_list[5][zh_repo_out_num]': '1',
                          'goods_list[5][zh_com_out_num]': '0', 'goods_list[5][zh_tiaoma]:': 'ZH02B215190T796242',
                          'goods_list[5][zh_mark]': '3', 'goods_list[5][zh_no_discount]': '0',
                          'goods_list[5][zh_no_score]': '0','goods_list[6][danjia]': '2000.00',
                          'goods_list[6][sku_num]': '3',
                          'goods_list[6][sku_name]': '腰背夹', 'goods_list[6][price]': '6000.00',
                          'goods_list[6][real_pay_price]': '5760.00', 'goods_list[6][discount_price]': '240.00',
                          'goods_list[6][sku_id]': '4878',
                          'goods_list[6][tiaoma]': 'M216C237C0458', 'goods_list[6][kuanhao]': 'M216C237',
                          'goods_list[6][sku_detail]': '深蓝色 58',
                          'goods_list[6][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
                          'goods_list[6][repo_out_num]': '3',
                          'goods_list[6][com_out_num]': '0', 'goods_list[6][no_discount]': '0',
                          'goods_list[6][no_score]': '0', 'goods_list[6][is_active]': '0', 'goods_list[6][type]': '2',
                          'goods_list[6][zh_num]': '1', 'goods_list[6][zh_repo_out_num]': '1',
                          'goods_list[6][zh_com_out_num]': '0', 'goods_list[6][zh_tiaoma]:': 'ZH02B215190T796242',
                          'goods_list[6][zh_mark]': '4', 'goods_list[6][zh_no_discount]': '0',
                          'goods_list[6][zh_no_score]': '0', 'goods_list[7][danjia]': '400.00',
                          'goods_list[7][sku_num]': '1',
                          'goods_list[7][sku_name]': '包臀内裤', 'goods_list[7][price]': '400.00',
                          'goods_list[7][real_pay_price]': '384.00', 'goods_list[7][discount_price]': '16.00',
                          'goods_list[7][sku_id]': '4701',
                          'goods_list[7][tiaoma]': 'M116E248B0158', 'goods_list[7][kuanhao]': 'M116E248',
                          'goods_list[7][sku_detail]': '黑色 58',
                          'goods_list[7][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
                          'goods_list[7][repo_out_num]': '1',
                          'goods_list[7][com_out_num]': '0', 'goods_list[7][no_discount]': '0',
                          'goods_list[7][no_score]': '0', 'goods_list[7][is_active]': '0', 'goods_list[7][type]': '2',
                          'goods_list[7][zh_num]': '1', 'goods_list[7][zh_repo_out_num]': '1',
                          'goods_list[7][zh_com_out_num]': '0', 'goods_list[7][zh_tiaoma]:': 'ZH02B215190T796242',
                          'goods_list[7][zh_mark]': '4', 'goods_list[7][zh_no_discount]': '0',
                          'goods_list[7][zh_no_score]': '0', 'pay_type': 'pos'
                          }
        # 下单购物
        globals()['shopping_order_id'] = market_service.pos_order(recharge_param)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 验证值
        self.expectedData(18624.00  # 会员消费额
                          , 18624.00  # 会员积分
                          , 2  # 会员卡等级
                          , 0  # 会员余额
                          , 1  # 总揽到店次数
                          , 0  # 总揽新增会员数
                          , 1  # 总揽订单数
                          , 0  # 总揽退单数
                          , 18624.00  # 总揽销售总额
                          , 0  # M216C237C0458总仓库存
                          , 0  # M216C237C0464总仓库存
                          , 0  # M116E248B0158总仓库存
                          , 0  # M116E248B0164总仓库存
                          , 0  # M316J232B01106总仓库存
                          , 0  # M316J232B0176总仓库存
                          , -2  # ZH02B215190T796242总仓库存
                          , 1.86  # 验证值
                          , -12  # M216C237C0458门店库存
                          , 0  # M216C237C0464门店库存
                          , -4  # M116E248B0158门店库存
                          , 0  # M116E248B0164门店库存
                          , 0  # M316J232B01106门店库存
                          , 0  # M316J232B0176门店库存
                          , 0  # ZH02B215190T796242门店库存
                          , 1  # 门店到店次数期待增加值
                          , 0  # 门店新增会员数期待增加值
                          , 1  # 门店订单数期待增加值
                          , 0  # 门店退单数期待增加值
                          , 18624.00  # 门店销售总额期待增加值
                          , 18624.00  # 门店平台销售总额期待增加值
                          )
        # 验证数据
        self._data_assertion()

    def test_2_return_all(self):
        """
        退货4件组合商品
        ZH02B215190T796242   2件
        2件选择 深蓝色 58 和黑色 58
        ZH02B215190T264284   2件
        2件选择 深蓝色 58 和黑色 58
        :return:
        """
        logging.debug("test_2_return_all")
        if globals()['shopping_order_id'] is not None:
            return_order_id0 = globals()['shopping_order_id'] + "_0"
            return_order_id1 = globals()['shopping_order_id'] + "_1"
            return_order_id2 = globals()['shopping_order_id'] + "_2"
            return_order_id3 = globals()['shopping_order_id'] + "_3"
            return_param = {'main_order_id': globals()['shopping_order_id'], 'return_price': '18624.00', 'reason': '拍错/不想要', 'remarks': '萨范德',
                            'afterSales_info[0][order_id]': return_order_id0, 'afterSales_info[0][danjia]': '3300.00', 'afterSales_info[0][sku_name]': '自动化测试勿删',
                            'afterSales_info[0][sku_detail]': '2件商品', 'afterSales_info[0][tiaoma]': 'ZH02B215190T264284', 'afterSales_info[0][kuanhao]': '', 'afterSales_info[0][sku_id]': '5973',
                            'afterSales_info[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019082058742101936.jpg', 'afterSales_info[0][aftersale_num]': '1',
                            'afterSales_info[0][aftersale_money]': '3168.00', 'afterSales_info[0][goods_type]': '2',
                            'afterSales_info[1][order_id]': return_order_id1, 'afterSales_info[1][danjia]': '3300.00',
                            'afterSales_info[1][sku_name]': '自动化测试勿删', 'afterSales_info[1][sku_detail]': '2件商品', 'afterSales_info[1][tiaoma]': 'ZH02B215190T264284', 'afterSales_info[1][kuanhao]': '',
                            'afterSales_info[1][sku_id]': '5973', 'afterSales_info[1][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019082058742101936.jpg',
                            'afterSales_info[1][aftersale_num]': '1', 'afterSales_info[1][aftersale_money]': '3168.00', 'afterSales_info[1][goods_type]': '2',
                            'afterSales_info[2][order_id]': return_order_id2, 'afterSales_info[2][danjia]': '6400.00', 'afterSales_info[2][sku_name]':'孟伟组合商品', 'afterSales_info[2][sku_detail]': '2件商品',
                            'afterSales_info[2][tiaoma]': 'ZH02B215190T796242', 'afterSales_info[2][kuanhao]': '', 'afterSales_info[2][sku_id]': '5955',
                            'afterSales_info[2][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019080310765489321.jpg', 'afterSales_info[2][aftersale_num]': '1', 'afterSales_info[2][aftersale_money]': '6144.00', 'afterSales_info[2][goods_type]': '2',
                            'afterSales_info[3][order_id]': return_order_id3, 'afterSales_info[3][danjia]': '6400.00', 'afterSales_info[3][sku_name]': '孟伟组合商品', 'afterSales_info[3][sku_detail]': '2件商品',
                            'afterSales_info[3][tiaoma]': 'ZH02B215190T796242', 'afterSales_info[3][kuanhao]': '', 'afterSales_info[3][sku_id]':'5955', 'afterSales_info[3][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019080310765489321.jpg',
                            'afterSales_info[3][aftersale_num]': '1', 'afterSales_info[3][aftersale_money]': '6144.00', 'afterSales_info[3][goods_type]':'2'}

            market_service.return_order(return_param)
            # 更新充值后的验证数据
            self._test_data.update_post_verify_data()
            # 验证值
            self.expectedData(-18624.00 # 会员消费额
                              , -18624 # 会员积分
                              , 2 # 会员卡等级
                              , 0 # 会员余额
                              , 0 # 总揽到店次数
                              , 0 # 总揽新增会员数
                              , 0 # 总揽订单数
                              , 0 # 总揽退单数
                              , -18624.00 # 总揽销售总额
                              , 0 # M216C237C0458总仓库存
                              , 0 # M216C237C0464总仓库存
                              , 0 # M116E248B0158总仓库存
                              , 0 # M116E248B0164总仓库存
                              , 0 # M316J232B01106总仓库存
                              , 0 # M316J232B0176总仓库存
                              , 2 # ZH02B215190T796242总仓库存
                              , -1.86 # 验证值
                              , 12 # M216C237C0458门店库存
                              , 0 # M216C237C0464门店库存
                              , 4 # M116E248B0158门店库存
                              , 0 # M116E248B0164门店库存
                              , 0 # M316J232B01106门店库存
                              , 0 # M316J232B0176门店库存
                              , 0 # ZH02B215190T796242门店库存
                              , 0 # 门店到店次数期待增加值
                              , 0 # 门店新增会员数期待增加值
                              , 0 # 门店订单数期待增加值
                              , 0 # 门店退单数期待增加值
                              , -18624.00 # 门店销售总额期待增加值
                              , -18624.00 # 门店平台销售总额期待增加值
                              )
            # 验证数据
            self._data_assertion()

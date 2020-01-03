from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service


class TestRewardGoods(BaseCase):
    """
     积分商城积分下单测试
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

    def test_1_Reward_shopping_order(self):
        """
        积分商城积分下单测试
        ‘hmr组合商品’ 1件
        积分和pos 混合兑换
        :return:
        """
        logging.debug("test_1_Reward_shopping_order")
        recharge_param = {'exchange_type': 'mix', 'total_score': '0', 'total_mix_score': '121','total_mix_price': '1222.00',
                          'receive_name': self._customer.consignee, 'receive_phone': self._customer.phone,
                          'receive_sheng': self._customer.province, 'receive_shi': self._customer.city,
                          'receive_diqu': '', 'receive_address': self._customer.address,
                          'member_id': self._customer.member_number, 'member_name': self._customer.name,
                          'member_phone': self._customer.phone,
                          'plateform_id': self._customer.platform.platform_id,
                          'special_employee_id': self._customer.employee.employee_id,
                          'pay_type': 'pos', 'goods_info[sku_num]': '1', 'beizhu': '',
                          'goods_info[sku_name]': '何明锐组合', 'goods_info[sku_id]': '506',
                          'goods_info[tiaoma]': 'ZH02B9797T638168','goods_info[kuanhao]':'',
                          'goods_info[sku_detail]': '2件商品',
                          'goods_info[img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019121824561739108.jpg',
                          'goods_info[type]': '2','goods_info[sub_goods][0][sku_num]': '1',
                          'goods_info[sub_goods][0][sku_name]': '运动文胸',
                          'goods_info[sub_goods][0][sku_id]': '175',
                          'goods_info[sub_goods][0][tiaoma]': 'M819A334B01_A75',
                          'goods_info[sub_goods][0][kuanhao]': 'M819A334',
                          'goods_info[sub_goods][0][kuanhao_id]': 'styleNun5523',
                          'goods_info[sub_goods][0][sku_detail]': 'A 黑色 75',
                          'goods_info[sub_goods][0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019112819237451086.jpg',
                          'goods_info[sub_goods][1][sku_num]': '1','goods_info[sub_goods][1][sku_name]': '防走光裤',
                          'goods_info[sub_goods][1][sku_id]': '192','goods_info[sub_goods][1][tiaoma]': 'M619D294E0264',
                          'goods_info[sub_goods][1][kuanhao]': 'M619D294', 'goods_info[sub_goods][1][kuanhao_id]': 'styleNun1804',
                          'goods_info[sub_goods][1][sku_detail]': '豆沙紫 64',
                          'goods_info[sub_goods][1][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019112810238741596.jpg'}
        globals()['shopping_order_id'] = market_service.rewards_order_2(recharge_param)

        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 封装验证值
        self.expectedData(0  # 会员消费额
                          , -121  # 会员积分
                          , 2  # 会员卡等级
                          , 0  # 会员余额
                          , 1  # 总揽到店次数
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

    def test_2_Reward_shopping_order_refund(self):
        """
         后台退积分商品
         ‘hmr组合商品’ 1件
        :return:
        """
        logging.debug("test_2_return_sameCodeAndBar_order")

        market_service.rewards_order_refund(globals()['shopping_order_id'] )
        # market_service.return_order_success(aftersaleid)

        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()

        # 封装期待值
        self.expectedData(0  # 会员消费额
                          ,121 # 会员积分
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
                          , 0 # ZH02B215190T796242总仓库存
                          , 0  # 验证值
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
                          , 0  # 门店销售总额期待增加值
                          , 0  # 门店平台销售总额期待增加值
                          )

        # 验证数据
        self._data_assertion()

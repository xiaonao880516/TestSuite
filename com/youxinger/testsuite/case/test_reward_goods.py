
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
        :return:
        """
        logging.debug("test_1_Reward_shopping_order")
        recharge_param = {'exchange_type': 'score', 'total_score': '1370', 'total_mix_score': '0','total_mix_price': '0',
                          'receive_name': self._customer.consignee, 'receive_phone': self._customer.phone,
                          'receive_sheng': self._customer.province, 'receive_shi': self._customer.city,
                          'receive_diqu': '', 'receive_address': self._customer.address,
                          'member_id': self._customer.member_number, 'member_name': self._customer.name,
                          'member_phone': self._customer.phone,
                          'plateform_id': self._customer.platform.platform_id,
                          'special_employee_id': self._customer.employee.employee_id,
                          'pay_type': '', 'goods_info[sku_num]': '1',
                          'goods_info[sku_name]': 'hmr普通商品',
                          'goods_info[sku_id]': '570', 'goods_info[tiaoma]': 'H137M086C0465',
                          'goods_info[kuanhao]': 'H137M086',
                          'goods_info[sku_detail]': '深蓝色 65',
                          'goods_info[img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019120568310451792.jpg',
                          'goods_info[type]': '1',
                          'goods_info[sub_goods]': '',


                          }
        globals()['shopping_order_id'] = market_service.rewards_order(recharge_param)

        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 封装验证值
        self.expectedData(0  # 会员消费额
                          , -1370  # 会员积分
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
                          ,0  # M116E248B0158门店库存
                          , 0  # M116E248B0164门店库存
                          , 0  # M316J232B01106门店库存
                          , 0  # M316J232B0176门店库存
                          , 0  # ZH02B215190T796242门店库存
                          , 1  # 门店到店次数期待增加值
                          , 0  # 门店新增会员数期待增加值
                          , 0  # 门店订单数期待增加值
                          , 0  # 门店退单数期待增加值
                          , 0 # 门店销售总额期待增加值
                          , 0  # 门店平台销售总额期待增加值
                          )
        # 验证数据
        self._data_assertion()

    def test_2_Reward_shopping_order_refund(self):
        """
         后台退款商品
        :return:
        """
        logging.debug("test_2_return_sameCodeAndBar_order")

        market_service.rewards_order_refund(globals()['shopping_order_id'] )
        # market_service.return_order_success(aftersaleid)

        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()

        # 封装期待值
        self.expectedData(0  # 会员消费额
                          ,1370 # 会员积分
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













from com.youxinger.testsuite.bean.area import AreaVerifyData
from com.youxinger.testsuite.bean.customer import CustomerVerifyData
from com.youxinger.testsuite.bean.employee import EmployeeVerifyData
from com.youxinger.testsuite.bean.platform import PlatVerifyData
from com.youxinger.testsuite.bean.store import StoreVerifyData
from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service
from com.youxinger.testsuite.utils.constant import AREA, STORE


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
        self._referral.update_pre_verify_data()

    def tearDown(self):
        super().tearDown()

    def test_1_pos_shopping_order(self):
        """
        pos门店总仓混合下单单购物成功检测
        腰背夹M216C237，深蓝色，58 总仓5个，门店5个
        填写转介绍人
        :return:
        """
        logging.debug("test_1_pos_shopping_order")
        order_param = {'price': '33800.00', 'discount_money': '2704.00', 'real_pay': '31096.00', 'receive_name': self._customer.consignee, 'receive_phone': self._customer.phone,
                       'receive_sheng': self._customer.province, 'receive_shi': self._customer.city, 'receive_diqu': self._customer.area, 'receive_address': self._customer.address,
                       'member_id': self._customer.member_number, 'member_name': self._customer.name, 'member_phone': self._customer.phone,
                       'plateform_id': self._customer.platform.platform_id, 'special_employee_id': self._customer.employee.employee_id, 'discount_rate': '0.92',
                       'goods_list[0][danjia]': '3380.00', 'goods_list[0][sku_num]': '10', 'goods_list[0][sku_name]': '腰背夹',
                       'goods_list[0][price]': '33800.00', 'goods_list[0][real_pay_price]': '31096.00', 'goods_list[0][discount_price]': '2704.00',
                       'goods_list[0][sku_id]': '4878', 'goods_list[0][tiaoma]': 'M216C237C0458', 'goods_list[0][kuanhao]': 'M216C237',
                       'goods_list[0][sku_detail]': '深蓝色 58', 'goods_list[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
                       'goods_list[0][repo_out_num]': '5', 'goods_list[0][com_out_num]': '5', 'goods_list[0][no_discount]': '0', 'goods_list[0][no_score]': '0',
                       'goods_list[0][is_active]': '0', 'goods_list[0][type]': '1', 'pay_type': 'pos', 'zip_code': '', 'referral_phone': '17151800001', 'beizhu': '',
                       'discount_id': '', 'discount_description': '', 'coupon_id': '', 'coupon_discount_amount': '0.00', 'coupon_discount_rate': ''}
        # 下单购物
        globals()['shopping_order_id'] = market_service.no_pos_order(order_param)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        self._referral.update_post_verify_data()
        # 封装验证值
        self._customer.expectedData = CustomerVerifyData.expected_data(31096, 31096, 3, 0)  # 更新会员验证值
        # self._global.expectedData = LCGlobalVerifyData.expected_data(1, 0, 1, 0, 31096)  # 更新总览验证值

        expected_global_repo = {'M216C237C0458': -5, 'M216C237C0464': 0, 'M116E248B0158': 0, 'M116E248B0164': 0,
                                'M316J232B01106': 0, 'M316J232B0176': 0, 'ZH02B215190T796242': 0}
        self._global.repository.update_expected_verify_data(expected_global_repo)  # 更新总览库存验证值

        expected_area_values = {AREA['area_id']: AreaVerifyData.expected_data(3.11)}
        self._global.update_expected_area_verify_data(expected_area_values)  # 更新大区验证值

        self._platform.expectedData = PlatVerifyData.expected_data(3.11)  # 更新平台验证值
        self._employee.expectedData = EmployeeVerifyData.expected_data(3.11)  # 更新员工验证值

        expected_store_repo = {'M216C237C0458': -5, 'M216C237C0464': 0, 'M116E248B0158': 0, 'M116E248B0164': 0,
                               'M316J232B01106': 0, 'M316J232B0176': 0, 'ZH02B215190T796242': 0}
        self._store.repository.update_expected_verify_data(expected_store_repo)  # 更新门店库存验证值

        expected_store_values = {STORE['store_id']: StoreVerifyData.expected_data(1, 0, 1, 0, 31096, 31096)}
        self._area.update_expected_store_verify_data(expected_store_values)  # 更新门店验证值
        self._referral.expectedData = CustomerVerifyData.expected_data(0, 31096, 5, 0)
        # 验证数据
        self._data_assertion()

    def test_2_cancellation_order(self):
        """
        取消支付
        :return:
        """
        logging.debug("test_2_cancellation_order")
        if globals()['shopping_order_id'] is not None:
            market_service.cancellation_of_order(globals()['shopping_order_id'])
            # 更新充值后的验证数据
            self._test_data.update_post_verify_data()
            self._referral.update_post_verify_data()
            # 验证值
            self.expectedData(-31096 # 会员消费额
                              , -31096 # 会员积分
                              , 2 # 会员卡等级
                              , 0 # 会员余额
                              , 0 # 总揽到店次数
                              , 0 # 总揽新增会员数
                              , 0 # 总揽订单数
                              , 0 # 总揽退单数
                              , -31096 # 总揽销售总额
                              , 5 # M216C237C0458总仓库存
                              , 0 # M216C237C0464总仓库存
                              , 0 # M116E248B0158总仓库存
                              , 0 # M116E248B0164总仓库存
                              , 0 # M316J232B01106总仓库存
                              , 0 # M316J232B0176总仓库存
                              , 0 # ZH02B215190T796242总仓库存
                              , -3.11 # 验证值
                              , 5 # M216C237C0458门店库存
                              , 0 # M216C237C0464门店库存
                              , 0 # M116E248B0158门店库存
                              , 0 # M116E248B0164门店库存
                              , 0 # M316J232B01106门店库存
                              , 0 # M316J232B0176门店库存
                              , 0 # ZH02B215190T796242门店库存
                              , 0 # 门店到店次数期待增加值
                              , 0 # 门店新增会员数期待增加值
                              , 0 # 门店订单数期待增加值
                              , 0 # 门店退单数期待增加值
                              , -31096 # 门店销售总额期待增加值
                              , -31096 # 门店平台销售总额期待增加值
                              )
            self._referral.expectedData = CustomerVerifyData.expected_data(0, -31096, 5, 0)
            # 验证数据
            self._data_assertion()
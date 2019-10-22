from com.youxinger.testsuite.bean.customer import CustomerVerifyData
from com.youxinger.testsuite.bean.lc_global import LCGlobalVerifyData
from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service
from com.youxinger.testsuite.utils.constant import AREA


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

    def tearDown(self):
        super().tearDown()

    def test_1_pos_shopping_order(self):
        """
        pos门店总仓混合下单单购物成功检测
        腰背夹M216C237，深蓝色，58 总仓5个，门店5个
        :return:
        """
        logging.debug("test_pos_shopping_order")
        # 更新充值前的验证数据
        self._test_data.update_pre_verify_data()
        order_param = {'price': '33800.00', 'discount_money': '2704.00', 'real_pay': '31096.00', 'receive_name': self._customer.consignee, 'receive_phone': self._customer.phone,
                       'receive_sheng': self._customer.province, 'receive_shi': self._customer.city, 'receive_diqu': self._customer.area, 'receive_address': self._customer.address,
                       'member_id': self._customer.member_number, 'member_name': self._customer.name, 'member_phone': self._customer.phone,
                       'plateform_id': self._customer.platform.platform_id, 'special_employee_id': self._customer.employee.employee_id, 'discount_rate': '0.92',
                       'goods_list[0][danjia]': '3380.00', 'goods_list[0][sku_num]': '10', 'goods_list[0][sku_name]': '腰背夹',
                       'goods_list[0][price]': '33800.00', 'goods_list[0][real_pay_price]': '31096.00', 'goods_list[0][discount_price]': '2704.00',
                       'goods_list[0][sku_id]': '4878', 'goods_list[0][tiaoma]': 'M216C237C0458', 'goods_list[0][kuanhao]': 'M216C237',
                       'goods_list[0][sku_detail]': '深蓝色 58', 'goods_list[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
                       'goods_list[0][repo_out_num]': '5', 'goods_list[0][com_out_num]': '5', 'goods_list[0][no_discount]': '0', 'goods_list[0][no_score]': '0',
                       'goods_list[0][is_active]': '0', 'goods_list[0][type]': '1', 'pay_type': 'pos', 'zip_code': '', 'referral_phone': '', 'beizhu': '',
                       'discount_id': '', 'discount_description': '', 'coupon_id': '', 'coupon_discount_amount': '0.00', 'coupon_discount_rate': ''}
        # 下单购物
        market_service.pos_order(order_param)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 封装验证值
        customer_verify_data = CustomerVerifyData()
        customer_verify_data.i_remainder = 0
        customer_verify_data.i_card_level = 3
        customer_verify_data.i_swap_score = 31096
        customer_verify_data.i_total_consume = 31096
        self._customer.expectedData = customer_verify_data

        lc_global_verify_data = LCGlobalVerifyData()
        lc_global_verify_data.i_lc_global_arrive_store_num = 1
        lc_global_verify_data.i_lc_global_newvip_num = 0
        lc_global_verify_data.i_lc_global_order_num = 1
        lc_global_verify_data.i_lc_global_refund_num = 0
        lc_global_verify_data.f_lc_global_sale_num = 31096
        self._test_data.lc_global.expectedData = lc_global_verify_data

        expected_global_repo = {'M216C237C0458': -5, 'M216C237C0464': 0, 'M116E248B0158': 0, 'M116E248B0164': 0,
                                'M316J232B01106': 0, 'M316J232B0176': 0, 'ZH02B215190T796242': 0}
        self._test_data.lc_global.repository.update_expected_verify_data(expected_global_repo)

        expected_area_values = {AREA['area_id']: 3.11}
        self._test_data.lc_global.update_expected_verify_data(expected_area_values)
        # 验证数据
        self._data_assertion()

    def test_2_return_2pieces(self):
        """
        退货2件商品数据
        腰背夹M216C237，深蓝色，58 退2个
        :return:
        """
        logging.debug("test_return_2pieces")
        pass
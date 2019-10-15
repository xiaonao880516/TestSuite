from com.youxinger.testsuite.bean.customer import Customer
from com.youxinger.testsuite.case.base_case import BaseCase
import logging

from com.youxinger.testsuite.service import customer_service, market_service
from com.youxinger.testsuite.utils.constant import CUSTOMER


class TestGeneralGoods(BaseCase):
    """
    一般商品测试
    """
    customer: Customer = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 注册新会员
        cls.customer = customer_service.register_customer(CUSTOMER)
        customer_service.recharge_customer(cls.customer, 40000)

    @classmethod
    def tearDownClass(cls):
        # 删除会员
        customer_service.del_customer(cls.customer)
        cls.customer = None
        super().tearDownClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_pos_shopping_order(self):
        """
        pos门店总仓混合下单单购物成功检测
        腰背夹M216C237，深蓝色，58 总仓5个，门店5个
        :return:
        """
        logging.debug("test_pos_shopping_order")
        order_param = {'price': '33800.00', 'discount_money': '2704.00', 'real_pay': '31096.00', 'receive_name': '孟伟', 'receive_phone': '13810567325',
                       'receive_sheng': '北京市', 'receive_shi': '北京市', 'receive_diqu': '东城区', 'receive_address': '哈哈哈', 'zip_code': '',
                       'referral_phone': '', 'beizhu': '', 'member_id': self.customer.member_number, 'member_name': self.customer.name, 'member_phone': self.customer.phone,
                       'plateform_id': '175149', 'special_employee_id': '204', 'discount_id': '', 'discount_rate': '0.92',
                       'discount_description': '', 'goods_list[0][danjia]': '3380.00', 'goods_list[0][sku_num]': '10', 'goods_list[0][sku_name]': '腰背夹',
                       'goods_list[0][price]': '33800.00', 'goods_list[0][real_pay_price]': '31096.00', 'goods_list[0][discount_price]': '2704.00',
                       'goods_list[0][sku_id]': '4878', 'goods_list[0][tiaoma]': 'M216C237C0458', 'goods_list[0][kuanhao]': 'M216C237',
                       'goods_list[0][sku_detail]': '深蓝色 58', 'goods_list[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
                       'goods_list[0][repo_out_num]': '5', 'goods_list[0][com_out_num]': '5', 'goods_list[0][no_discount]': '0', 'goods_list[0][no_score]': '0',
                       'goods_list[0][is_active]': '0', 'goods_list[0][type]': '1', 'pay_type': 'pos', 'coupon_id': '', 'coupon_discount_amount': '0.00', 'coupon_discount_rate': ''}
        market_service.pos_order(order_param)
        pass

    def test_return_2pieces(self):
        """
        退货2件商品数据
        腰背夹M216C237，深蓝色，58 退2个
        :return:
        """
        logging.debug("test_return_2pieces")
        pass
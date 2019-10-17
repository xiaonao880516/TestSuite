from com.youxinger.testsuite.bean.customer import Customer, CustomerVerifyData
from com.youxinger.testsuite.bean.employee import Employee
from com.youxinger.testsuite.bean.platform import Platform
from com.youxinger.testsuite.bean.group import Group
from com.youxinger.testsuite.case.base_case import BaseCase, TestData
import logging

from com.youxinger.testsuite.service import customer_service, market_service
from com.youxinger.testsuite.utils.constant import CUSTOMER, EMPLOYEE, PLATFORM


class TestGeneralGoods(BaseCase):
    """
    一般商品测试
    """
    customer: Customer = None
    employee: Employee = None
    platform: Platform = None
    group: Group = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 注册新会员
        cls.group = Group()
        cls.employee = Employee(EMPLOYEE['employee_name'], EMPLOYEE['employee_id'], EMPLOYEE['employee_phone'], EMPLOYEE['employee_password'])
        cls.platform = Platform(PLATFORM['name'], PLATFORM['platform_id'])
        cls.customer = customer_service.register_customer(CUSTOMER, cls.employee, cls.platform)
        cls._test_data.customers.append(cls.customer)
        cls._test_data.group = cls.group
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

    def test_1_pos_shopping_order(self):
        """
        pos门店总仓混合下单单购物成功检测
        腰背夹M216C237，深蓝色，58 总仓5个，门店5个
        :return:
        """
        logging.debug("test_pos_shopping_order")
        # 更新充值前的验证数据
        customer_service.update_customer_verify_data(False, self.customer)
        order_param = {'price': '33800.00', 'discount_money': '2704.00', 'real_pay': '31096.00', 'receive_name': self.customer.consignee, 'receive_phone': self.customer.phone,
                       'receive_sheng': self.customer.province, 'receive_shi': self.customer.city, 'receive_diqu': self.customer.area, 'receive_address': self.customer.address,
                       'member_id': self.customer.member_number, 'member_name': self.customer.name, 'member_phone': self.customer.phone,
                       'plateform_id': self.customer.platform.platform_id, 'special_employee_id': self.customer.employee.employee_id, 'discount_rate': '0.92',
                       'goods_list[0][danjia]': '3380.00', 'goods_list[0][sku_num]': '10', 'goods_list[0][sku_name]': '腰背夹',
                       'goods_list[0][price]': '33800.00', 'goods_list[0][real_pay_price]': '31096.00', 'goods_list[0][discount_price]': '2704.00',
                       'goods_list[0][sku_id]': '4878', 'goods_list[0][tiaoma]': 'M216C237C0458', 'goods_list[0][kuanhao]': 'M216C237',
                       'goods_list[0][sku_detail]': '深蓝色 58', 'goods_list[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
                       'goods_list[0][repo_out_num]': '5', 'goods_list[0][com_out_num]': '5', 'goods_list[0][no_discount]': '0', 'goods_list[0][no_score]': '0',
                       'goods_list[0][is_active]': '0', 'goods_list[0][type]': '1', 'pay_type': 'pos', 'zip_code': '', 'referral_phone': '', 'beizhu': '',
                       'discount_id': '', 'discount_description': '', 'coupon_id': '', 'coupon_discount_amount': '0.00', 'coupon_discount_rate': ''}
        market_service.pos_order(order_param)

        # 更新充值后的验证数据
        customer_service.update_customer_verify_data(True, self.customer)
        # 封装验证值
        customer_verify_data = CustomerVerifyData()
        customer_verify_data.i_remainder = 0
        customer_verify_data.i_card_level = 3
        customer_verify_data.i_swap_score = 31096
        customer_verify_data.i_total_consume = 31096
        self.customer.expectedData = customer_verify_data
        # 验证数据
        super()._data_assertion()
        pass

    def test_2_return_2pieces(self):
        """
        退货2件商品数据
        腰背夹M216C237，深蓝色，58 退2个
        :return:
        """
        logging.debug("test_return_2pieces")
        pass
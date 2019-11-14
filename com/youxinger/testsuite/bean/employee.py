import logging

from com.youxinger.testsuite.bean.i_validate import IDataVerify


class EmployeeVerifyData(object):
    """
    员工数据验证类
    """
    f_employee_sale_num = 0.0  # 员工业绩

    @classmethod
    def expected_data(cls, f_employee_sale_num):
        """
        创建预期值对象
        :param f_employee_sale_num: 员工业绩
        :return:
        """
        exp_value = cls()
        exp_value.f_employee_sale_num = f_employee_sale_num
        return exp_value


class Employee(IDataVerify):
    """
    员工
    """
    employee_name = ''
    employee_id = ''
    employee_phone = ''
    employee_password = ''
    store_id = ''  # 门店id

    preVerifyData: EmployeeVerifyData = None  # 操作前数据
    postVerifyData: EmployeeVerifyData = None  # 操作后数据
    expectedData: EmployeeVerifyData = None  # 期待增加值

    def __init__(self, employee_name, employee_id, employee_phone, employee_password):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.employee_phone = employee_phone
        self.employee_password = employee_password
        self.preVerifyData = EmployeeVerifyData()
        self.postVerifyData = EmployeeVerifyData()

    def update_pre_verify_data(self):
        """
        更新操作之前的数据
        :return:
        """
        from com.youxinger.testsuite.service import financial_data_service
        financial_data_service.get_update_employee_data(self.store_id, self.employee_id, self.preVerifyData)

    def update_post_verify_data(self):
        """
        更新操作之后的数据
        :return:
        """
        from com.youxinger.testsuite.service import financial_data_service
        financial_data_service.get_update_employee_data(self.store_id, self.employee_id, self.postVerifyData)

    def data_verify(self):
        if self.expectedData is not None:
            assert abs(
                self.postVerifyData.f_employee_sale_num - self.expectedData.f_employee_sale_num - self.preVerifyData.f_employee_sale_num) < 0.02, \
                "员工业绩检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.f_employee_sale_num, self.postVerifyData.f_employee_sale_num, self.preVerifyData.f_employee_sale_num)
        else:
            logging.debug("Employee:"+self.employee_name+", 无预期值，无需进行数据验证")
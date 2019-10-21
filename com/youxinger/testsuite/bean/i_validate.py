import abc


class IDataVerify(metaclass=abc.ABCMeta):

    def data_verify(self):
        """
        to do something
        :return:
        """

    def update_pre_verify_data(self):
        """
        更新操作之前的数据
        :return:
        """

    def update_post_verify_data(self):
        """
        更新操作之后的数据
        :return:
        """

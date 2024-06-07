from assignment.controller.exceptions import OrderNotFoundError
from assignment.model.da.da import DataAccess
from assignment.model.entity.order import Order

Order_da = DataAccess(Order)

class OrderBl:

    @staticmethod
    def save(order):
        return order_da.save(order)


    @staticmethod
    def edit(order):
        if order_da.find_by_id(order.id):
            return order_da.edit(order)
        else:
            raise OrderNotFoundError()

    @staticmethod
    def remove(id):
        order = order_da.find_by_id(id)
        if order:
            return order_da.remove(order)
        else:
            raise OrderNotFoundError()

    @staticmethod
    def find_all():
        order_list = order_da.find_all()
        if order_list:
            return order_list
        else:
            raise OrderNotFoundError()

    @staticmethod
    def find_by_id(id):
        order = order_da.find_by_id(id)
        if order:
            return order
        else:
            raise OrderNotFoundError()

    @staticmethod
    def find_by_status(status=True):
        order_list = order_da.find_by(Order.status == status)
        if order_list:
            return order_list
        else:
            raise OrderNotFoundError()





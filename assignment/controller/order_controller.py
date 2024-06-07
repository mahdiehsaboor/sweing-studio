from assignment.model.bl.order_bl import OrderBl
from assignment.model.entity.order import Order
from assignment.model.tools.decorators import exception_handling


class OrderController:
    @staticmethod
    @exception_handling
    def save(customer_id,tailor_id,order_date,deliverty_date,status=True):
        order = Order(customer_id,tailor_id,order_date,deliverty_date,status)
        return True, OrderBl.save(order)

    @staticmethod
    @exception_handling
    def edit(id,customer_id,tailor_id,order_date,deliverty_date,status=True):
        order = Order(customer_id,tailor_id,order_date,deliverty_date,status)
        order.id = id
        return True, OrderBl.edit(order)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, OrderBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, OrderBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, OrderBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_customer_id(customer_id):
        return True, OrderBl.find_by_customer_id(customer_id)

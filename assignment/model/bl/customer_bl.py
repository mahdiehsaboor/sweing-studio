from assignment.controller.exceptions import CustomerNotFoundError
from assignment.model.da.da import DataAccess
from assignment.model.entity.customer import Customer

customer_da = DataAccess(Customer)


class CustomerBl:
    @staticmethod
    def save(customer):
        return customer_da.save(customer)

    @staticmethod
    def edit(customer):
        if customer_da.find_by_id(customer.id):
            return customer_da.edit(customer)
        else:
            raise CustomerNotFoundError()

    @staticmethod
    def remove(id):
        customer = customer_da.find_by_id(id)
        if customer:
            return customer_da.remove(customer)
        else:
            raise CustomerNotFoundError()

    @staticmethod
    def find_all():
        customer_list = customer_da.find_all()
        if customer_list:
            return customer_list
        else:
            raise CustomerNotFoundError()

    @staticmethod
    def find_by_id(id):
        customer = customer_da.find_by_id(id)
        if customer:
            return customer
        else:
            raise CustomerNotFoundError()

    @staticmethod
    def find_by_family(family):
        customer_list = customer_da.find_by(Customer.family == family)
        if customer_list:
            return customer_list
        else:
            raise CustomerNotFoundError()
from assignment.model.bl.customer_bl import CustomerBl
from assignment.model.entity.customer import Customer
from assignment.model.tools.decorators import exception_handling


class CustomerController:
    @staticmethod
    @exception_handling
    def save(name, family, phone, national_id, birth_date):
        customer = Customer(name, family, phone, national_id, birth_date)
        return True, CustomerBl.save(customer)

    @staticmethod
    @exception_handling
    def edit(id, name, family , phone , email , national_id , birth_date ):
        customer = Customer( id, name, family, phone , email , national_id , birth_date )
        customer.id = id
        return True, CustomerBl.edit(customer)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, CustomerBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, CustomerBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, CustomerBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_family(family):
        return True, CustomerBl.find_by_family(family)
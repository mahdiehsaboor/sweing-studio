from assignment.model.entity import *
class Order(Base):
    __tablename__ = "order_tbl"
    id = Column(Integer, primary_key=True,autoincrement=True)
    order_date = Column(Date)
    delivery_date = Column(Date)
    status = Column(Boolean,default="True")# compelete,pending

    customer_id = Column(Integer, ForeignKey("customer_tbl.customer_id"))
    customer = relationship(Customer)

    tailor_id = Column(Integer, ForeignKey("tailor_tbl.tailor_id"))
    tailor = relationship(Tailor)

    clothes_id = Column(Integer,ForeignKey("clothes_tbl.clothes_id"))
    clothes = relationship(Clothes)

    def __init__(self,order_date, delivery_date,status,customer_id,tailor_id,clothes_id):
        self.id = None
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.status = status
        self.customer_id = customer_id
        self.tailor_id = tailor_id
        self.clothes_id = clothes_id

    @property
    def order_date(self):
        print("Get order_date")
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        print("Set order_date")
        if re.match("%Y/%m/%d", order_date):
            self._order_date = order_date
        else:
            raise ValueError("Order date ")

    @property
    def delivery_date(self):
        print("Get delivery_date")
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        print("Set delivery_date")
        if re.match("%Y/%m/%d", delivery_date):
            self._delivery_date = delivery_date
        else:
            raise ValueError("Invalid delivery date")

    @property
    def status(self):
        print("Get status")  # 'pending', 'completed' or 'cancle'
        return self._status

    @status.setter
    def status(self, status):
        print("Set status")
        if re.match("^(True|False)$", status):
            self._status = status
        else:
            raise ValueError("Invalid status")

    @property
    def customer_id(self):
        print("Get customer_id")
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        if re.match(r"^\d{8}$", customer_id):
            self._customer_id = customer_id
        else:
            raise ValueError("Invalid customer-id")

    @property
    def tailor_id(self):
        print("Get tailor_id")
        return self._tailor_id

    @tailor_id.setter
    def tailor_id(self, tailor_id):
        if re.match(r"^\d{8}$", tailor_id):
            self._tailor_id = tailor_id
        else:
            raise ValueError("Invalid tailor-id")

    @property
    def clothes_id(self):
        print("Get clothes_id")
        return self._clothes_id

    @clothes_id.setter
    def clothes_id(self, clothes_id):
        if re.match(r"^\d{8}$", clothes_id):
            self.clothes_id = clothes_id
        else:
            raise ValueError("Invalid clothes_id")


    def to_tuple(self):
        return (self.order_date, self.delivery_date, self.status , self.customer_id, self.tailor_id , self.clothes_id)

    order_date = property(fget=Order.order_date.fget, fset=Order.order_date.fset)
    delivery_date = property(fget=Order.delivery_date.fget, fset=Order.delivery_date.fset)
    status = property(fget=Order.status.fget, fset=Order.status.fset)
    customer_id = property(fget=Order.customer_id.fget, fset=Order.customer_id.fset)
    tailor_id = property(fget=Order.tailor_id.fget, fset=Order.tailor_id.fset)
    clothes_id = property(fget=Order.clothes_id.fget, fset=Order.clothes_id.fset)





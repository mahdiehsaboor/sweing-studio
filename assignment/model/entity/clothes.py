from assignment.model.entity import *


class Clothes(Base):
    __tablename__ = "clothes_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_clothes = Column(String(30), nullable=False)
    fabric = Column(String(20), nullable=False)
    color = Column(String(20),nullable=False)
    price = Column(Numeric, nullable=False)
    size = Column(String(20),nullable=False)
    description = Column(String(30),nullable=False)

    order = relationship('Order', back_populates='clothes')


    def __init__(self, name_clothes, fabric , color, price,size, description):
        self.order_id = None
        self.name_clothes = name_clothes
        self.fabric = fabric
        self.color = color
        self.price = price
        self.size = size
        self.description = description

    @property
    def name_clothes(self):
        print("Get name_clothes")
        return self._name_clothes

    @name_clothes.setter
    def name_clothes(self, name_clothes):
        print("Set name")
        if re.match("^[A-Za-z\s]+$", name_clothes):
            self._name_clothes = name_clothes
        else:
            raise ValueError("Invalid name_clothes")

    @property
    def fabric(self):
        print("Get fabric")
        return self._fabric

    @fabric.setter
    def fabric(self, fabric):
        print("Set name")
        if re.match("^[A-Za-z\s]+$", fabric):
            self._fabric = fabric
        else:
            raise ValueError("Invalid fabric")

    @property
    def color(self):
        print("Get color")
        return self._color

    @color.setter
    def color(self, color):
        print("Set color")
        if re.match("^[A-Za-z\s]+$", color):
            self._color = color
        else:
            raise ValueError("Invalid color")

    @property
    def price(self):
        print("Get price")
        return self._price

    @price.setter
    def price(self, price):
        if re.match(r"^\d+(\.\d{1,2})?$", price):  # [\d\s.,]*\d]
            self._price = price
        else:
            raise ValueError("Invalid price")

    @property
    def size(self):
        print("Get size")
        return self._size

    @size.setter
    def size(self, size):
        if re.match(r"^(XS|S|M|L|XL|XXL)$", size):
            self._size = size
        else:
            raise ValueError("Invaid size")


    @property
    def description(self):
        print("Get description")
        return self._description

    @description.setter
    def description(self, description):
        if re.match(r"^[a-zA-Z0-9\s,.'-]+$", description):
            raise ValueError("Invalid description")
        if len(description) > 500:
            raise ValueError("Description must be 500 characters or fewer")
        self._description = description

    def to_tuple(self):
        return (self.id, self.name_clothes,self.fabric, self.color,self.price, self.size, self.description)

    name_clothes = property(fget=Clothes.name_clothes.fget, fset=Clothes.name_clothes.fset)
    fabric = property(fget=Clothes.fabric.fget, fset=Clothes.fabric.fset)
    color = property(fget=Clothes.color.fget, fset=Clothes.color.fset)
    price = property(fget=Clothes.price.fget, fset=Clothes.price.fset)
    size = property(fget=Clothes.size.fget, fset=Clothes.size.fset)
    description = property(fget=Clothes.description.fget, fset=Clothes.description.fset)









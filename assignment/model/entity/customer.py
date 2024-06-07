from assignment.model.entity import *


class Customer(Base):
    __tablename__ = "customer_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    phone = Column(Boolean, default=False)
    email = Column(String(50),nullable=False)
    national_id = Column(String(10),unique = True,nullable=True)
    birth_date = Column(Date,nullable=True)


    order = relationship("Order", back_populates="customer")

    def __init__(self, name, family,phone,email,national_id,birth_date ):
        self.id = None
        self.name = name
        self.family = family
        self.phone = phone
        self.email = email
        self.national_id = national_id
        self.birth_date = birth_date

    def sign_up(self):
       print(f"{self.id}-{self._name}-{self.family}-{self.phone}-{self.email}-{self.national_id}-{self.birth_date} Signed Up")

    def sign_in(self):
       print(f"{self._name} Signed In !!!")

    @property
    def name(self):
        print("Get name")
        return self._name

    @name.setter
    def name(self, name):
        print("Set name")
        if re.match("^[A-Za-z\s]+$", name):
            self._name = name
        else:
            raise ValueError("Invalid name")

    @property
    def family(self):
        print("Get family")
        return self._family

    @family.setter
    def family(self, family):
        print("Set family")
        if re.match("^[A-Za-z\s]+$", family):
            self._family = family
        else:
            raise ValueError("Invalid family")

    @property
    def phone(self):
        print("Get phone")
        return self._phone

    @phone.setter
    def phone(self, phone):
        print("Set phone")
        if re.match("\+\d|\d{9,15}", phone):  # r'^\+?1?\d{9,15}$
            self._phone = phone
        else:
            raise ValueError("Invalid phone")

    @property
    def email(self):
        print("Get email")
        return self._email

    @email.setter
    def email(self, email):
        print("Set email")
        if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            self._email = email
        else:
            raise ValueError("Invalid email")

    @property
    def nationa_id(self):
        print("Get national id")
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        print("Set national id")
        if re.match("r'^\d{10}$'", national_id):
            self._national_id = national_id
        else:
            raise ValueError("Invalid national Id")

    @property
    def birth_date(self):
        print("Get birth_date")
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        print("set birth_date")
        if re.match("%Y/%m/%d", birth_date):
            self._birth_date = birth_date
        else:
            raise ValueError("Invalid birth_date, should be YYYY-MM-DD")

    def to_tuple(self):
        return (self.id, self.name, self.family, self.phone, self.email , self.national_id, self.birth_date)

    name = property(fget=Customer.name.fget, fset=Customer.name.fset)
    family = property(fget=Customer.family.fget, fset=Customer.family.fset)
    phone = property(fget=Customer.phone.fget, fset=Customer.phone.fset)
    email = property(fget=Customer.email.fget, fset=Customer.email.fset)
    national_id = property(fget=Customer.national_id.fget, fset=Customer.national_id.fset)
    birth_date = property(fget=Customer.birth_date.fget, fset=Customer.birth_date.fset)
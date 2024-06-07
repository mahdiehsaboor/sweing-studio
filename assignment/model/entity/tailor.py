from assignment.model.entity import *

class Tailor(Base):
    __tablename__ = "tailor_tbl"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(30),nullable=False)
    family = Column(String(30),nullable=False)
    phone = Column(Integer(15),nullable=False)
    salary = Column(Integer,nullable=False)
    national_id = Column(String(10),unique=True,nullable=True)
    birth_date = Column(Date,nullable=True)
    status = Column(Boolean, default=True)

    order = relationship("Order",back_populates="tailor")

    def __init__(self,name,family,phone,salary,national_id,birth_date,status):
        self.id = None
        self.name = name
        self.family = family
        self.phone = phone
        self.salary = salary
        self.national_id = national_id
        self.birth_date = birth_date
        self.status = status

    @property
    def name(self):
        print("Get name ")
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
        if re.match("\+\d|\d{11}", phone):  # r'^\+?1?\d{9,15}$
            self._phone = phone
        else:
            raise ValueError("Invalid phone")

    @property
    def salary(self):
        print("Get salary")
        return self._salary

    @salary.setter
    def salary(self, salary):
        print("Set salary")
        if salary >= 0:
            self._salary = salary
        else:
            raise ValueError("Salary must be a non-negative number")

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

    @property
    def status(self):
        print("Get status")#'accept' , 'refuse'
        return self._status

    @status.setter
    def status(self, status):
        print("Set status")
        if re.match("^(True|False)$", status):
            self._status = status
        else:
            raise ValueError("Invalid status")

    def to_tuple(self):
        return (
        self.id, self.name, self.family, self.phone, self.salary, self.national_id, self.birth_date, self.status)

    name = property(fget=Tailor.name.fget, fset=Tailor.name.fset)
    family = property(fget=Tailor.family.fget, fset=Tailor.family.fset)
    phone = property(fget=Tailor.phone.fget, fset=Tailor.phone.fset)
    salary = property(fget=Tailor.salary.fget, fset=Tailor.salary.fset)
    national_id = property(fget=Tailor.national_id.fget, fset=Tailor.national_id.fset)
    birth_date = property(fget=Tailor.birth_date.fget, fset=Tailor.birth_date.fset)
    status = property(fget=Tailor.status.fget, fset=Tailor.status.fset)






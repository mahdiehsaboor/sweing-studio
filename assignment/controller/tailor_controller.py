from assignment.model.bl.tailor_bl import TailorBl
from assignment.model.entity.tailor import Tailor
from assignment.model.tools.decorators import exception_handling


class TailorController:
    @classmethod
    @staticmethod
    @exception_handling
    def save(name,family,phone,salary,national_id,birth_date,status=True):
        tailor = Tailor(name,family,phone,salary,national_id,birth_date,status)
        return True, TailorBl.save(tailor)

    @staticmethod
    @exception_handling
    def edit(id,name,family,phone,salary,national_id,birth_date,status=True):
        tailor = Tailor(id,name, family,phone,salary,national_id,birth_date,status)
        tailor.id = id
        return True, TailorBl.edit(tailor)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, TailorBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, TailorBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, TailorBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_family(family):
        return True, TailorBl.find_by_family(family)



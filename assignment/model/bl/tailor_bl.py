from assignment.controller.exceptions import TailorNotFoundError
from assignment.model.da.da import DataAccess
from assignment.model.entity.tailor import Tailor

tailor_da = DataAccess(Tailor)

class TailorBl:
    @staticmethod
    def save(tailor):
        return tailor_da.save(tailor)

    @staticmethod
    def edit(tailor):
        if tailor_da.find_by_id(tailor.id):
            return tailor_da.edit(tailor)
        else:
            raise TailorNotFoundError()

    @staticmethod
    def remove(id):
        tailor = tailor_da.find_by_id(id)
        if tailor:
            return tailor_da.remove(tailor)
        else:
            raise TailorNotFoundError()

    @staticmethod
    def find_all():
        tailor_list = tailor_da.find_all()
        if tailor_list:
            return tailor_list
        else:
            raise TailorNotFoundError()

    @staticmethod
    def find_by_id(id):
        tailor = tailor_da.find_by_id(id)
        if tailor:
            return tailor
        else:
            raise TailorNotFoundError()

    @staticmethod
    def find_by_family(family):
        tailor_list = tailor_da.find_by(Tailor.family == family)
        if tailor_list:
            return tailor_list
        else:
            raise TailorNotFoundError()
from assignment.controller.exceptions.clothes_exceptions import ClothesNotFoundError
from assignment.model.da.da import DataAccess
from assignment.model.entity.clothes import Clothes

clothes_da = DataAccess(Clothes)


class ClothesBl:
    @staticmethod
    def save(clothes):
        return clothes_da.save(clothes)

    @staticmethod
    def edit(clothes):
        if clothes_da.find_by_id(clothes.id):
            return clothes_da.edit(clothes)
        else:
            raise ClothesNotFoundError()

    @staticmethod
    def remove(id):
        clothes = clothes_da.find_by_id(id)
        if clothes:
            return clothes_da.remove(clothes)
        else:
            raise ClothesNotFoundError()

    @staticmethod
    def find_all():
        clothes_list = clothes_da.find_all()
        if clothes_list:
            return clothes_list
        else:
            raise ClothesNotFoundError()

    @staticmethod
    def find_by_id(id):
        clothes = clothes_da.find_by_id(id)
        if clothes:
            return clothes
        else:
            raise ClothesNotFoundError()

    @staticmethod
    def find_by_name_clothes(name_clothes):
        clothes_list = clothes_da.find_by(ClothesBl.name_clothes == name_clothes)
        if clothes_list:
            return clothes_list
        else:
            raise ClothesNotFoundError()
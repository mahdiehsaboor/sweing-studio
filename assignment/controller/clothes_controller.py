from assignment.model.bl.clothes_bl  import ClothesBl
from assignment.model.entity.clothes import Clothes
from assignment.model.tools.decorators import exception_handling



class  ClothesController:

    @staticmethod
    @exception_handling
    def save(id,name_clothes ,fabric, color, price, size, description):
        clothes = Clothes(name_clothes, fabric, color, price, size, description)
        return True, ClothesBl.save(clothes)

    @staticmethod
    @exception_handling
    def edit(id, name_clothes, fabric, color, price, size, description):
        clothes = Clothes(id, name_clothes, fabric, color, price, size, description)
        clothes.id = id
        return True, ClothesBl.edit(clothes)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, ClothesBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, ClothesBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, ClothesBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_name_clothes(name_clothes):
        return True, ClothesBl.find_by_name_clothes(name_clothes)



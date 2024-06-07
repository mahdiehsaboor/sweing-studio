from xml.dom.minidom import Document

from assignment.model.da.da import DataAccess
from assignment.model.entity import *

#Entity test
#customer=Customer("Ali","Alipour","+989141632595","1234567890","1374/3/27")
#print(customer)

#tailor=Tailor("Alireza","Alipouryy","09142561265","5000","1374/3/27")
#print(tailor)
tailor_da = DataAccess(Tailor)

#clothes=Clothes("suit","cotton ","gray","450","l","no pocket")
#print(clothes)
clothes_da = DataAccess(Clothes)

#order=Order("1403/2/15","1403/3/10 ","compeleted","78945612","12345678")
#print(order)
order_da = DataAccess(Order)


customer = Customer("ali","Alipour","+989142361245","1234567890","1374/3/27")
print(customer)
customer_da = DataAccess(Customer)
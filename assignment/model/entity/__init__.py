from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey,Numeric
from sqlalchemy.orm import relationship

import re

from assignment.model.entity.base import Base
from assignment.model.entity.customer import Customer
from assignment.model.entity.tailor import Tailor
from assignment.model.entity.order import Order
from assignment.model.entity.clothes import Clothes

from assignment.model.tools.validator import Validator
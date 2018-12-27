from functools import reduce


class Product(object):
    price = 0
    packing_charges = 0
    
    def __init__(self, price, packing_charges=0):
        self.price = price
        self.packing_charges = packing_charges
        
    @property
    def should_pay(self):
        return self.price + self.packing_charges

    
class Customer(object):
    orders = []
    bill = 0
    
    @property
    def should_pay(self):
        return sum(map(lambda x: x.should_pay, self.orders))
    

class Coupon(object):
    cost = 0
    preciprice = 0
    
    def __init__(self, preciprice, cost=0):
        self.preciprice = preciprice
        self.cost = cost
        

class FullReduction(object):
    full = 0
    reduction = 0
    
    def __init__(self, full, reduction):
        if full < reduction:
            raise ValueError
        self.full = full
        self.reduction = reduction
        
    @property
    def off_percent(self):
        return '{}%'.format((self.reduction/self.full) * 100)
    
    
class Order(object):
    customers = []
    coupons = []
    full_reduction = []
    carriage = 0
    
    @property
    def should_pay(self):
        return sum(map(lambda x: x.should_pay, self.customers))
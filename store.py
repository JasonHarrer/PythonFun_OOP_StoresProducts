import product as p

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product, id=''):
        if not isinstance(new_product, p.Product):
            print(f'Error: {new_product} is not a valid Product.')
        else:
            if self.id_exists(id):
                print(f'Error: id {id} already exists.  Product cannot be added.')
            else:
                if(id==''):
                    id = 1
                    while self.id_exists(id):
                        id += 1
                print(f'Adding new product {id} {new_product.name}')
                new_product.set_id(id)
                self.products.append(new_product)

    def sell_product(self, id):
        for i in range(len(self.products)):
            if self.products[i].id == id:
                self.products.remove(i)
                return
        print('Error: Product ID #{id} does not exist.')
        return
    
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)

    def id_exists(self, id):
        for product in self.products:
            if product.id == id:
                return True
        return False

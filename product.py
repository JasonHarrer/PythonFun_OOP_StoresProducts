class Product:
    def __init__(self, name, price, category):
        self.id       = ''
        self.name     = name
        self.price    = price
        self.category = category

    def set_id(self, id):
        self.id = id

    def update_price(self, percent_change, is_increased):
        difference = self.price * percent_change
        if is_increased:
            self.price += difference
        else:
            self.price -= difference

    def print_info(self):
        print(f'Product: {self.id}\t{self.name}\tCategory: {self.category}')
        print(f'       Price: ${self.price:.2f}')


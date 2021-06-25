import store as s
import product as p


if __name__ == '__main__':
    my_store  = s.Store('Boring Store Name')
    p1     = p.Product('Flashy New Techno Gizmo Doohicky', 10.50, 'Electronics')
    p2     = p.Product('Bananas', .50, 'Fruit')
    p3     = p.Product('Cardboard Boxes', 8.50, 'Moving Supplies')
    p4     = p.Product('Apples', .35, 'Fruit')
    p5     = p.Product('Non-Electronic Electronic Thingy', 15.50, 'Electronics')
    p6     = "All filler, no substance"

    my_store.add_product(p1, 'id010')
    my_store.add_product(p2)
    my_store.add_product(p3)
    my_store.add_product(p4)
    my_store.add_product(p5, 'id010')
    my_store.add_product(p6)

    print(f'Welcome to {my_store.name}')
    print('Our products include:')
    for product in my_store.products:
        product.print_info()
        print()

    my_store.inflation(0.055)
    print('Unfortunately, we just had to raise prices due to inflation.  Here are the new prices:')
    for product in my_store.products:
        product.print_info()
        print()

    my_store.set_clearance('Electronics', 0.035)
    print('We\'re not complete money grubbers though!!!')
    print('We decided afterwards to reduce the price of your electronics:')
    for product in my_store.products:
        product.print_info()
        print()

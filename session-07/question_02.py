def process_order(customer, *products, **options):
    discount=options.get('discount',0)
    tax=options.get('tax',0)
    shipping=options.get('shipping',0)
    products=list(products)
    options['customer']=customer
    options['products']=list(products)
    options['discount']=discount
    options['tax']=tax
    options['shipping']=shipping
    
    return options

print(process_order())
    
    
    

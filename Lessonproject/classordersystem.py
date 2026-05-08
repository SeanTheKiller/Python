class Shop:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def order(self):
        print(f"ordering {item.stock} by {self.customer_name}")

    def sell(self):
        pass

    def check_stock(self):
        pass

class item:
    def __init__(self, product_name):
        self.product_name = product_name

    def stock(self):
        items = [{"product_name":"Apple", "price": 1600}, 
                 {"product_name":"Google_Pixel", "price": 1600}, 
                 {"product_name":"Samsung", "price": 1600}]
        
        for i in items:
            if i["product_name"].lower() == self.product_name:
                print(f"{i["product_name"]}: Found it! The price is {i['price']}")
    



    